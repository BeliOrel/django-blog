from django.shortcuts import render, get_object_or_404

# LoginRequiredMixin -> this takes care of the pages that require Login ->
# if not logged in, it redirects to login page
# UserPassesTestMixin -> allows only the right owner to edit the data
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User

from django.views.generic import (
                                ListView,
                                DetailView,
                                CreateView,
                                UpdateView,
                                DeleteView
)

from .models import Post
# from django.http import HttpResponse

'''
def home(request):
    context = {
        'posts': Post.objects.all()
    }
    # the keys of context are gonna be available in the template
    return render(request, 'blog/home.html', context)
'''

class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html' # <app>/<model>_<viewtype>.html
    # so that we know what variable to use in the template
    # by default it's named 'object_list'
    context_object_name = 'posts'
    ordering = ['-date_posted'] # newest at the top
    paginate_by = 5 # 5 posts per page

class UserPostListView(ListView):
    model = Post
    template_name = 'blog/user_posts.html'
    context_object_name = 'posts'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')


class PostDetailView(DetailView):
    model = Post
    # we don't need to define template_name because
    # the template for post details already have
    # the default template name django is searching for
    # also by default context_object_name here is named 'object'

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    # we want to use current logged in user as an author
    # so we need to overwrite function for form validation
    # for a successful form submit we need an author
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    # for this view we don't need template
    # because it uses same template as PostCreateView

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    # test function for UserPassesTestMixin
    def test_func(self):
        post = self.get_object()
        # check if the author of the post
        if self.request.user == post.author:
            return True
        return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    # after we successfuly deleted post we need to redirect somewhere
    success_url = '/'  # redirect to home page

    # test function for UserPassesTestMixin
    def test_func(self):
        post = self.get_object()
        # check if the author of the post
        if self.request.user == post.author:
            return True
        return False

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
