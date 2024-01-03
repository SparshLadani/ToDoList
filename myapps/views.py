from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, request
from .models import TheToDoList, Item
from .forms import *

def list(response, id):
    list = TheToDoList.objects.get(id=id)
    if response.method == "POST":
        print(list)
        if response.POST.get("save"):
            for item in list.item_set.all():
                if response.POST.get("checked" + str(item.id)) == "clicked":
                    item.completed = True
                else:
                    item.completed = False
                item.save()
            list.item_set.filter(completed=True).delete()
        elif response.POST.get("newItem"):
            theText = response.POST.get("New Input")
            if len(theText) > 2:
                list.item_set.create(text=theText, completed=False)
            else:
                print("Invalid Input")
    return render(response, "myapps/ToDoList.html", {"list": list})

def homePage(response):
    return render(response, "myapps/home.html")

def createNewList(response):
    if response.method == "POST":
        form = newList(response.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            t = TheToDoList(name=name)
            t.save()
            response.user.todolist.add(t)
        return HttpResponseRedirect("/%i" %t.id)
    else:
        form = newList()
    return render(response, "myapps/newList.html", {'form': form})

def view(request):
    if request.method == "POST":
        list_id_to_delete = request.POST.get("delete_list")
        if list_id_to_delete:
            try:
                list_to_delete = TheToDoList.objects.get(id=list_id_to_delete, user=request.user)
                list_to_delete.delete()
                return HttpResponseRedirect("/")
            except TheToDoList.DoesNotExist:
                pass

    return render(request, "myapps/view.html", {})