# Import Necessary Library

import base64, time, datetime
from django.shortcuts import render
from admin_webapp.models import Resume_class, SessionClass, BlogPostClass
from django.shortcuts import redirect
from django.http import HttpResponse

auth_error = "True"  # Global Variable For Authentication Error Status


# Django View For Admin Panel

def admin_view(request):

    database_object = Resume_class.objects.all()        # Creating Resume Class Instance
    session_obj = SessionClass.objects.get()    # Getting Session Data

    if session_obj.login_status == "True":
        return render(request, 'home.html', {'aspirant_list': database_object})           # Rendering Admin Page
    else:
        return redirect('login_view')       # Rendering Log In Page Due To Session Expired

# Django View For Viewing PDF File


def pdf_viewer(request, phone_number):

    db_object = Resume_class.objects.all()          # Creating Resume Class Instance
    base64_value = ""

    for i in db_object:
        if i.phone == int(phone_number):
            base64_value = i.pdf_file

    final_val = "data:application/pdf;base64," + base64_value       # Final Value Variable To Be Send

    return render(request, 'view.html', {'base64_value': final_val})        # Rendering PDF View Page

# Django View For Blog Page


def blog_view(request):
    blog_database_object = BlogPostClass.objects.all()             # Creating BlogPostClass Instance

    session_obj = SessionClass.objects.get(admin_email="alokyadav@cosaia.com")      # Fetching Session Data
    # Making A Variable For Rendering

    context = {'blog_list': blog_database_object, 'blog_status': session_obj.blog_status}

    return render(request, 'blog.html', {'context': context})       # Rendering Blog Page


# Django View For Candidate Details


def candidate_details_view(request, phone_number):
    database_object = Resume_class.objects.filter(phone=phone_number)       # Getting Specified DB object

    return render(request, 'can_details.html', {'content': database_object[0]})    # Rendering Candidate Details Page


# Django View For Log In Page


def login_view(request):

    global auth_error

    if auth_error == "False":       # Condition For Current Error Status
        temp_err_var = "False"
    else:
        temp_err_var = "True"

    auth_error = "True"
    return render(request, 'login.html', {'context': temp_err_var})         # Rendering Log In Page

# Django View For Authentication


def authentication(request):

    if request.method == 'POST':        # Condition For Checking Request Is Post Or Get
        temp_email = request.POST.get("adminEmail")
        temp_password = request.POST.get("adminPassword")

        status_flag = ""
        # Try And Catch Block For Throwing Exception

        try:
            session_obj = SessionClass.objects.get(admin_email=temp_email, admin_password=temp_password)
            status_flag = "True"
        except SessionClass.DoesNotExist:
            status_flag = "False"

        if status_flag == "False":      # Checking Blog Status Is False Or NOt
            global auth_error
            auth_error = "False"
            return redirect('login_view')

        else:

            if session_obj.login_status == "False":
                # Updating Session DB Data

                SessionClass.objects.filter(admin_email=temp_email).update(login_status="True")
                return redirect('admin_view')       # Rendering Admin Page

            else:
                return redirect('admin_view')       # Rendering Admin Page


# Django View For Log Out Functionality


def logout_view(request):
    SessionClass.objects.filter(admin_email="alokyadav@cosaia.com").update(login_status="False")
    return redirect('home')

# Django View For Redirecting Admin's Home Page


def redirect_admin_view(request):
    return redirect('admin_view')

# Django View For Redirecting Client's Home Page


def redirect_home_view(request):
    return redirect('home')


# Django View For Adding New Post

def add_post_view(request):

    post_object = BlogPostClass()               # Creating Required DB Instance
    total_row = BlogPostClass.objects.all().count()
    if total_row == 0:
        post_object.blogId = 1
    else:
        post_object.blogId=BlogPostClass.objects.all().order_by("-id")[0].blogId+1

    post_object.blogTitle = request.POST.get("blogTitle")       # Assigning Value Into Variable

    post_object.blogDescription = request.POST.get("blogDescription")

    post_object.blogPostDateTime = datetime.datetime.fromtimestamp(time.time()).strftime('%H:%M:%S %d-%m-%Y')

    img = request.FILES['blogImage']
    var = base64.b64encode(img.read())      # Convert Image Into Base64
    post_object.blogImage = var.decode("utf-8")

    img1 = request.FILES['coverImage']
    var1 = base64.b64encode(img1.read())      # Convert Image Into Base64
    post_object.blogCoverImage = var1.decode("utf-8")

    post_object.save()      # Saving New Row Into Database

    return redirect('blog_view')        # Rendering To Blog Page


