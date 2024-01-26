from django.shortcuts import render
from django.contrib.auth.models import User
from django.views.generic import CreateView,TemplateView
from django.contrib.auth.views import LoginView,LogoutView
from django.contrib import messages
from .forms import SignUpForm
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from musician.models import Musician
# Create your views here.

class SignUpView(CreateView):
    model = User
    form_class = SignUpForm
    template_name = 'user_form.html'
    success_url = reverse_lazy('signup')

    def form_valid(self, form):
        messages.success(self.request,'Account Created Successfully')
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs) -> dict[str]:
        context = super().get_context_data(**kwargs)
        context["type"] = 'Sign Up'
        return context
    
class UserLoginView(LoginView):
    template_name = 'user_form.html'

    def get_success_url(self):
        return reverse_lazy('profile')
    
    def form_valid(self, form):
        messages.success(self.request,'Logged In Successfully')
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.warning(self.request, 'Given Informations are incorrect')
        response = super().form_invalid(form)
        return response
    
    def get_context_data(self, **kwargs) -> dict[str]:
        context = super().get_context_data(**kwargs)
        context["type"] = 'Login' 
        return context

class UserLogout(LogoutView):
    def get_success_url(self):
        return reverse_lazy('home')

@method_decorator(login_required,name='dispatch')
class ProfileView(TemplateView):
    template_name = 'profile.html'

    def get_context_data(self, **kwargs) -> dict[str]:
        context = super().get_context_data(**kwargs)
        context["data"] = Musician.objects.all()
        return context