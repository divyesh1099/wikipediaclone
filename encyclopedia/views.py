from django.shortcuts import render
from markdown2 import Markdown
from . import util
from django import forms
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect, Http404
import random
import difflib
markdowner=Markdown()
def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def search(request):
    if request.method=="POST":
        foundentries=[]
        title=request.POST['q']
        matchword=difflib.get_close_matches(title, util.list_entries())
        if matchword:
            return render(request, "encyclopedia/title.html", {
                "title":matchword[0],
                "description":markdowner.convert(util.get_entry(matchword[0]))
            })
        else:
            for word in util.list_entries():
                if word.startswith(title):
                    actualword=word
                    foundentries.append(actualword)
                else:
                    print("NO SUCH ENTRIES FOUND")
            if foundentries:
                return render(request, "encyclopedia/index.html", {
                    "entries":foundentries
                })
            else:
                return render(request, "encyclopedia/index.html", {
                    "entries":util.list_entries()
                })
    else:
        raise Http404    
    
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
        "description":markdowner.convert(util.get_entry(title))
    })

def wikititle(request, title):
    return render(request, "encyclopedia/title.html", {
        "title":title,
        "description":markdowner.convert(util.get_entry(title))
    })