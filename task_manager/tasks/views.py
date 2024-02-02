from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.models import auth
from django.contrib import messages
from django.utils import timezone
from django.db.models import Q
from django.views import generic

from rest_framework import viewsets

from .serializers import TaskSerializer
from .models import Task, Image

from datetime import datetime

class IndexView(generic.ListView):
    template_name = "tasks/index.html"
    context_object_name = "all_tasks"

    def get_queryset(self):
        return Task.objects.all().order_by('priority')

class DetailView(generic.DetailView):
    template_name = "tasks/details.html"
    model = Task


@login_required(
    login_url='tasks:signin'
)
def update(request, task_id):
    task = Task.objects.get(pk=task_id)
    images_for_the_task = Image.objects.filter(task=task)

    if request.user == task.user:

        if request.method == 'POST':
            title = request.POST.get('title')
            description = request.POST.get('description')
            due_date = request.POST.get('due_date')
            priority = request.POST.get('priority')
            images = request.FILES.getlist('images')
            is_completed = request.POST.get('is_complete')

            is_complete = True if is_completed == 'completed' else False

            # print(title)
            # print(description)
            # if due_date == '':
            #     print(False)
            # else:
            #     print(True)
            # print(priority)
            # print(is_complete)

            task.title = title
            task.description = description
            if due_date != '':
                task.due_date = due_date

            task.priority = priority
            task.is_complete = is_complete

            task.save()

            for image in images:
                image_for_the_updated_task = Image.objects.create(
                    task=task,
                    task_image=image,
                )
                image_for_the_updated_task.save()

            return redirect('tasks:details', task_id=task.id)
        else:
            context = {
                'task': task,
                'images': images_for_the_task
            }

            return render(request, "tasks/update.html", context)

    else:
        return redirect('task:details', task_id=task.id)
@login_required(
    login_url='tasks:signin'
)
def delete_image(request, image_id):
    image = Image.objects.get(pk=image_id)
    task = Task.objects.get(pk= image.task.id)
    if request.user == task.user:
        image.delete()
        return redirect('tasks:update', task_id=task.id)
    else:
        return redirect('tasks:details', task_id=task.id)

@login_required(
    login_url="tasks:signin"
)
def create(request):
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        images = request.FILES.getlist('images')
        is_completed = request.POST.get('is_complete')
        priority = request.POST.get('priority', 3)
        due_date = request.POST.get('due_date')

        is_complete = True if is_completed == 'completed' else False

        # print(title)
        # print(description)
        # # print(images)
        # print(is_complete)
        # print(priority)
        # print(due_date)

        #create task
        if due_date != '':
            new_task = Task.objects.create(
                user=request.user,
                title=title,
                description=description,
                is_complete=is_complete,
                priority=priority,
                created_at=timezone.now(),
                due_date=due_date
            )
            new_task.save()
        else:
            new_task = Task.objects.create(
                user=request.user,
                title=title,
                description=description,
                is_complete=is_complete,
                priority=priority,
                created_at=timezone.now()
            )
            new_task.save()

        #save the images for the task
        for image in images:
            image_for_the_new_task = Image.objects.create(
                task=new_task,
                task_image=image
            )

            image_for_the_new_task.save()

        return redirect('tasks:index')

    return render(request, 'tasks/create.html')

@login_required(
    login_url='tasks:signin'
)
def delete(request,task_id):
    task = Task.objects.get(pk=task_id)
    if task.user == request.user:
        task.delete()
        return redirect('tasks:index')

    else:
        return redirect('tasks:details',task_id=task_id)

@login_required(
    login_url="tasks:signin"
)
def search(request):
    if request.method == 'POST':
        search_string = request.POST.get('title')
        if search_string != '':
            tasks = Task.objects.filter(title__icontains=search_string)
        else:
            tasks = None

        context = {
            'tasks': tasks
        }

        return render(request, "tasks/search.html", context)

    else:
        return render(request, 'tasks/search.html')

@login_required(
    login_url='tasks:signin'
)
def filter(request):
    if request.method == 'POST':
        creation_date = request.POST.get('creation_date')
        due_date = request.POST.get('due_date')
        priority = request.POST.get('priority')
        is_completed = request.POST.get('is_complete')

        filtered_tasks = Task.objects.all()

        if creation_date != '':
            creation_date = datetime.strptime(creation_date, '%Y-%m-%d')
            filtered_tasks = filtered_tasks.filter(
                Q(created_at__day=creation_date.day) &
                Q(created_at__month=creation_date.month) &
                Q(created_at__year=creation_date.year)
            )
        if due_date != '':
            due_date = datetime.strptime(due_date, '%Y-%m-%d')
            filtered_tasks = filtered_tasks.filter(
                Q(due_date__day=due_date.day) &
                Q(due_date__month=due_date.month) &
                Q(due_date__year=due_date.year)
            )
        if priority is not None:
            filtered_tasks = filtered_tasks.filter(priority=priority)
        if is_completed is not None:
            filtered_tasks = filtered_tasks.filter(is_complete=True)

        context = {
            "tasks": filtered_tasks
        }


        return render(request, 'tasks/search.html', context)

    else:
        return redirect('tasks:search')



def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('tasks:index')
        else:
            messages.info(request,"Invalid username or password")
            return redirect('tasks:signin')

    else:
        return render(request, 'tasks/signin.html')


@login_required(
    login_url='tasks:signin',
)
def logout(request):
    auth.logout(request)
    return redirect('tasks:signin')

