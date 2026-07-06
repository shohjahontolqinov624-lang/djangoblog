from django.shortcuts import render, redirect
from .models import Bloglar

def home(request):
    blogs = Bloglar.objects.all()
    return render(request, "index.html", {"blogs": blogs})

def blog(request, pk):
    blog = Bloglar.objects.get(id=pk)
    return render(request, "blog.html", {"blog": blog})

def editblog(request, pk):
    blog = Bloglar.objects.get(id=pk)

    if request.method == "POST":
        title = request.POST.get("title")
        shortdesc = request.POST.get("short")
        longdesc = request.POST.get("long")
        blog.title = title
        blog.shortdesc = shortdesc
        blog.longdesc = longdesc
        blog.save()
        return redirect("/")

    return render(request, "edit.html", {"blog": blog})

def deleteblog(request, pk):
    blog = Bloglar.objects.get(id=pk)
    blog.delete()
    return redirect("/")