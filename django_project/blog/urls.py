from django.urls import path
from . import views

#this tells django where to route your request
# URL patterns contain a list of paths. It refers to the views.py page where we defined our home function and about function

# If we change the first value '' to 'home', when we go to localhost:8000/home, it will land on our home page.
# In this scenario, if we go to localhost:8000, we will land on our home page.
urlpatterns = [
    path('', views.home, name='blog-home'),
    path('about/', views.about, name='blog-about')
]
