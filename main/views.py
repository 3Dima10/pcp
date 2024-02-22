from django.shortcuts import render, redirect
from .models import Dolw
from django.views.generic import CreateView
from .forms import *
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views.generic import DetailView

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
    username = request.user.username
    return render(request, "main/hom.html", {"data": data, "username": username})

@login_required
def index2(request):
    username = request.user.username
    return render(request, "main/index2.html", {"username": username})

def rol(request):
    return render(request, "main/rol.html")

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


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = "main/logo.html"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        # c_def = self.get_user_context(titlt = "Авторизацыя")
        return dict(list(context.items()))


# class proga(DetailView):
#     model = Dolw
#     template_name = "main/proga.html"
#     context_object_name = "post"


def create(request):
    error = ""
    if request.method == "POST":
        form = Ahop(request.POST)

        if form.is_valid():
            form.save()
            return redirect("home")
        else:
            error = "Форма была не верной"

    form = Ahop()

    date = {
        "form": form,
        "error": error,
    }
    return render(request, "main/proga.html", date)
