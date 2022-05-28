from django.db import models


class Thread(models.Model):
  name = models.TextField()
  description = models.TextField()
  likes = models.PositiveIntegerField(default=0)


class Comment(models.Model):
  text = models.TextField()

  post_parent = models.ForeignKey(
    Thread,
    on_delete=models.CASCADE,
    related_name='top_level_comments',
    null=True,
    blank=True)

  comment_parent = models.ForeignKey(
    'threads.Comment',
    on_delete=models.CASCADE,
    related_name='nested_comments',
    null=True,
    blank=True)

  likes = models.PositiveIntegerField(default=0)

  @property
  def parent(self):
    return self.post_parent or self.comment_parent
