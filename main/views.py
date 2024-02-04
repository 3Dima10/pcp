from django.shortcuts import render, redirect
from .models import Dolw
from django.views.generic import CreateView
from .forms import *
from django.urls import reverse_lazy

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
    return render(request, "main/hom.html", {"data": data})


def index2(request):
    return render(request, "main/index2.html")


def cot(request):
    return render(request, "main/cot.html")

def love(request):
    return render(request, "main/love.html")

class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = "main/register.html"
    success_url = reverse_lazy('home')

    def get_context_data(self, *, objects_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        # c_def = self.get_user_context(title="Регистрацыя")


        return dict(list(context.items()))
