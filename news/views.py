from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, redirect
from .models import Aweitr
from .forms import Ahop
from django.views.generic import DetailView, UpdateView, DeleteView, ListView

# Create your views here.


def news_home(request):
    # news = Aweitr.objects.all()
    news = Aweitr.objects.order_by("-data")
    return render(request, "news/news_home.html", {"news": news})
    # return render(request, "news\news_home.html")


class nowels(DetailView):
    model = Aweitr
    template_name = "news/gener.html"
    context_object_name = "post"


class ubate(UpdateView):
    model = Aweitr
    template_name = "news/create.html"

    # fields = ["title", "anons", "text", "data"]
    form_class = Ahop


class delete(DeleteView):
    model = Aweitr
    template_name = "news/delete.html"
    success_url = "/news/"
    # fields = ["title", "anons", "text", "data"]


class Search(ListView):
    template_name = "news/news_home.html"
    context_object_name = "post"
    paginate_by = 5

    def get_queryset(self):
        return Aweitr.objects.filter(title__icontains=self.request.GET.get("q"))

    def get_context_data(self, *, objects_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context["q"] = self.request.GET.get("q")

        return context

def create(request):
    error = ""
    if request.method == "POST":
        form = Ahop(request.POST)

        if form.is_valid():
            form.save()
            return redirect("news_home")
        else:
            error = "Форма была не верной"

    form = Ahop()

    date = {
        "form": form,
        "error": error,
    }
    return render(request, "news/create.html", date)
