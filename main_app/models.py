from django.db import models
from django.contrib.auth.models import User


class Record(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    website = models.CharField(max_length=50)
    login_url = models.CharField(max_length=500)
    email = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    security_key = models.TextField(max_length=500)
    security_questions = models.TextField(max_length=1000)
    notes = models.TextField(max_length=5000)
    verified_record = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "Record:" + self.website

    class Meta:
        ordering = [models.functions.Upper("website")]
