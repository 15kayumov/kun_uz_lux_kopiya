from django.shortcuts import render
from django.views.generic import ListView,DetailView
from .models import Post,Mir

class HomeListViev(ListView):
    model=Post
    template_name='home.html'
class Post_detail(DetailView):
    model=Post
    template_name='post_detail.html'
class Post2_detail(DetailView):
    model=Post
    template_name='post2_detail.html'

class MirListViev(ListView):
    model=Mir
    template_name='mir.html'    
class Mir_detail(DetailView):
    model=Mir
    template_name='mir_detail.html'
class Mir2_detail(DetailView):
    model=Mir
    template_name='mir2_detail.html'
