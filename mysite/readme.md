creating and applying migrations PAGE14 django3byexample
If you edit the models.py file in order to add, remove, or change the fields of existing 
models, or if you add new models, you will have to create a new migration using the 
makemigrations command. The migration will allow Django to keep track of model 
changes. Then, you will have to apply it with the migrate command to keep the 
database in sync with your models.

Create a post from shell
python manage.py shell
Then, type the following lines:
>>> from django.contrib.auth.models import User
>>> from blog.models import Post
>>> user = User.objects.get(username='admin')
>>> post = Post(title='Another post',
... slug='another-post',
... body='Post body.',
... author=user)
>>> post.save()

-creating a comment system page50
![Screenshot_select-area_20221226145817](https://user-images.githubusercontent.com/68698872/209551506-2448def4-3176-4f8d-be5b-4e0453c9a04d.png)
