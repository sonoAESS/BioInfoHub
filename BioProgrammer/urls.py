"""
URL configuration for djangoCRUD project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import include, path
from tasks import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home, name="home"),
    path('logout/',views.signout, name='logout'),
    path('signin/',views.signin, name='signin'),
    path('signup/', views.signup, name="signup"),#ruta donde guardar usuarios
    
    path('tasks/', views.tasks, name="tasks"),
    path('tasks/completed/', views.tasksDone, name='tasksDone'),
    path('tasks/<int:taskId>/completeTask/',views.completeTask, name="completeTask"),
    path('tasks/<int:taskId>/deleteTask/',views.deleteTask, name="deleteTask"),
    path('tasks/createTask/',views.createTask, name="createTask"),
    path('tasks/<int:taskId>/',views.taskDetail, name="taskDetail"),
    path('tasks/delete-completed/', views.delete_completed_tasks, name='deleteCompletedTasks'),
    
    #path('alignment/',include('alignment.urls')),
    path('blog/',include('blog.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
