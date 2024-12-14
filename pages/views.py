from django.shortcuts import render
from django.views.generic import ListView,DetailView
from .models import Post,Mir,Obshestvo

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


    
class ObshestvoListViev(ListView):
    model=Obshestvo
    template_name='obshestvo.html'    
class Obshestvo_detail(DetailView):
    model=Obshestvo
    template_name='obshestvo_detail.html'
class Obshestvo2_detail(DetailView):
    model=Obshestvo
    template_name='obshestvo2_detail.html'
