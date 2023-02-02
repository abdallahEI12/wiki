from django.shortcuts import render, redirect , reverse
from django.http import HttpResponseRedirect
import markdown2 as md
from . import util
from django import forms
from random import choice

class Newpageform(forms.Form):
    title = forms.CharField(label= "title")

    content = forms.CharField(label="add content")





def gotowiki(request):
    return HttpResponseRedirect("/wiki")

def index(request):
    if request.method == "GET":
        return render(request, "encyclopedia/index.html", {
            "entries": util.list_entries()
        })
    elif request.method == "POST":
        entry = request.POST.get('q')
    return HttpResponseRedirect(f"/wiki/{entry}")



def viewentry(request,entry):
    if entry in util.list_entries():
        title = entry
        entry = util.get_entry(entry)
        entry = md.markdown(entry)
        return render(request, "encyclopedia/entryview.html", {
            "entry": entry,
            "title": title,
        })

    else:
        possible_entries = []
        for element in util.list_entries():
            if entry.lower() in element.lower():
                possible_entries.append(element)
        if len(possible_entries) == 0:
            return render(request, "encyclopedia/error.html")
        return render (request, "encyclopedia/searchresults.html",{
            "possible_entries": possible_entries
        })
def newpage(request):
    if request.method == "GET":
        return render(request,"encyclopedia/newpage.html",{
            "form": Newpageform()
        })
    elif request.method == "POST":

        form = Newpageform(request.POST)

        if form.is_valid():
            title = form.cleaned_data["title"]
            content = form.cleaned_data["content"]

            if title not in util.list_entries():
                util.save_entry(title,content)
                return render(request,"encyclopedia/newpageadded.html")
            else:
                return render(request,"encyclopedia/pagecreateerror.html")

def editpage(request,entry):
    if request.method == "GET":
        entry_content = util.get_entry(entry)
        print(entry_content)
        return render(request,"encyclopedia/editentry.html",{
            "entry":entry,
            "content":entry_content
        })
    else:
        title = request.POST.get("entry")
        content = request.POST.get("content").strip()
        util.save_entry(title,content)
        return HttpResponseRedirect(f"/wiki/{title}")
def randompage(request):
    entries = util.list_entries()

    entry = choice(entries)

    return HttpResponseRedirect(f"/wiki/{entry}")