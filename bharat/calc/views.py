from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home(request):
    return render(request, "home.html", {"name": "my name"})


def add_num(request):
    n1 = request.POST["num1"]
    n2 = request.POST["num2"]
    a = n1+n2
    return render(request, "result.html", {"ans": a})