# Django View For Delete Post


def delete_post_view(request, blog_id):
    BlogPostClass.objects.filter(blogId=blog_id).delete()

    return redirect('blog_view')        # Redirecting To Admin's Blog Page


# Django View For Client's All Blog Contained Home Page


def blog_home_view(request):
    blogpost_obj = BlogPostClass.objects.all()              # Creating Required DB Instance
    return render(request, 'blogHome.html', {'blog_list': blogpost_obj})       # Rendering Home Page Of Blog


# Django View For Blog Description Page


def blog_description_view(request, blog_id):

    blog_obj = BlogPostClass.objects.get(blogId=blog_id)        # Creating Required DB Instance
    print(blog_obj.blogCoverImage)
    return render(request, 'blogDescription.html', {'context': blog_obj})        # Rendering Home Page Of Blog

# Django View For Edit Blog Details


def edit_blog_details_view(request, blog_id):

    blog_obj = BlogPostClass.objects.get(blogId=blog_id)        # Fetching Row Of that Blog Id
    blg_image = "data:image/png;base64," + blog_obj.blogImage
    cv_image = "data:image/png;base64," + blog_obj.blogCoverImage

    context = {'blogId': blog_id, 'blogTitle': blog_obj.blogTitle, 'blogDescription':  # Data To Be Send
        blog_obj.blogDescription, 'blogImage': blg_image, 'coverImage': cv_image}

    return render(request, 'edit_blog.html', {'context': context})          # Rendering Edit Blog Page

# Django View For Update Blog Entry


def update_blog_entry_view(request, blog_id):

    blog_obj = BlogPostClass.objects.get(blogId=blog_id)        # Fetching Row Of that Blog Id

    new_title = request.POST.get("blogTitle_edit")          # Assignment Of Data
    new_description = request.POST.get("blogDescription_edit")
    new_datetime = datetime.datetime.fromtimestamp(time.time()).strftime('%H:%M:%S %d-%m-%Y')

    blg_image = blog_obj.blogImage
    cv_image = blog_obj.blogCoverImage

    if len(request.FILES) != 0:         # Condition For Checking Image Files Are Blank Or Not
        img = request.FILES['blogImage_edit']
        var = base64.b64encode(img.read())          # Image To Base64 Conversion
        blg_image = var.decode("utf-8")

        img1 = request.FILES['coverImage_edit']
        var1 = base64.b64encode(img1.read())        # Image To Base64 Conversion
        cv_image = var1.decode("utf-8")

    temp_obj = BlogPostClass.objects.get(blogId=blog_id)
    temp_obj.blogTitle = new_title
    temp_obj.blogPostDateTime = new_datetime
    temp_obj.blogDescription = new_description
    temp_obj.blogImage = blg_image
    temp_obj.blogCoverImage = cv_image

    temp_obj.save()         # Saving Into Database
    return redirect('blog_view')        # Redirecting Admin Blog Page

# Django View For Redirecting To Blog Page


def redirect_to_blog(request):
    return redirect('blog_view')

# Django View For Checking Blog Status


def blog_status(request, number):
    if number == "0":
        SessionClass.objects.filter(admin_email="alokyadav@cosaia.com").update(blog_status="False")
    else:
        SessionClass.objects.filter(admin_email="alokyadav@cosaia.com").update(blog_status="True")

    return redirect('blog_view')

# Django View For Getting Blog Description -- Only Limited To Ajax Request Not For Rendering


def get_blog_description(request, blog_id):
    blog_obj = BlogPostClass.objects.get(blogId=blog_id)
    return HttpResponse(blog_obj.blogDescription)
