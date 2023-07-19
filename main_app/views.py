from django.shortcuts import redirect, render
from django.contrib.auth import login
from django.urls import reverse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.base import TemplateView
from django.views.generic import DetailView
from django.db.models import Q
from django.views import View
from .models import Record
from .forms import SignUpForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth import logout


class Home(TemplateView):
    template_name = "home.html"


class SignUp(View):
    def get(self, request):
        form_class = SignUpForm
        context = {"form": form_class}
        return render(request, "registration/signup.html", context)

    def post(self, request):
        form_class = SignUpForm(request.POST)
        if form_class.is_valid():
            user = form_class.save()
            login(request, user)
            return redirect("records_list")
        else:
            context = {"form": form_class}
            return render(request, "registration/signup.html", context)


def logout_view(request):
    logout(request)
    return redirect("home")


@method_decorator(login_required, name="dispatch")
class RecordsList(TemplateView):
    template_name = "records_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        search = self.request.GET.get("search")
        if search != None:
            context["recs"] = Record.objects.filter(
                Q(website__icontains=search)
                | Q(email__icontains=search)
                | Q(username__icontains=search)
                | Q(login_url__icontains=search),
                user=self.request.user,
            )
        else:
            context["recs"] = Record.objects.filter(user=self.request.user)
        return context


@method_decorator(login_required, name="dispatch")
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

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(RecordCreate, self).form_valid(form)

    def get_success_url(self):
        return reverse("record_detail", kwargs={"pk": self.object.pk})


@method_decorator(login_required, name="dispatch")
class RecordDetail(DetailView):
    model = Record
    template_name = "record_detail.html"


@method_decorator(login_required, name="dispatch")
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


@method_decorator(login_required, name="dispatch")
class RecordDelete(DeleteView):
    model = Record
    template_name = "record_delete.html"
    success_url = "/records/"
