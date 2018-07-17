import base64, time, datetime
from django.shortcuts import render
from admin_webapp.models import Resume_class, SessionClass, BlogPostClass
from index.models import CommentClass
from django.shortcuts import redirect

auth_error = "True"


def admin_view(request):
    aspirant_list = []
    database_object = Resume_class.objects.all()
    for i in database_object:
        resume_obj = Resume_class()
        resume_obj.name = i.name
        resume_obj.phone = i.phone
        resume_obj.email = i.email
        temp = i.whywehire_message
        resume_obj.whywehire_message = temp[:100]

        resume_obj.pdf_file = i.pdf_file

        aspirant_list.append(resume_obj)

    session_obj = SessionClass.objects.get()
    if session_obj.login_status == "True":
        return render(request, 'home.html', {'aspirant_list': aspirant_list})
    else:
        return redirect('login_view')


def pdf_viewer(request, phone_number):

    db_object = Resume_class.objects.all()
    base64_value = ""
    for i in db_object:
        if i.phone == int(phone_number):
            base64_value = i.pdf_file

    final_val = "data:application/pdf;base64," + base64_value
    return render(request, 'view.html', {'base64_value': final_val})


def blog_view(request):
    blog_list = []
    blog_database_object = BlogPostClass.objects.all()

    session_obj = SessionClass.objects.get(admin_email="alokyadav@cosaia.com")

    for blog_temp_obj in blog_database_object:

        blog_obj = BlogPostClass()
        blog_obj.blogId = blog_temp_obj.blogId

        blog_obj.blogTitle = blog_temp_obj.blogTitle
        blog_obj.blogDescription = blog_temp_obj.blogDescription[:110]+"..........."
        blog_obj.blogPostDateTime = blog_temp_obj.blogPostDateTime
        blog_obj.blogImage = blog_temp_obj.blogDescription
        blog_obj.blogCoverImage = blog_obj.blogCoverImage
        blog_list.append(blog_obj)

    context = {'blog_list': blog_list, 'blog_status': session_obj.blog_status }

    return render(request, 'blog.html', {'context': context})


def candidate_details_view(request, phone_number):
    database_object = Resume_class.objects.filter(phone=phone_number)
    for i in database_object:
        if phone_number == i.phone:
                break

    content = {'name': i.name, 'phone': phone_number, 'email': i.email, 'pdf_file': i.pdf_file, 'whywehire_message': i.whywehire_message}

    return render(request, 'can_details.html', {'content': content})


def login_view(request):
    temp_err_var = ""
    global auth_error
    if auth_error == "False":
        temp_err_var = "False"
    else:
        temp_err_var = "True"
    print (temp_err_var)
    print("\n")
    auth_error = "True"
    return render(request, 'login.html', {'context': temp_err_var})


def authentication(request):
    if request.method == 'POST':
        temp_email = request.POST.get("adminEmail")
        temp_password = request.POST.get("adminPassword")

        status_flag = ""
        try:
            session_obj = SessionClass.objects.get(admin_email=temp_email, admin_password=temp_password)
            status_flag = "True"
        except SessionClass.DoesNotExist:
            status_flag = "False"

        if status_flag == "False":
            global auth_error
            auth_error = "False"
            return redirect('login_view')

        else:

            if session_obj.login_status == "False":

                SessionClass.objects.filter(admin_email=temp_email).update(login_status="True")
                return redirect('admin_view')

            else:
                return redirect('admin_view')


def logout_view(request):
    SessionClass.objects.filter(admin_email="alokyadav@cosaia.com").update(login_status="False")
    return redirect('home')


def redirect_admin_view(request):

    return redirect('admin_view')


def redirect_home_view(request):

    return redirect('home')


def addpost_view(request):

    post_object = BlogPostClass()
    total_row = BlogPostClass.objects.all().count()

    post_object.blogId = total_row+1
    post_object.blogTitle = request.POST.get("blogTitle")

    post_object.blogDescription = request.POST.get("blogDescription")

    post_object.blogPostDateTime = datetime.datetime.fromtimestamp(time.time()).strftime(' %H:%M:%S %d-%m-%Y')

    img = request.FILES['blogImage']
    var = base64.b64encode(img.read())
    post_object.blogImage = var.decode("utf-8")

    img1 = request.FILES['coverImage']
    var1 = base64.b64encode(img1.read())
    post_object.blogCoverImage = var1.decode("utf-8")

    post_object.save()

    return redirect('blog_view')


