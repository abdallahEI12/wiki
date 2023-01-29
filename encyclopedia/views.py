from django.shortcuts import render, redirect , reverse
from django.http import HttpResponseRedirect
import markdown2 as md
from . import util


def gotowiki(request):
    return HttpResponseRedirect("/wiki")

def index(request):
    if request.method == "GET":
        return render(request, "encyclopedia/index.html", {
            "entries": util.list_entries()
        })
    elif request.method == "POST":
        entry = request.POST.get('q')
    return viewentry(request,entry)


def viewentry(request,entry):
    if entry in util.list_entries():
        title = entry
        entry = util.get_entry(entry)
        entry = md.markdown(entry)

    else:
        title = None
        entry = None

    return render(request, "encyclopedia/entryview.html",{
        "entry": entry,
        "title": title,
    })

