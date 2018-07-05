from django.db import models


class CommentClass(models.Model):
    commentId = models.IntegerField(default=1)
    blogId = models.IntegerField(default=1)
    cName = models.CharField(max_length=50)
    cEmail = models.EmailField(max_length=100)
    comment = models.CharField(max_length=500)
    commentDate = models.CharField(max_length=30)