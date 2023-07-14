from django.shortcuts import redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.base import TemplateView
from django.views.generic import DetailView
from django.db.models import Q
from django.views import View
from .models import Record


class Home(TemplateView):
    template_name = "home.html"


class SignUp(TemplateView):
    template_name = "sign_up.html"


class SignIn(TemplateView):
    template_name = "sign_in.html"


class RecordsList(TemplateView):
    template_name = "records_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        search = self.request.GET.get('search')
        if search != None:
            context['recs'] = Record.objects.filter(Q(website__icontains=search) | Q(email__icontains=search) | Q(username__icontains=search) | Q(login_url__icontains=search))
        else:
            context['recs'] = Record.objects.all()
        return context


class RecordCreate(CreateView):
    model = Record
    fields = [
        "website",
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
    model = Record
    template_name = "record_detail.html"


class RecordUpdate(UpdateView):
    model = Record
    fields = [
        "website",
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


class RecordDelete(DeleteView):
    model = Record
    template_name = "record_delete.html"
    success_url = "/records/"
