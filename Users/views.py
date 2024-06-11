from django.contrib.auth import logout
from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, UpdateView
from .forms import UserAuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Client


class UserLoginView(LoginView):
    template_name = 'Users/login.html'
    form_class = UserAuthenticationForm


class ClientsListView(LoginRequiredMixin, ListView):
    model = Client
    template_name = 'Users/clients_list.html'
    context_object_name = 'clients'

    def get_queryset(self):
        current_user = self.request.user
        queryset = Client.objects.filter(responsible_full_name=current_user)
        return queryset


class UpdateStatusView(LoginRequiredMixin, UpdateView):
    model = Client
    fields = ['status']
    template_name = 'Users/clients_list.html'
    success_url = reverse_lazy('users:clients')

    def form_valid(self, form):
        client = self.get_object()
        client.status = form.cleaned_data['status']
        client.save()
        return super().form_valid(form)


def user_logout(request):
    logout(request)
    return redirect(reverse('users:login'))
