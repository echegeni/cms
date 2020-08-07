from django.shortcuts import render
from .models import post
# Create your views here.
def home (request):
    context = {
        "post": post.objects.all
    }
    return render(request, "blog/home.html", context)