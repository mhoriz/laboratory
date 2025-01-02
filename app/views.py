from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Resident
from django.urls import reverse_lazy

class HomepageView(TemplateView):
    template_name = 'app/Home.html'

class AboutpageView(TemplateView):
    template_name = 'app/About.html'

class ResidentListView(ListView):
    model = Resident
    context_object_name = 'posts'
    template_name = 'app/post_list.html'

class ResidentDetailView(DetailView):
    model = Resident
    context_object_name = 'post'
    template_name = 'app/post_detail.html'

class ResidentCreateView(CreateView):
    model = Resident
    fields = ['resident_id', 'first_name', 'last_name']
    template_name = 'app/post_create.html'

class ResidentUpdateView(UpdateView):
    model = Resident
    fields = ['resident_id', 'first_name', 'last_name']
    template_name = 'app/post_update.html'

class ResidentDeleteView(DeleteView):
    model = Resident
    template_name = 'app/post_delete.html'
    success_url = reverse_lazy('Home')
