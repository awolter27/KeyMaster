from django.urls import path
from . import views

urlpatterns = [
    path("", views.Home.as_view(), name="home"),
    path("sign-up/", views.SignUp.as_view(), name="sign_up"),
    path("sign-in/", views.SignIn.as_view(), name="sign_in"),
    path("records/", views.Records.as_view(), name="records"),
    path("record/create/", views.RecordCreate.as_view(), name="record_create"),
    path("record/<int:pk>/", views.Record.as_view(), name="record"),
    path("record/<int:pk>/update/", views.RecordUpdate.as_view(), name="record_update"),
    path("record/<int:pk>/delete/", views.RecordDelete.as_view(), name="record_delete"),
]
