from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

#python3 manage.py makemigrations 
#sql code -> python3 manage.py sqlmigrate blog 0001
#python3 manage.py migrate -> apply all migrations
#python3 manage.py shell
#from blog.models import Post
#from django.contrib.auth.models import User
#see all the users -> User.objects.all()
#User.objects.first()
#User.objects.filter(username='mwia')
#user = User.objects.filter(username='mwia').first() -> then run user variable
#user = User.objects.get(id=1)
#create a Post
#post_1 = Post(title='Blog 1', content='First Post Content!', author=user)
#post_1.save() -> save our post to our database
#post_2 = Post(title='Blog 2', content='Second Blog Post', author_id=user.id)
#post = Post.objects.first() -> post.author -> post.author.email
#fetch all posts by a specific user
#.modelname_set -> user.post_set
#user.post_set.all()
#user.post_set.create(title='Blog 3', content='Third Blog Post')
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    #date_posted = models.DateTimeField(auto_now_add=True)
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE) 
    #on deleting user it deletes his posts
    
    def __str__(self):
        return self.title 
    #exit shell and run again from blog.models import Post
    #from django.contrib.auth.models import User
    #Post.objects.all() -> it will gives us the title of the post
    
