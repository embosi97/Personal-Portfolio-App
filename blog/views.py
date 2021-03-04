from django.shortcuts import render, get_object_or_404
from .models import Blog

#get_object_or_404 gets a particular object or a 404 error if it doesn't exist

# Create your views here.
def the_blog(request):
    #grabs all the blog objects from the DB
    blogs = Blog.objects.order_by('-date')
    return render(request, 'blog/myblog.html', {'blogs': blogs})


def details(request, blog_id):
    a_blog = get_object_or_404(Blog, pk = blog_id)
    return render(request, 'blog/detail.html', {'a_blog':a_blog})
