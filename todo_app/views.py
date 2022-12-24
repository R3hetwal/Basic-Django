from django.shortcuts import render, HttpResponseRedirect
from todo_app.models import Todo


# CRUD
# C => CREATE
# R => READ / RETRIEVE
# u => UPDATE
# D => DELETE

# Create your views here.
def todo_list(request):
    todos = Todo.objects.all()
    return render(
        request = request,
        template_name = "bootstrap/todo_list.html",
        context = {"todos": todos},
    )

# To make the button work
def todo_create(request):
    if request.method == "POST":
        title = request.POST['title']
        # ORM => Object Relational Mapping
        Todo.objects.create(title=title)
        return HttpResponseRedirect("/")
    return render(request, "bootstrap/todo_create.html")

def todo_delete(request, pk):
    todo = Todo.objects.get(id=pk) # pk is primary key (id)
    todo.delete()
    return HttpResponseRedirect("/")

def todo_update(request, pk):
    todo = Todo.objects.get(id = pk)
    if request.method == "POST":
        title = request.POST["title"]
        todo = Todo.objects.get(id = pk)
        todo.title = title
        todo.save()
        return HttpResponseRedirect("/")
    
    return render(
                    request, 
                    "bootstrap/todo_update.html",
                    {"todo": todo},
                )