from django.shortcuts import render
from .models import Post

# This function sends a httpresponse when a user goes to the home page.
# Views.py talks to the blog directory > home.html file
def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request,'blog/home.html', context)

# This function sends a httpresponse when a user enters a URL path /about
# and it renders the about.html template that we created in the templates > blog directory
def about(request):
    return render(request,'blog/about.html', {'title': 'About'})

# Create your views here.
