from django.contrib import admin
from .models import Category, Forum, Thread, Comment


admin.site.register(Category)
admin.site.register(Forum)
admin.site.register(Thread)
admin.site.register(Comment)