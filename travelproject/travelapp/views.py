from django.http import HttpResponse
from django.shortcuts import render
from . models import Place,Team

# # Create your views here.
# def demo(request):
#     return HttpResponse("Hello World")
#
#
# def about(request):
#     return render(request, "about.html")

def web(request):
    obj=Place.objects.all()
    tem =Team.objects.all()
    return render(request,"index.html",{'result':obj,'team':tem})

