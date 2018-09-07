from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse, resolve
from django.views import generic

from .forms import AvatarForm, CommentForm, PostForm
from .models import Post, User


class HomeView(generic.ListView):
    model = Post
    template_name = 'blabber/home.html'
    context_object_name = 'posts'

    def get_context_data(self, object_list=None, **kwargs):
        """Insert the forms into the context dict."""
        context = super().get_context_data(**kwargs)
        if 'post_form' not in context:
            context['post_form'] = PostForm()
        if 'comment_form' not in context:
            context['comment_form'] = CommentForm()
        return context


class ProfileView(generic.DetailView):
    model = User
    template_name = 'blabber/profile.html'
    context_object_name = 'custom_user'
    slug_field = 'username'
    slug_url_kwarg = 'username'

    def get_context_data(self, **kwargs):
        """Insert the forms into the context dict."""
        context = super().get_context_data(**kwargs)
        if 'post_form' not in context:
            context['post_form'] = PostForm()
        if 'comment_form' not in context:
            context['comment_form'] = CommentForm()
        return context

    # def get(self, request, *args, **kwargs):
    #     self.object = self.get_object()
    #     form = PostForm()
    #     context = self.get_context_data()
    #     context.update({'form': form})
    #     return self.render_to_response(context)

    # def post(self, request):
    #     form = PostForm(request.POST, request.FILES)
    #     user = request.user
    #     if form.is_valid():
    #         post = form.save(commit=False)
    #         post.created_by = user
    #         post.save()
    #         return redirect('blabber:home')


class CommentFormView(generic.FormView):
    form_class = CommentForm

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            pk = kwargs['pk']
            return self.form_valid(form, pk)
        else:
            return self.form_invalid(form)

    def form_valid(self, form, pk):
        comment = form.save(commit=False)
        comment.created_by = self.request.user
        comment.to = Post.objects.get(pk=pk)
        comment.save()
        return redirect(self.request.POST.get('next'))


class PostFormView(generic.FormView):
    form_class = PostForm

    def form_valid(self, form):
        post = form.save(commit=False)
        post.created_by = self.request.user
        post.save()
        return redirect(self.request.POST.get('next'))


class AvatarView(generic.UpdateView):
    model = User
    form_class = AvatarForm
    template_name = 'blabber/edit_avatar.html'

    def get_success_url(self):
        user = self.get_object()
        url = reverse('blabber:profile', args=[user.username])
        return url


class LikeToggleView(generic.View):

    def get(self, request, pk=None):
        post = get_object_or_404(Post, pk=pk)
        user = request.user
        url = request.GET.get('next')
        if user.is_authenticated:
            if post.likes.filter(pk=user.pk).exists():
                post.likes.remove(user)
            else:
                post.likes.add(user)
            post.save()
        if request.is_ajax():
            data = {
                'likes_count': post.likes.count()
            }
            return JsonResponse(data)
        return HttpResponseRedirect(url)
