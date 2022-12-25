from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    # post views PAGE28 django3byexample
    #path('', views.post_list, name='post_list'),
    path('', views.PostListView.as_view(), name='post_list'),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/',
         views.post_detail, name='post_detail'),
]

# In order to keep pagination working, you have to use the right page object that is passed to the template, check post/list.html template and use right variable: page=page_obj PAGE37 d3be
# {% include "pagination.html" with page=page_obj %}
