from django.shortcuts import render
import markdown2
from . import util
from django import forms
from django.urls import reverse
from django.http import HttpResponse
from django.http import HttpResponseRedirect
import random as rnd

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def search(request):
    if request.method=="POST":
        title=request.POST['q']
        return render(request, "encyclopedia/title.html", {
            "title":title,
            "description":markdown2.Markdown(util.get_entry(title))
        })
    else:
        return HttpResponse("WRONG PAGE")
    
    
def new(request):
    if request.POST:
        util.save_entry(request.POST["q"],request.POST["description"])
        return HttpResponseRedirect(reverse("wiki:index"))
    else:
        return render(request, "encyclopedia/new.html")
    

def random(request):
    title=rnd.choice(((util.list_entries())))
    return render(request, "encyclopedia/title.html", {
        "title":title,
        "description":util.get_entry(title)
    })

def wikititle(request, title):
    return render(request, "encyclopedia/title.html", {
        "title":title,
        "description":util.get_entry(title)
    })