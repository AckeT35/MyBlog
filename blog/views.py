from django.views.generic import ListView, DetailView

from blog.models import Post

class PostList(ListView):
    """ Представление списка """
    
    model = Post
    context_object_name = 'post_list'
    template_name = 'blog/base.html'

class PostDetail(DetailView):
    """ Представление списка """
    
    model = Post
    context_object_name = 'post'
    template_name = 'blog/index.html'
        

#()