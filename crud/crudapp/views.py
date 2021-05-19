from django.shortcuts import render,redirect, get_object_or_404, render
from django.utils import timezone

from .models import Blog


def main(request):
    blogs = Blog.objects.all()
    context= {
       'blogs' : blogs
    }
    return render(request,'main3.html',context)

def detail(request,id): 
    detail_data= get_object_or_404(Blog,pk=id)
    context= { 
        'title': detail_data.title,
        'writer': detail_data.writer,
        'body': detail_data.body,
        'pub_date': detail_data.pub_date,
        'applicant':detail_data.applicant,
        'id' : id

    }
    
    return render(request,'detail.html',context)

def create_page(request):
    return render(request,'create.html')

def create(request):
    new_data= Blog()
    new_data.title= request.POST['title']
    new_data.writer= request.POST['writer']
    new_data.body= request.POST['body']
    new_data.pub_date= timezone.now()
    new_data.applicant = 0
    new_data.save()
    return redirect('main')

def update_page(request,id):
    update_data= get_object_or_404(Blog,pk=id)
    context = {
        'id':id,
        'title': update_data.title,
        'writer': update_data.writer,
        'body': update_data.body,
     }
    return render(request, 'update.html',context)

def update (request,id):
    update_data= get_object_or_404(Blog,pk=id)
    update_data.title = request.POST['title']
    update_data.writer = request.POST['writer']
    update_data.body= request.POST['body']
    update_data.pub_date= timezone.now()
    update_data.save()
    return redirect('main')

def delete(request,id):
    delete_data =  get_object_or_404(Blog,pk=id)
    delete_data.delete()
    return redirect('main')

def increase(request, id):
    increase_data = get_object_or_404(Blog,pk=id)
    increase_data.applicant = increase_data.applicant + 1
    increase_data.save()
    return redirect('detail', id)

def decrease(request, id):
    decrease_data = get_object_or_404(Blog,pk=id)
    if(decrease_data.applicant>0):
        decrease_data.applicant = decrease_data.applicant - 1
    decrease_data.save()
    return redirect('detail', id)