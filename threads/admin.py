from django.contrib import admin
from threads.models import Comment
from threads.models import Thread


@admin.register(Thread)
class ThreadModelAdmin(admin.ModelAdmin):
  list_display = ('id', 'name')


@admin.register(Comment)
class CommentModelAdmin(admin.ModelAdmin):
  list_display = ('id', 'parent', 'text')
