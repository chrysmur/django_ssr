from django.shortcuts import render
from .models import Post

# we  call the database models get values and pass it to the context
def home(request):
    return render(
        request, 
        'blog/home.html', 
        context={'title':'home', 'posts': Post.objects.all()}
    )

def about(request):
    return render(
        request,
        'blog/about.html',
        context={})


