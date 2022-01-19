from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

# Create your views here.

def home_view(request, *args, **kwargs):
   #import pdb;pdb.set_trace()
   posts = Post.objects.filter(status="PUBLISHED")
   context_data = {
      "title": "Home page | posts",
      "posts": posts,
   }
   return render(request, "blog1/index.html", context_data)

