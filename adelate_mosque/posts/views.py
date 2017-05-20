from django.shortcuts import render
from .models import Posts
# Create your views here.
def home(request):

    posts =  Posts.objects.order_by('-pub_date')

    return render(request, 'posts/home.html', {'posts':posts})