from django.contrib import admin

# Importing All model For Registration For Admin
from admin_webapp.models import Resume_class, SessionClass, BlogPostClass

admin.site.register(Resume_class)
admin.site.register(SessionClass)
admin.site.register(BlogPostClass)
