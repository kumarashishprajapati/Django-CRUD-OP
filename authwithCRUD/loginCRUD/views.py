from django.shortcuts import render,HttpResponse,redirect
from loginCRUD.models import students 
from django.contrib import messages
# Create your views here.
def home(request):
    show=students.objects.all()
    return render(request,'index.html',{"data":show})

def update(request):
    if request.method == 'POST':
        fname=request.POST.get('fname')
        lname=request.POST.get('lname')
        email=request.POST.get('email')
        course=request.POST.get('course')
        gender=request.POST.get('gender')
        address=request.POST.get('address')
        s=students()
        s.fname=fname
        s.lname=lname
        s.email=email
        s.course=course
        s.gender=gender
        s.address=address
        s.save()
        messages.success(request,"Student\n--"+fname+ "--\nAdded Successfully ...")
        return render(request,'post.html')
    else:
        return render(request,'post.html')
    

def edit(request,id):
    ed=students.objects.get(id=id)
    return render(request,"edit.html",{"students":ed})

def modify(request,id):
    if request.method == "POST":

        fname=request.POST.get('fname')
        lname=request.POST.get('lname')
        email=request.POST.get('email')
        course=request.POST.get('course')
        gender=request.POST.get('gender')
        address=request.POST.get('address')
        ed=students.objects.get(id=id)
        
        ed.fname=fname
        ed.lname=lname
        ed.email=email
        ed.course=course
        ed.gender=gender
        ed.address=address
        ed.save()
        return redirect("home")

def delet(request,id):
    de=students.objects.get(id=id)
    de.delete()
    messages.success(request,"Student delete successfully....")
    return redirect('home')


