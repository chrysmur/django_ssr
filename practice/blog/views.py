from django.shortcuts import render
from django.views.generic import (
    ListView, 
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
    )
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Post

# we  call the database models get values and pass it to the context
class PostListView(LoginRequiredMixin, ListView):
    model = Post
    context_object_name = 'posts' # rename the default content name for listviews
    template_name='blog/home.html' # rename the templates
    ordering = ['-date_posted'] # order in descending order

class PostDetailView(LoginRequiredMixin, DetailView):
    model = Post
    
class PostCreateView(LoginRequiredMixin, CreateView):
    '''
    the above creates the form for  new post, 
    on submit, django needs to get the user logged in, so we have to access the user from request
    #We intercept the form_valid, modify the form by adding user and then let it go to save
   '''
    model = Post
    fields = ['title','content'] # create form is expected to be post_form

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    #user passes this test
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

     #user passes this test
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
    
def about(request):
    return render(
        request,
        'blog/about.html',
        context={})


