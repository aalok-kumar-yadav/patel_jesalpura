"""pdf_store URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url
from admin_webapp import views
from index.views import home, upload_file

urlpatterns = [

    url(r'^$', home, name="home"),
    url(r'^upload/', upload_file, name="upload"),
    url(r'^admin/', admin.site.urls),
    url(r'^admin_page/$', views.admin_view, name="admin_view"),
    url(r'^admin_page/view_resume/(?P<phone_number>[0-9]+)$', views.pdf_viewer, name="pdf_view"),
    url(r'^admin_page/blog/$', views.blog_view, name="blog_view"),
    url(r'^admin_page/candidate_details/(?P<phone_number>[0-9]+)$', views.candidate_details_view, name= "candidate_details_view"),
    url(r'^login/$', views.login_view, name="login_view"),
    url(r'^login/authentication/$', views.authentication, name="authentication_view"),
    url(r'^admin_page/logout', views.logout_view, name="logout_view"),
    url(r'^admin_page/blog/logout', views.logout_view, name="logout_view"),
    url(r'redirect_admin/', views.redirect_admin_view, name="redirect_admin"),
    url(r'^admin_page/blog/addPost/', views.addpost_view, name="addpost_view"),
    url(r'^blog_description/bloghome/', views.blogHome_view, name="blogHome_view"),
    url(r'^blog_description/(?P<blog_id>[0-9]+)$', views.blogDescription_view, name="blogDescription_view"),
    url(r'^admin_page/blog/deletepost/(?P<blog_id>[0-9]+)$', views.deletepost_view, name="deletepost_view"),
    url(r'^admin_page/blog/edit/(?P<blog_id>[0-9]+)$', views.edit_blog_details_view, name="edit_b(log_details_view"),
    url(r'^admin_page/blog/edit/update/(?P<blog_id>[0-9]+)$', views.update_blog_entry_view, name="update_blog_entry_view"),
    url(r'^admin_page/blog/edit/redirect_blog/', views.redirect_to_blog, name="redirect_to_blog"),
    url(r'^admin_page/candidate_details/redirect_to_blog/', views.redirect_to_blog, name="redirect_blog"),
    url(r'^admin_page/blog/change_blog_status/(?P<number>[0-9]+)$', views.blog_status, name="blog_status"),
    url(r'^admin_page/candidate_details/view_resume/(?P<phone_number>[0-9]+)$', views.pdf_viewer, name="pdf_view"),
    url(r'^blog_description/comment/(?P<blog_id>[0-9]+)$', views.add_comment, name = "add_comment"),

]
