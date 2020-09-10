from django.shortcuts import render
import markdown2
from . import util
from django import forms
from django.urls import reverse
from django.http import HttpResponse
from django.http import HttpResponseRedirect
import random

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def search(request):
    if request.method=="POST":
        title=request.POST['q']
        return render(request, "encyclopedia/title.html", {
            "title":title,
            "description":util.get_entry(title)
        })
    else:
        return HttpResponse("WRONG PAGE")
    
    
def new(request):
    if request.POST:
        util.save_entry(request.POST["q"],request.POST["description"])
        return HttpResponseRedirect(reverse("wiki:index"))
    else:
        return render(request, "encyclopedia/new.html")

def edit(request, title):
    if not request.POST:
        return render(request, "encyclopedia/edit.html", {
        "title":title,
        "description":util.get_entry(title)
        })
    else:
        print("NOICE")
        util.save_entry(request.POST["q"],request.POST["description"])
        return HttpResponseRedirect(reverse("wiki:index"))

def randompage(request):
    title=random.choice(((util.list_entries())))
    return render(request, "encyclopedia/title.html", {
        "title":title,
        "description":util.get_entry(title)
    })

def wikititle(request, title):
    return render(request, "encyclopedia/title.html", {
        "title":title,
        "description":util.get_entry(title)
    })