from django.shortcuts import render
from .models import Dolw

# from django.http import HttpResponse
# Create your views here.


def index(request):
    # return HttpResponse("<h2>Lorem is dolar</h2>")
    # data = {"title": "Главная страница",
    #         "value": ["Some,", "Hello", "3510"],
    #         "slovo": {
    #             "name": "Dima",
    #             "password": 12345678,
    #             "age": 19
    #         },}
    data = Dolw.objects.order_by()
    return render(request, "main\hom.html", {"data": data})


def index2(request):
    return render(request, "main\index2.html")


def cot(request):
    return render(request, "main\cot.html")
