from django.shortcuts import render,redirect
from tasks.models import Task
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.http import HttpResponse
def index(request):
    return render(request,'index.html')
# Create your views here.
def loginForm(request):
    return render(request,'login.html')
def adminHome(request):
    return render(request,'adminHome.html')
def userHome(request):
    return render(request,'userHome.html')    
def signIn(request):
    username=request.POST.get('uname')
    password=request.POST.get('psd')
    data=authenticate(username=username,password=password)
    request.session['username']=username
    if data is not None and data.is_superuser==1:
        return redirect('/adminHome/')
    elif data is not None and data.is_superuser==0:
        return redirect('/userHome/')
    else:
        return HttpResponse('Invalid user')
def addTaskForm(request):
    return render(request,'taskForm.html') 
def addTask1(request):
        id=request.POST.get('id')
        try:
            t=Task.objects.get(id=id)
            t.title=request.POST.get('title') 
            t.description=request.POST.get('dec')
            sts=request.POST.get('sts')
            if sts == "True":
                    t.completed=True
            elif sts == "False":
                t.completed=False
            else:
                pass
            t.save()
        except:

            t=Task()
            t.title=request.POST.get('title') 
            t.description=request.POST.get('dec')
            sts=request.POST.get('sts')
            if sts == "True":
                    t.completed=True
            elif sts == "False":
                t.completed=False
            else:
                pass
            t.save()
        return redirect('/adminHome/')         
    
def viewTask(request):
    content=request.POST.get('search')
    data=[]
    if content=="True":
        data=Task.objects.filter(completed=1)
        return render(request,'viewTask.html',{'taskData':data})
    elif content=="False":
        data=Task.objects.filter(completed=0)
        return render(request,'viewTask.html',{'taskData':data})
    else:
        tasks=Task.objects.all()
        return render(request,'viewTask.html',{'taskData':tasks})
   
    return render(request,'viewTask.html',{'taskData':data})

def updateTask1(request):
    tasks=Task.objects.all()
    return render(request,'updateTask.html',{'taskData':tasks})
def updateTask2(request,id):
    tasks=Task.objects.get(id=id)
    return render(request,'updateTaskForm.html',{'x':tasks})
def delTask(request,id):
    tasks=Task.objects.get(id=id)
    tasks.delete()
    return redirect('/adminHome/')
def tasks(request):
    content=request.POST.get('search')
    
    if content=="True":
        data=Task.objects.filter(completed=1)
        return render(request,'tasks.html',{'taskData':data})
    elif content=="False":
        data=Task.objects.filter(completed=0)
        return render(request,'tasks.html',{'taskData':data})
    else:
        tasks=Task.objects.all()
        return render(request,'tasks.html',{'taskData':tasks})
def addUserForm(request):
    return render(request,'userForm.html') 
def addUser1(request):
    id=request.POST.get('id')
    print('test1')
    try:
         print('test2')
         u=User.objects.get(id=id)
         pswd1=request.POST.get('psd')
         u.set_password(pswd1)
         u.save()
    except: 
        print('test2')      
        u=User()
        u.email=request.POST.get('email')
        u.first_name=request.POST.get('fname')
        u.last_name=request.POST.get('lname')
        u.username=request.POST.get('email')
        pswd1=request.POST.get('psd')
        u.set_password(pswd1)
        u.save()
    return redirect('/adminHome/')
def viewUsers(request): 
    data=User.objects.filter(is_superuser=0)
    return render(request,'viewUsers.html',{'datas':data})
def delUser(request,id): 
    data=User.objects.get(id=id)
    data.delete()
    return redirect('/viewUsers/')
def viewUserUpdt(request): 
    data=User.objects.filter(is_superuser=0)
    return render(request,'updateUser1.html',{'datas':data})
def viewUserUpdt1(request,id):
    data=User.objects.get(is_superuser=0,id=id)
    print(data,"test1")
    return render(request,'updateUser2.html',{'x':data})