from django.db import models


class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    date_of_birth = models.IntegerField
    email = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    verified_user = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "User:" + self.first_name + self.last_name

    class Meta:
        ordering = ["last_name"]


class Record(models.Model):
    website = models.CharField(max_length=50)
    login_url = models.CharField(max_length=500)
    email = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    security_key = models.CharField(max_length=500)
    security_questions = models.CharField(max_length=1000)
    notes = models.CharField(max_length=5000)
    verified_record = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "Record:" + self.login_url

    class Meta:
        ordering = ["website"]
