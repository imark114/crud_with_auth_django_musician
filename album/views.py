from django.shortcuts import render
from django.views.generic import CreateView
from django.contrib import messages
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .models import Album
from .forms import AddAlbum


# Create your views here.
@method_decorator(login_required,name='dispatch')
class AddAlbumView(CreateView):
    model = Album
    form_class = AddAlbum
    template_name = 'user_form.html'
    success_url = reverse_lazy('add_album')

    def form_valid(self, form):
        messages.success(self.request,'Album Added Succesfully')
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs) -> dict[str]:
        context = super().get_context_data(**kwargs)
        context["type"] = 'Add Album'
        return context
    