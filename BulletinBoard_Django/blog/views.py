from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.urls import reverse_lazy, reverse
from django.utils import timezone
from .models import Post, Comment, Favorite
from .forms import PostForm, CommentForm

"""
published_date <= timezone.now()
公開日が現在の時間より前の時

render関数では、パラメーターとしてrequestとtemplate fileが渡されている。
リクエストとは、インターネットを介してユーザから受け取った全ての情報が詰まったもの。
render関数の最後の引数 {} はこの中に指定した情報を、テンプレートが表示する。
表示させたいのはクエリセットのデータなので、postsを指定
'posts'は名前
postsは値、クエリセットのこと
"""


def post_list(request):
    all_post = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    paginator = Paginator(all_post, 5)
    page = request.GET.get('page')
    lists = paginator.get_page(page)
    context = {
        'lists': lists,
    }

    return render(request, 'blog/post_list.html', context)


def post_detail(request, pk):
    # 未ログインならログインページにリダイレクト
    if not request.user.is_authenticated:
        return redirect('/accounts/login/?next=%s' % request.path)
    post = get_object_or_404(Post, pk=pk)
    comments = Comment.objects.filter(post=post).order_by('-created_date')

    context = {
        'post': post,
        'comments': comments,
    }

    return render(request, 'blog/post_detail.html', context)


@login_required
def post_new(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            post.publish()

            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()

    context = {
        'form': form,
    }

    return render(request, 'blog/post_edit.html', context)


@login_required
# 投稿の編集
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()

            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)

    context = {
        'form': form,
    }

    return render(request, 'blog/post_edit.html', context)


@login_required
# 下書きリスト表示
# def post_draft_list(request):
#     posts = Post.objects.filter(published_date__isnull=True).order_by('created_date')
#
#     context = {
#         'posts': posts,
#     }
#     return render(request, 'blog/post_draft_list.html', context)
@login_required
# 公開する
def post_publish(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.publish()
    return redirect(request, 'post_detail', pk=pk)


@login_required
# 削除関数
def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('post_list')


@login_required
# コメント投稿
def add_comment_to_post(request, pk):
    post = get_object_or_404(Post, pk=pk)

    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = CommentForm()

    context = {
        'form': form,
    }

    return render(request, 'blog/add_comment_to_post.html', context)


@login_required
# お気に入り機能
def add_favorite_to_post(request, pk):
    post = get_object_or_404(Post, pk=pk)

    if request.method == 'GET':

        is_favorite = Favorite.objects.filter(user=request.user).filter(post=post).count()

        global favorite_style
        # お気に入り取り消し
        if is_favorite > 0:
            favorite_style = 'far favorite-i'
            do_favorite = Favorite.objects.get(post__id=pk, user=request.user)
            do_favorite.delete()
            post.favorite_num -= 1
            post.save()
            return redirect('post_detail', pk=pk)

        else:
            # お気に入り追加
            favorite_style = 'fas click-favorite-i'
            post.favorite_num += 1
            post.save()
            favorite = Favorite()
            favorite.user = request.user
            favorite.post = post
            favorite.save()
            return redirect('post_detail', pk=pk)

    context = {
        'favorite_style': favorite_style,
        'favorite_num': post.favorite_num,
    }

    return render(request, 'blog/post_detail.html', context)
# def already_liked_post(user, post_id):
#
#     post= Post.objects.get(id=post_id)
#     return Favorite.objects.filter(user=user, post=post).exists()
#
#
# def like_button_clicked(request, post_id):
#
#     if request.user.is_authenticated():
#         post = Post.objects.get(id=post_id)
#
#         if not already_liked_post(request.user, post_id):
#             Favorite.objects.create(user=request.user, post=post, timestamp=timezone.now)
#         else:
#             Favorite.objects.filter(user=request.user, post=post).delete()
#
#         return redirect(reverse('index'))
#     else:
#         return redirect(reverse('login'))


# @login_required
# def comment_approve(request, pk):
#     comment = get_object_or_404(Comment, pk=pk)
#     comment.approve()
#     return redirect('post_detail', pk=comment.post.pk)
#
#
# @login_required
# def comment_remove(request, pk):
#     comment = get_object_or_404(Comment, pk=pk)
#     comment.delete()
#     return redirect('post_detail', pk=comment.post.pk)

