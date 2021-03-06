from django.shortcuts import render,get_object_or_404
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from .models import Post,CategoryList,Comment
from .forms import PostForm,UpdatePostForm,AddCommentForm
from django.urls import reverse_lazy,reverse
from django.http import HttpResponseRedirect
#def home(request):
#    return render(request,'home.html',{})

# Create your views here.
class IndexView(ListView):
    model = Post
    template_name = 'Index.html'
    ordering = ['-pub_Date']

    def get_context_data(self, *args, **kwargs):
        cat_menu = CategoryList.objects.all()
        cat_count = []
        tags = Post.objects.all().values_list('title_tag', 'title_tag')
        for item in cat_menu:
            number = Post.objects.filter(category=item).count()
            cat_count.append(number)
        print(cat_menu)
        poem = Post.objects.filter(category='Poem').order_by('-pub_Date')
        story = Post.objects.filter(category='Story').order_by('-pub_Date')
        context = super(IndexView,self).get_context_data(*args, **kwargs)

        context["zipped"] = zip(cat_menu,cat_count)
        context["poem"] = poem
        context["story"] = story
        context["tags"] = tags

        #context["cat_count"] = cat_count
        return context
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
    #success_url = reverse_lazy('article-detail',kwargs={'id':id})

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
    category_post = Post.objects.filter(category=cats.title().replace('-',' ')).order_by('-pub_Date')
    return render(requests,'categories.html',{'cats':cats.title().replace('-',' '),'category_post':category_post})

def LikeView(request, pk):
    LikeAdd = get_object_or_404(Post, id=request.POST.get('post_ids'))
    liked = False
    if LikeAdd.likes.filter(id=request.user.id).exists():
        LikeAdd.likes.remove(request.user)
        liked = False
    else:
        LikeAdd.likes.add(request.user)
        liked = True
    return HttpResponseRedirect(reverse('article-detail',args=[str(pk)]))

class AddCommentView(CreateView):
    model = Comment
    form_class = AddCommentForm
    template_name = 'add_comment.html'

    def form_valid(self,form):
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('article-detail', kwargs={'pk': self.kwargs['pk']})



