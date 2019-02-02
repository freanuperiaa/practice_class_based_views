from django.shortcuts import redirect, render
from django.views.generic import (
    TemplateView,
    ListView,
    DetailView,
)
from django.views.generic.edit import (
     CreateView,
     UpdateView,
     DeleteView,
)
from django.utils import timezone
from django.urls import reverse_lazy
from .models import Post


# Create your views here.

class HomePageView(TemplateView):
    template_name = 'home.html'

class AboutPageView(TemplateView):
    template_name = 'about.html'

class PostListView(ListView):
    model = Post
    template_name = 'posts.html'

class PostDetailView(DetailView):
    model = Post
    template_name ='post.html'

class PostCreateView(CreateView):
    model = Post
    template_name = 'post_add.html'
    fields = [
        'title',
        'category',
        'content',
    ]
    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.pub_date = timezone.now()
        obj.save()
        return redirect(obj.get_absolute_url())

class PostUpdateView(UpdateView):
    model = Post
    template_name = 'post_edit.html'
    fields = [
        'title',
        'category',
        'content',
    ]

class PostDeleteView(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('home')