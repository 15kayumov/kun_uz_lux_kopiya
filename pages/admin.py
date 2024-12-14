from django.contrib import admin

# Register your models here.
from .models import Post,Mir,Obshestvo
admin.site.register(Post)
admin.site.register(Obshestvo)
admin.site.register(Mir)
