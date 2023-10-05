"""TaskTracker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path
from tasks import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index),
    path('loginForm/',views.loginForm),
    path('signIn/',views.signIn),
    path('adminHome/',views.adminHome),
    path('userHome/',views.userHome),
    path('addTaskForm/',views.addTaskForm),
    path('addTask1/',views.addTask1),
    path('viewTask/',views.viewTask),
    path('updateTask1/',views.updateTask1),
    path('updateTask2/<int:id>',views.updateTask2),
    path('addTask1/<int:id>',views.addTask1),
    path('delTask/<int:id>',views.delTask),
    path('tasks/',views.tasks),
    path('addUserForm/',views.addUserForm),
    path('addUser1/',views.addUser1),
    path('viewUsers/',views.viewUsers),
    path('delUser/<int:id>',views.delUser),
    path('viewUserUpdt/',views.viewUserUpdt),
    path('viewUserUpdt1/<int:id>',views.viewUserUpdt1),

    



    
]
