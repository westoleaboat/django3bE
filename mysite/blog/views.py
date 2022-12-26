from django.shortcuts import render, get_object_or_404
from .models import Post, Comment
# pagination
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# class-based views
from django.views.generic import ListView
# handling forms in views
from .forms import EmailPostForm, CommentForm
# tagging
from taggit.models import Tag


# Create your views here.


class PostListView(ListView):  # PAGE37 d3be
    queryset = Post.published.all()
    context_object_name = 'posts'
    paginate_by = 3
    template_name = 'blog/post/list.html'


def post_share(request, post_id):  # 42d3be
    # retireve post by id
    post = get_object_or_404(Post, id=post_id, status='published')
    # distinguish betweem request method.
    if request.method == 'POST':
        # Form was submitted
        form = EmailPostForm(request.POST)
        if form.is_valid():
            # Form fields passed validation
            cd = form.cleaned_data
            # ... send email
        else:
            form = EmailPostForm()
        return render(request, 'blog/post/share.html', {'post': post,
                                                        'form': form})


def post_list(request, tag_slug=None):  # PAGINA26-27/34 django3byexample
    object_list = Post.published.all()
    # tagging
    tag = None
    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        object_list = object_list.filter(tags__in=[tag])
    # instantiate the Paginator class with the number of objects that you want to display on each page.
    paginator = Paginator(object_list, 3)  # 3 post in each page
    # you get the page GET parameter, indicates the current page #
    page = request.GET.get('page')
    try:
        # obtain objects for the desider page with page() method
        posts = paginator.page(page)
    except PageNotAnInteger:
        # if page not an integer deliver first page
        posts = paginator.page(1)
    except EmptyPage:
        # if page is out of range deliver last page of results
        posts = paginator.page(paginator.num_pages)

    # pass the page number and retrieved pbjects to the template
    return render(request,
                  'blog/post/list.html',
                  {'page': page,
                   'posts': posts,
                   'tag': tag})


def post_detail(request, year, month, day, post):
    """ This view takes the year, month,day and post arguments to retrieve a published post with the given slug and date. """
    post = get_object_or_404(Post, slug=post,
                             status='published', publish__year=year, publish__month=month, publish__day=day)

    # List of active comments for this post
    comments = post.comments.filter(active=True)
    new_comment = None

    if request.method == 'POST':
        # A comment was posted
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            # Create comment object but dont save to database yet
            new_comment = comment_form.save(commit=False)
            # Assing the current post to the comment
            new_comment.post = post
            # save the comment to the database
            new_comment.save()
    else:
        comment_form = CommentForm()

    return render(request, 'blog/post/detail.html', {'post': post, 'comments': comments,
                                                     'new_comment': new_comment,
                                                     'comment_form': comment_form})
