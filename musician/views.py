from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView,UpdateView,DeleteView
from .models import Musician
from .forms import AddMusician
from django.contrib import messages
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

# Create your views here.

class AddMusicianView(CreateView):
    model = Musician
    form_class = AddMusician
    template_name = 'user_form.html'
    success_url = reverse_lazy('add_musician')

    def form_valid(self, form):
        messages.success(self.request,'Musician Added Successfully')
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs) -> dict[str]:
        context = super().get_context_data(**kwargs)
        context["type"] = 'Add Musician'
        return context

@method_decorator(login_required,name='dispatch')
class EditMusicianView(UpdateView):
    model = Musician
    form_class = AddMusician
    template_name = 'user_form.html'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('profile')

    def form_valid(self, form):
        messages.success(self.request,'Musician Updated Successfully')
        return super().form_valid(form)

    def get_context_data(self, **kwargs) -> dict[str]:
        context = super().get_context_data(**kwargs)
        context["type"] = 'Updated Musician'
        return context

@method_decorator(login_required,name='dispatch')
class DeleteMusicianView(DeleteView):
    model = Musician
    template_name = 'user_form.html'
    success_url = reverse_lazy('profile')
    pk_url_kwarg = 'id'
    def get_context_data(self, **kwargs) -> dict[str]:
        context = super().get_context_data(**kwargs)
        context["type"] = 'Delete Musician'
        return context