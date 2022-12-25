from django.contrib import admin
from .models import Post, Comment

# Register your models here.
# admin.site.register(Post)
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    # You are telling the Django administration site that your model is registered in 
    # the site using a custom class that inherits from ModelAdmin. In this class, you 
    # can include information about how to display the model in the site and how to 
    # interact with it.

    # The list_display attribute allows you to set the fields of your model that you 
    # want to display on the administration object list page. The @admin.register()
    # decorator performs the same function as the admin.site.register() function 
    # that you replaced, registering the ModelAdmin class that it decorates. #PAGINA20 django3byexample
    list_display = ('title', 'slug', 'author', 'publish', 'status')
    list_filter = ('status', 'created', 'publish', 'author')
    search_fields = ('title', 'body')
    raw_id_fields = ('author',)
    date_hierarchy = 'publish'
    ordering = ('status', 'publish')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'post', 'created', 'active')
    list_filter = ('active', 'created', 'updated')
    search_fields = ('name', 'email', 'body')