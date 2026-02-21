
from django.urls import path

from BLOGING_APP import views, blogviews, adminviews

urlpatterns = [
    path("",views.index,name="index"),
    path("dash",views.dash,name="dash"),

    path("admin",views.admin,name="admin"),
    path("blogger",views.blogger,name="blogger"),
    path("login_view",views.login_view,name="login_view"),
    path("blogger_add",views.blogger_add,name="blogger_add"),
    path("my_profile",views.my_profile,name="my_profile"),
    path("blog_edit",blogviews.blog_edit,name="blog_edit"),
    path("blogpost_add",blogviews.blogpost_add,name="blogpost_add"),
    path("blogpost_list",blogviews.blogpost_list,name="blogpost_list"),
    path("blogpost_update/<int:id>/", blogviews.blogpost_update, name="blogpost_update"),
    path("blogpost_delete/<int:id>/", blogviews.blogpost_delete, name="blogpost_delete"),
    path("blogpost_lists",blogviews.blogpost_lists,name="blogpost_lists"),
    path("blogposts_lists",adminviews.blogposts_lists,name="blogposts_lists"),
    path("blogers_list",adminviews.blogers_list,name="blogers_list"),
path("blogers_delete/<int:id>/", adminviews.blogers_delete, name="blogers_delete"),
]