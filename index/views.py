import base64
from django.shortcuts import render
from admin_webapp.models import Resume_class, SessionClass, BlogPostClass
from django.shortcuts import redirect



def home(request):
    blogpost_obj = BlogPostClass.objects.all()
    session_obj = SessionClass.objects.get(admin_email="alokyadav@cosaia.com")
    blog_list = []

    count =0
    for obj in blogpost_obj:
        if count == 6:
            break

        temp_obj = BlogPostClass()
        temp_obj.blogId = obj.blogId
        temp_obj.blogTitle = obj.blogTitle
        temp = obj.blogDescription


        temp_obj.blogDescription = temp[:88] +"...."
        temp_obj.blogImage = "data:image/png;base64," + obj.blogImage
        blog_list.append(temp_obj)
        count = count+1

    context = {'blog_list': blog_list, 'blog_status': session_obj.blog_status}

    return render(request, 'index.html', {'context': context})


def upload_file(request):
    res_object = Resume_class()

    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']

        var = base64.b64encode(myfile.read())
        res_object.name = request.POST.get("fname")
        res_object.pdf_file = var.decode("utf-8")
        res_object.email = request.POST.get("email")
        res_object.phone = request.POST.get("phone")
        res_object.whywehire_message = request.POST.get("whywe")
        res_object.save()

        return redirect('home')
    return render(request, 'index.html')







