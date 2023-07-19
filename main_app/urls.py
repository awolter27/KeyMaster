from django.urls import path
from . import views

urlpatterns = [
    path("", views.Home.as_view(), name="home"),
    path("accounts/signup/", views.SignUp.as_view(), name="signup"),
    path("records/", views.RecordsList.as_view(), name="records_list"),
    path("record/create/", views.RecordCreate.as_view(), name="record_create"),
    path("record/<int:pk>/", views.RecordDetail.as_view(), name="record_detail"),
    path("record/<int:pk>/update/", views.RecordUpdate.as_view(), name="record_update"),
    path("record/<int:pk>/delete/", views.RecordDelete.as_view(), name="record_delete"),
    path("logout", views.logout_view, name= "logout"),
]
