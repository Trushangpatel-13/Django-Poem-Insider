from django.shortcuts import render
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from .models import Post,CategoryList
from .forms import PostForm,UpdatePostForm
from django.urls import reverse_lazy
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
        context["cat_menu"] = cat_menu
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
