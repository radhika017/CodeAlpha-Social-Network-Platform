from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Post, Comment, Follow


@login_required
def home(request):
    posts = Post.objects.all().order_by('-created_at')

    if request.method == 'POST':
        content = request.POST.get('content')

        if content:
            Post.objects.create(
                user=request.user,
                content=content
            )

        return redirect('home')

    return render(request, 'home.html', {
        'posts': posts
    })


@login_required
def like_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    if request.user in post.likes.all():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)

    return redirect('home')


@login_required
def add_comment(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    if request.method == 'POST':
        text = request.POST.get('text')

        if text:
            Comment.objects.create(
                user=request.user,
                post=post,
                text=text
            )

    return redirect('home')


@login_required
def follow_user(request, user_id):
    user_to_follow = get_object_or_404(User, id=user_id)

    if request.user != user_to_follow:
        follow, created = Follow.objects.get_or_create(
            follower=request.user,
            following=user_to_follow
        )

        if not created:
            follow.delete()

    return redirect('home')


@login_required
def profile(request, user_id):
    profile_user = get_object_or_404(User, id=user_id)

    posts = profile_user.posts.all()

    return render(request, 'profile.html', {
        'profile_user': profile_user,
        'posts': posts
    })