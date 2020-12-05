from django.shortcuts import render,get_object_or_404
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from .models import Post,CategoryList
from .forms import PostForm,UpdatePostForm
from django.urls import reverse_lazy,reverse
from django.http import HttpResponseRedirect
#def home(request):
#    return render(request,'home.html',{})

# Create your views here.
class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    ordering = ['-pub_Date']

    def get_context_data(self, *args, **kwargs):
        cat_menu = CategoryList.objects.all()
        context = super(HomeView,self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context

class ArticleDetailView(DetailView):
    model = Post
    template_name = 'article_detail.html'
    def get_context_data(self, *args, **kwargs):
        cat_menu = CategoryList.objects.all()
        context = super(ArticleDetailView,self).get_context_data(*args, **kwargs)
        stuff = get_object_or_404(Post,id=self.kwargs['pk'])
        total_likes = stuff.total_likes()
        liked = False
        if stuff.likes.filter(id=self.request.user.id).exists():
            liked = True
        context["cat_menu"] = cat_menu
        context["total_likes"] = total_likes
        context["liked"] = liked

        return context
class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'
    #fields = '__all__'
class UpdatePostView(UpdateView):
    model = Post
    form_class = UpdatePostForm
    template_name = 'update_post.html'
class DeletePostView(DeleteView):
    model = Post
    form_class = UpdatePostForm
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')

def CategoryView(requests,cats):
    category_post = Post.objects.filter(category=cats.title().replace('-',' '))
    return render(requests,'categories.html',{'cats':cats.title().replace('-',' '),'category_post':category_post})

def LikeView(request, pk):
    print(request)
    LikeAdd = get_object_or_404(Post, id=request.POST.get('post_ids'))
    liked = False
    if LikeAdd.likes.filter(id=request.user.id).exists():
        LikeAdd.likes.remove(request.user)
        liked = False
    else:
        LikeAdd.likes.add(request.user)
        liked = True
    return HttpResponseRedirect(reverse('article-detail',args=[str(pk)]))


