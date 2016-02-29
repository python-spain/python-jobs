from django.contrib import admin

from .models import Category, JobPost


admin.site.register(Category)
admin.site.register(JobPost)
