# Import Library

import base64, datetime, time
from django.shortcuts import render
from admin_webapp.models import Resume_class, SessionClass, BlogPostClass
from django.shortcuts import redirect
from django.core.mail import EmailMessage


# Django View For Client Side Home Page

def home(request):
    blog_post_obj = BlogPostClass.objects.all()                     # Creating BlogPostClass Instance
    session_obj = SessionClass.objects.get(admin_email="alokyadav@cosaia.com")          # Fetching Session Data
    blog_list = []  # Temporary List
    date_list = []

    for object_bl in blog_post_obj:  # Loop For Appending Fetched DB Rows Into List
        date_list.append(object_bl.blogPostDateTime)

    # Calling Method For Custom Sorting
    sorted_datetime_list = sorted(date_list, key=lambda x: datetime.datetime.strptime(x, '%H:%M:%S %d-%m-%Y'))
    count = 1
    length_list = len(sorted_datetime_list)                         # Storing Length Of Sorted Blog List

    while count <= 6 and count <= length_list:                       # While Loop For Getting Only Top Six Latest Blog
        for obj in blog_post_obj:

            if sorted_datetime_list[-count] == obj.blogPostDateTime:
                temp_obj = BlogPostClass()                          # Assigning Value To BlogPostClass Instance
                temp_obj.blogId = obj.blogId
                temp_obj.blogTitle = obj.blogTitle
                temp = obj.blogDescription

                temp_obj.blogDescription = temp[:88] + "...."
                temp_obj.blogImage = "data:image/png;base64," + obj.blogImage       # Appending Some Base64 Encoding
                blog_list.append(temp_obj)
        count = count + 1

    context = {'blog_list': blog_list,
               'blog_status': session_obj.blog_status}                  # Send In A Proper Format In Single Variable

    return render(request, 'index.html', {'context': context})          # Rendering Home Page With Data


# Django View For Uploading Resume

def upload_file(request):
    res_object = Resume_class()                 # Making Resume Class Instance

    if request.method == 'POST' and request.FILES['myfile']:            # Checking Request Method Is Post Or Not
        myfile = request.FILES['myfile']

        var = base64.b64encode(myfile.read())                           # Converting PDF To Base64
        res_object.name = request.POST.get("fname")
        res_object.pdf_file = var.decode("utf-8")
        res_object.email = request.POST.get("email")
        res_object.phone = request.POST.get("phone")
        res_object.whywehire_message = request.POST.get("whywe")
        
        res_object.save()                                               # Saving data Into Database

        return redirect('home')                 # Redirecting Home Page
    return render(request, 'index.html')                                # Rendering Index Page
