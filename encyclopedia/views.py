from django.shortcuts import render
import markdown2
from . import util
from django import forms
from django.urls import reverse
from django.http import HttpResponse
from django.http import HttpResponseRedirect

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })
def new(request):
    if request.POST:
        util.save_entry(request.POST["q"],request.POST["description"])
        return HttpResponseRedirect(reverse("wiki:index"))
    else:
        return render(request, "encyclopedia/new.html")
    return render(request, "encyclopedia/new.html")
    

def random(request):
    return render(request, "encyclopedia/random.html")

def wikititle(request, q):
    querry=request.POST
    print(querry)
    if querry:
        return render(request, "encyclopedia/title.html",{
            "title":querry,
            "description":markdown2.markdown(util.get_entry(querry))
        })
    else:
        return render(request, "encyclopedia/title.html",{
            "title":"NO PAGE EXISTS LIKE THAT",
            "description":"RETYPE THAT"
        })