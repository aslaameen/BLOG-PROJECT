from django.contrib.auth import logout
from django.shortcuts import render, redirect

from BLOGING_APP.models import BlogPost, Blogger


def blogers_list(request):
    data = Blogger.objects.all()
    return render(request,"admin/blogers_list.html",{"data":data})
# ----------------------------------------------------------------------


def blogposts_lists(request):
    data=BlogPost.objects.all()
    return render(request, "admin/blogposts_lists.html", {"data":data})

def blogers_delete(request,id):
    data =Blogger.objects.get(id=id)
    data.delete()
    return redirect('blogers_list')



def Log_out(request):
    logout(request)
    return redirect('index')