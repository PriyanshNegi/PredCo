from django.db import models
from django.contrib.auth.models import User
import string
import random
import datetime
from django.utils.text import slugify


class Org(models.Model):
    INDUSTRY_CHOICES = [
            ('Beginner', 'Beginner'),
            ('Intermediate', 'Intermediate'),
            ('Advanced', 'Advanced')
        ]
    DOMAIN_CHOICES = [
            ('Beginner', 'Beginner'),
            ('Intermediate', 'Intermediate'),
            ('Advanced', 'Advanced')
        ]

    name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to="courses/", null=True)

    industry = models.CharField(choices=INDUSTRY_CHOICES, max_length=50)
    domain = models.CharField(choices=DOMAIN_CHOICES, max_length=50)

    client_users = models.ManyToManyField(User, related_name="clients")
    our_admin = models.ForeignKey(User, on_delete=models.CASCADE)

class UseCase(models.Model):
    org = models.ForeignKey(Org, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    desc = models.TextField(max_length=400)

    iframe_link = models.TextField(max_length=1000)

class Sensor(models.Model):
    CATEGORY_CHOICES = [
            ('Beginner', 'Beginner'),
            ('Intermediate', 'Intermediate'),
            ('Advanced', 'Advanced')
        ]
    cat = models.CharField(choices=CATEGORY_CHOICES, max_length=50)
    usecase = models.ForeignKey(UseCase, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)

    active = models.BooleanField(default=False)