def deletepost_view(request, blog_id):

    BlogPostClass.objects.filter(blogId=blog_id).delete()

    return redirect('blog_view')


def blogHome_view(request):

    blogpost_obj = BlogPostClass.objects.all()

    blog_list = []

    for obj in blogpost_obj:
        temp_obj = BlogPostClass()
        temp_obj.blogId = obj.blogId
        temp_obj.blogTitle = obj.blogTitle
        temp = obj.blogDescription
        temp_obj.blogDescription = temp[:77]
        temp_obj.blogImage = "data:image/png;base64," + obj.blogImage
        blog_list.append(temp_obj)

    return render(request, 'blogHome.html', {'blog_list': blog_list})


def blogDescription_view(request, blog_id):

    blog_obj = BlogPostClass.objects.get(blogId=blog_id)
    comment_db_obj = CommentClass.objects.all()
    blg_image = "data:image/png;base64," + blog_obj.blogImage
    cv_image = "data:image/png;base64," + blog_obj.blogCoverImage
    comment_list = []

    for c_obj in comment_db_obj:
        if c_obj.blogId == int(blog_id):
            comment_class_obj = CommentClass()
            comment_class_obj.commentId = c_obj.commentId
            comment_class_obj.blogId = c_obj.blogId
            comment_class_obj.comment = c_obj.comment
            comment_class_obj.cEmail = c_obj.cEmail
            comment_class_obj.cName = c_obj.cName
            comment_class_obj.commentDate = c_obj.commentDate
            comment_list.append(comment_class_obj)


    context = {'blogId': blog_id, 'blogTitle': blog_obj.blogTitle, 'blogDescription':
        blog_obj.blogDescription, 'blogImage': blg_image, 'coverImage': cv_image, 'blogPostDateTime': blog_obj.blogPostDateTime,
               'comment_list': comment_list}
    return render(request, 'blogDescription.html', {'context': context})


def edit_blog_details_view(request, blog_id):

    blog_obj = BlogPostClass.objects.get(blogId=blog_id)
    blg_image = "data:image/png;base64," + blog_obj.blogImage
    cv_image = "data:image/png;base64," + blog_obj.blogCoverImage

    context = {'blogId': blog_id, 'blogTitle': blog_obj.blogTitle, 'blogDescription':
     blog_obj.blogDescription, 'blogImage': blg_image, 'coverImage': cv_image}

    return render(request, 'edit_blog.html', {'context': context})


def update_blog_entry_view(request, blog_id):

    blog_obj = BlogPostClass.objects.get(blogId=blog_id)
    new_title = request.POST.get("blogTitle_edit")
    new_description = request.POST.get("blogDescription_edit")
    new_datetime = datetime.datetime.fromtimestamp(time.time()).strftime(' %H:%M:%S %d-%m-%Y')

    blg_image = blog_obj.blogImage
    cv_image = blog_obj.blogCoverImage

    if len(request.FILES) != 0:
        img = request.FILES['blogImage_edit']
        var = base64.b64encode(img.read())
        blg_image = var.decode("utf-8")

        img1 = request.FILES['coverImage_edit']
        var1 = base64.b64encode(img1.read())
        cv_image = var1.decode("utf-8")

    temp_obj = BlogPostClass.objects.get(blogId=blog_id)
    temp_obj.blogTitle = new_title
    temp_obj.blogPostDateTime = new_datetime
    temp_obj.blogDescription = new_description
    temp_obj.blogImage = blg_image
    temp_obj.blogCoverImage = cv_image

    temp_obj.save()
    return redirect('blog_view')


def redirect_to_blog(request):

    return redirect('blog_view')


def blog_status(request, number):

    if number == "0":
        SessionClass.objects.filter(admin_email="alokyadav@cosaia.com").update(blog_status="False")
    else:
        SessionClass.objects.filter(admin_email="alokyadav@cosaia.com").update(blog_status="True")

    return redirect('blog_view')


def add_comment(request, blog_id):
    total_row = BlogPostClass.objects.all().count()
    if request.method == 'POST':
        comment_obj = CommentClass()
        comment_obj.commentId = total_row + 1
        comment_obj.blogId = blog_id
        comment_obj.cName = request.POST.get("cName")
        comment_obj.cEmail = request.POST.get("cEmail")
        comment_obj.comment = request.POST.get("comment")
        comment_obj.commentDate = datetime.datetime.fromtimestamp(time.time()).strftime('%d-%m-%Y')
        comment_obj.save()

        return redirect('blogDescription_view', blog_id)

