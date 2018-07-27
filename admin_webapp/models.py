from django.db import models


# Resume class and their attribute for Candidate Resume

class Resume_class(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=70, null=True)
    phone = models.BigIntegerField()
    whywehire_message = models.CharField(max_length=1000, blank=True)
    pdf_file = models.CharField(max_length=1000000)


# Session class and their attribute for creating a session for admin

class SessionClass(models.Model):
    admin_email = models.EmailField(max_length=70, null=False)
    admin_password = models.CharField(max_length=20)
    login_status = models.CharField(max_length=5)
    blog_status = models.CharField(max_length=5)


# BlogPost class and their attribute for Storing Posted Blog

class BlogPostClass(models.Model):
    blogId = models.IntegerField()
    blogTitle = models.CharField(max_length=300)
    blogDescription = models.CharField(max_length=100000)
    blogPostDateTime = models.CharField(max_length=50)
    blogCoverImage = models.CharField(blank=True, max_length=100000000)
    blogImage = models.CharField(blank=True, max_length=100000000)
