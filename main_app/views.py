from django.shortcuts import redirect
from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.base import TemplateView
from django.views.generic import DetailView
from django.views import View
from .models import Record


class Home(TemplateView):
    template_name = "home.html"


class SignUp(TemplateView):
    template_name = "sign_up.html"


class SignIn(TemplateView):
    template_name = "sign_in.html"


class Records(TemplateView):
    template_name = "records.html"


class RecordCreate(CreateView):
    model = Record
    fields = []
    template_name = "record_create.html"
    success_url = "/records/"


class Record(DetailView):
    template_name = "record.html"


class RecordUpdate(UpdateView):
    model = Record
    fields = []
    template_name = "record_update.html"
    success_url = "/records/"


class RecordDelete(DeleteView):
    model = Record
    template_name = "record_delete.html"
    success_url = "/records/"
