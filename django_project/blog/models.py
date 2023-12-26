from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
# This is Post model or Post class. Model/Class is the same
# Each class is going to be its own table in the Database.
# Each attribute will be its own field in the Database.
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    #you cannot update the last_date posted if you use the argument "auto_now_add" in the DateTimeField function in line 13.
    # if you want the option for users to change the dates, use "default" argument
    date_posted = models.DateTimeField(default=timezone.now)
    # Author is the user who created the post. First we need to import the User model.
    # on_delete argument means that if user is deleted, the post will also be deleted.
    author = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.title


