from django.shortcuts import render
from django.views.generic import CreateView
from django.urls import reverse_lazy
from customer.forms import RegistrationForm
from django.contrib import messages


# Create your views here.
class SignUpView(CreateView):
    template_name="signup.html"
    form_class=RegistrationForm
    success_url=reverse_lazy("register")

    def form_valid(self, form):
        messages.success(self.request,"account created successfully")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request,"account creation failed")
        return super().form_invalid(form)
