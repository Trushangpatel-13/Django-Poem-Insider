from django.shortcuts import render
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from .models import Post
from .forms import PostForm,UpdatePostForm
from django.urls import reverse_lazy
#def home(request):
#    return render(request,'home.html',{})

# Create your views here.
class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    ordering = ['-id']
class ArticleDetailView(DetailView):
    model = Post
    template_name = 'article_detail.html'
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