from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView
from django.views import View
from .models import Records


class Home(TemplateView):
    template_name = "home.html"


class SignUp(TemplateView):
    template_name = "sign_up.html"


class SignIn(TemplateView):
    template_name = "sign_in.html"


class RecordsList(TemplateView):
    template_name = "records_list.html"


class RecordCreate(CreateView):
    model = Records
    fields = [
        "login_url",
        "email",
        "username",
        "password",
        "security_key",
        "security_questions",
        "notes",
    ]
    template_name = "record_create.html"
    success_url = "/records/"


class RecordDetail(DetailView):
    template_name = "record_detail.html"


class RecordUpdate(UpdateView):
    model = Records
    fields = [
        "login_url",
        "email",
        "username",
        "password",
        "security_key",
        "security_questions",
        "notes",
    ]
    template_name = "record_update.html"
    success_url = "/records/"


# class RecordDelete(DeleteView):
#     model = Records
#     template_name = "record_delete.html"
#     success_url = "/records/"
