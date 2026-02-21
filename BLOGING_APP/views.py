from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

from BLOGING_APP.forms import BloggerRegister, LoginRegister
from BLOGING_APP.models import Login, Blogger


# Create your views here.

def index(request):
    return render(request, "index.html")

def dash(request):
    return render(request, "dash.html")



def admin(request):
    return render(request, "admin/admin_base.html")

def blogger(request):
    return render(request, "blogger/blogger_base.html")
# --------------------------------------------------------------------------------

def login_view(request):
    if request.method == "POST":
         username = request.POST.get('uname')
         password = request.POST.get('pass')

         user = authenticate(request, username=username, password=password)
         # authenticate= inbuild function aan
         if user is not None:
            login(request,user)
            if user.is_staff:
                return redirect ('admin')
            elif user.is_blogger:
                return redirect('blogger')
         else:
             messages.info(request, 'Username or password is incorrect')
    return render(request, 'login.html')
# ---------------------------------------------------------------------------------------------




def blogger_add(request):

    if request.method == "POST":
        blog_form = BloggerRegister(request.POST,request.FILES,request.FILES)
        login_form = LoginRegister(request.POST)



        if blog_form.is_valid() and login_form.is_valid():
            blog=login_form.save(commit=False)
            blog.is_blogger=True
            blog.save()

            user = blog_form.save(commit=False)
            user.blogger_details = blog
            user.save()

    else:
        blog_form=BloggerRegister()
        login_form = LoginRegister()
    return render(request,'register_1.html',{'blog_form':blog_form,'login_form':login_form})


# ------------------------------------------------------------------------------------------
def my_profile(request):
    data = request.user
    # print(data.id)
    my_profile = Blogger.objects.get(blogger_details=data.id)
    # print(passenger_profile.phone)
    return render(request,"blogger/my_profile.html",{"data":my_profile})
# ----------------------------------------------------------------------

