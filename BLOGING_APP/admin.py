from django.contrib import admin
from django.contrib.auth.models import User

from BLOGING_APP.models import Blogger, BlogPost

# Register your models here.
admin.site.register(User)
admin.site.register(Blogger)
admin.site.register(BlogPost)
