from django.shortcuts import render
from musician.models import Musician
from django.views.generic import TemplateView

class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs) -> dict[str]:
        context = super().get_context_data(**kwargs)
        context["data"] = Musician.objects.all()
        return context
    