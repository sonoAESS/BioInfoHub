from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import (
    UserCreationForm,
    AuthenticationForm,
)  # para usar formularios
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import (
    login,
    logout,
    authenticate,
)  # crea la cookie por nosotros
from .forms import TaskForm
from .models import Task
from django.utils import timezone
from django.contrib.auth.decorators import login_required


# Create your views here.
def home(request):
    return render(request, "home.html")


def signup(request):
    if request.method == "GET":
        return render(request, "signup.html", {"form": UserCreationForm})
    else:
        if request.POST["password1"] == request.POST["password2"]:
            try:
                # register user
                user = User.objects.create_user(
                    username=request.POST["username"],
                    password=request.POST["password1"],
                )
                user.save()
                # return HttpResponse("User created successfully")
                login(request, user)
                return redirect("tasks")
            except IntegrityError:
                errorMessage = "Username already exists"
        else:
            errorMessage = "Password do not match"
        return render(
            request,
            "signup.html",
            {"form": UserCreationForm, "error": errorMessage},
        )

@login_required
def tasks(request):
    tasks = Task.objects.filter(user=request.user, datecompleted__isnull=True)
    return render(request, "tasks.html", {"tasks": tasks})


def signout(request):
    logout(request)
    return redirect("home")


def signin(request):
    if request.method == "GET":
        return render(request, "signin.html", {"form": AuthenticationForm})
    else:
        user = authenticate(
            request,
            username=request.POST["username"],
            password=request.POST["password"],
        )
        if user is None:
            return render(
                request,
                "signin.html",
                {
                    "form": AuthenticationForm,
                    "error": "Username or password is invalid",
                },
            )
        else:
            login(request, user)
            return redirect("tasks")

@login_required
def createTask(request):
    if request.method == "GET":
        return render(request, "createTask.html", {"form": TaskForm})
    else:
        try:
            form = TaskForm(request.POST)
            newTask = form.save(commit=False)
            newTask.user = request.user
            newTask.save()
            return redirect("tasks")
        except ValueError:
            return render(
                request,
                "createTask.html",
                {"form": TaskForm, "error": "Please provide valid data"},
            )

@login_required
def taskDetail(request, taskId):
    if request.method == "GET": #obtener tarea
        task = get_object_or_404(
        Task, pk=taskId
        )  # respuesta sin que el servidor se caiga, necesita el modelo del que extrae datos y el id de la task
        form = TaskForm(instance=task)
        return render(request, "taskDetail.html", {"task": task, "form": form})
    else: #actualizar tarea
        try:
            task=get_object_or_404(Task, pk=taskId, user=request.user)
            form=TaskForm(request.POST, instance=task)
            form.save()
            return redirect('tasks')
        except ValueError:
            return render(request, "taskDetail.html", {"task": task, "form": form, 'error': "Error updating task"})

@login_required
def completeTask(request, taskId):
    task=get_object_or_404(Task, pk=taskId, user=request.user)
    if request.method=='POST':
        task.datecompleted=timezone.now()
        task.save()
        return redirect('tasks')

def deleteTask(request, taskId):
    task=get_object_or_404(Task, pk=taskId, user=request.user)
    if request.method=='POST':
        task.delete()
        return redirect('tasks')

@login_required
def tasksDone(request):
    tasks = Task.objects.filter(user=request.user, datecompleted__isnull=False).order_by('-datecompleted')
    return render(request, "completedTasks.html", {"tasks": tasks})

@login_required
def delete_completed_tasks(request):
    if request.method == "POST":
        Task.objects.filter(user=request.user, datecompleted__isnull=False).delete()
        return redirect('tasksDone')  # Redirige a la vista de tareas completadas