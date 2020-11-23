from django.contrib import admin

from . import models

admin.site.register(models.Article)
admin.site.register(models.Reporter)

#作业#
admin.site.register(models.Student)