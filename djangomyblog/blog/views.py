# djangomyblog\blog\views.py

from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm
from blog.models import Post


def home(request):

    posts = (
        Post.objects
        .filter(status='ON')
        .select_related('user')
        .order_by('-created_at')
    )

    return render(request, "blog/home.html", {"posts": posts})


def about(request):
    return render(request, "blog/about.html")

# Só acessa profile() se estiver logado
# Não está logado, vai para '/accounts/login/'


@login_required
def profile(request):
    return render(request, "blog/profile.html")


def signup(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = CustomUserCreationForm()

    return render(request, "registration/signup.html", {"form": form})


def post_detail(request, id):
    post = get_object_or_404(Post, id=id, status='ON')

    # Lista apenas comentários ON do post
    comments = Comment.objects.filter(
        post=post,
        status='ON'
    ).select_related('user').order_by('-created_at')

    # Formulário inicial
    form = CommentForm()

    # Se o usuário enviou um comentário
    if request.method == 'POST':
        if request.user.is_authenticated:
            form = CommentForm(request.POST)
            if form.is_valid():
                new_comment = form.save(commit=False)
                new_comment.user = request.user
                new_comment.post = post
                new_comment.save()
                return redirect('post_detail', id=post.id)

    return render(
        request,
        "blog/post_detail.html",
        {
            "post": post,
            "comments": comments,
            "form": form
        }
    )


@login_required
def new_post(request):

    if request.method == "POST":
        title = request.POST.get("title")
        content = request.POST.get("content")

        if title and content:
            Post.objects.create(
                title=title,
                content=content,
                user=request.user,
                status='ON'
            )
            return redirect("home")

    return render(request, "blog/new_post.html")

@login_required
def delete_post(request, id):
    post = get_object_or_404(
        Post,
        id=id,
        status='ON'
    )

    if post.user != request.user:
        return redirect('home')

    post.status = 'DEL'
    post.save(update_fields=['status'])

    return redirect('home')