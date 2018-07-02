from django.db import models


class Resume_class(models.Model):  # Resume class and their attribute
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=70, null=True)
    phone = models.IntegerField(default=200)
    whywehire_message = models.CharField(max_length=1000, blank=True)
    pdf_file = models.CharField(max_length=1000000)


class SessionClass(models.Model):  # Session class and their attribute
    admin_email = models.EmailField(max_length=70, null=False)
    admin_password = models.CharField(max_length=20)
    login_status = models.CharField(max_length=5)


class BlogPostClass(models.Model):  # BlogPost class and their attribute
    blogId = models.IntegerField()
    blogTitle = models.CharField(max_length=300)
    blogDescription = models.CharField(max_length=100000)
    blogPostDateTime = models.CharField(max_length=50)
    blogCoverImage = models.CharField(blank=True, max_length=1000000)
    blogImage = models.CharField(blank=True, max_length=1000000)

