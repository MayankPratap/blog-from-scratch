from django.shortcuts import render
from django.utils import timezone

from .models import Post 

# The dot before models means current directory 

# Create your views here.

def post_list(request):
	posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	# posts is a QuerySet object we pass it to our template
	return render(request,'blog/post_list.html',{'posts':posts})
