from django.contrib import admin

from admin_webapp.models import Resume_class, SessionClass, BlogPostClass
from index.models import CommentClass

admin.site.register(Resume_class)
admin.site.register(SessionClass)
admin.site.register(BlogPostClass)
admin.site.register(CommentClass)