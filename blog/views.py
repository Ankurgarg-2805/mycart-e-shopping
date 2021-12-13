
from django.shortcuts import render
from .models import Blogpost
# Create your views here.
from django.http import HttpResponse

def index(request):
    myposts= Blogpost.objects.all()
    return render(request, 'blog/index.html', {'myposts': myposts})

def blogpost(request, id):

    myposts = Blogpost.objects.all()
    posts = Blogpost.objects.filter(post_id=id)[0]
    blogIndex = []
    nBlogs = len(myposts)
    for post in myposts:
        blogIndex.append(post.post_id)

    indexID = blogIndex.index(id)
    if indexID>0:
        p1 = blogIndex[indexID-1]
        post1 = Blogpost.objects.filter(post_id=p1)[0]
    else:
        post1 = 'NIL'

    if indexID<nBlogs-1:
        p2 = blogIndex[indexID + 1]
        post2 = Blogpost.objects.filter(post_id=p2)[0]
    else:
        post2 = 'NIL'

    print(post1, post2, indexID)
    return render(request, 'blog/blogpost.html', {'posts': posts, 'id':id, 'post1': post1, 'post2':post2, 'index': indexID, 'nBlogs': nBlogs})