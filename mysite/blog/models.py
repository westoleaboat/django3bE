from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# canonical URLS for models
from django.urls import reverse
# tagging
from taggit.managers import TaggableManager

# Create your models here.
# The first manager declared in a model becomes the default manager.


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager, self).get_queryset().filter(status='published')


class Post(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    # pagina 11 django3byexample
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique_for_date='publish')
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='blog_posts')
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(
        max_length=10, choices=STATUS_CHOICES, default='draft')
    objects = models.Manager()  # The default manager.
    published = PublishedManager()  # Our custom manager.
    tags = TaggableManager()  # page58

    def get_absolute_url(self):
        """ Use the get_absolute_url() method in your templates to link to specific posts."""
        return reverse("blog:post_detail", args=[self.publish.year, self.publish.month, self.publish.day, self.slug])

    class Meta:
        # The Meta class inside the model contains metadata. You tell Django to sort
        # results by the publish field in descending order by default when you query the database.
        # You specify the descending order using the negative prefix. By doing this, posts published recently will appear first.
        ordering = ('-publish',)

    def __str__(self):
        # The __str__() method is the default human-readable representation of the object.
        return self.title


class Comment(models.Model):
    '''
    many-to-one relationship. page50 
    '''
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)  # deactivate comments

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return f'Comment by {self.name} on {self.post}'
