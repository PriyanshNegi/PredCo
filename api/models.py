from django.db import models
from django.contrib.auth.models import User
import string
import random
import datetime
from django.utils.text import slugify

def org_default():
    length=9
    while True:
        code = ''.join(random.choices(string.ascii_lowercase,k=length))
        break
    return code

class Org(models.Model):
    INDUSTRY_CHOICES = [    
        ('Manufacturing', 'Manufacturing'),    
        ('Oil and gas', 'Oil and gas'),    
        ('Aerospace and defense', 'Aerospace and defense'),    
        ('Automotive', 'Automotive'),    
        ('Chemicals', 'Chemicals'),    
        ('Energy and utilities', 'Energy and utilities'),    
        ('Healthcare', 'Healthcare'),    
        ('Mining', 'Mining'),    
        ('Pharmaceuticals', 'Pharmaceuticals'),    
        ('Food and beverage', 'Food and beverage'),    
        ('Transportation and logistics', 'Transportation and logistics'),    
        ('Agriculture', 'Agriculture'),    
        ('Construction', 'Construction'),    
        ('Telecommunications', 'Telecommunications'),    
        ('Banking and finance', 'Banking and finance')
    ]
    DOMAIN_CHOICES = [            
        ('Manufacturing - Automotive', 'Manufacturing - Automotive'),            
        ('Manufacturing - Electronics', 'Manufacturing - Electronics'),            
        ('Manufacturing - Aerospace', 'Manufacturing - Aerospace'),            
        ('Manufacturing - Chemicals', 'Manufacturing - Chemicals'),            
        ('Manufacturing - Food & Beverage', 'Manufacturing - Food & Beverage'),            
        ('Manufacturing - Machinery', 'Manufacturing - Machinery'),            
        ('Manufacturing - Metals', 'Manufacturing - Metals'),            
        ('Manufacturing - Plastics', 'Manufacturing - Plastics'),            
        ('Manufacturing - Textiles', 'Manufacturing - Textiles'),            
        ('Healthcare - Hospitals', 'Healthcare - Hospitals'),            
        ('Healthcare - Pharmaceuticals', 'Healthcare - Pharmaceuticals'),            
        ('Transportation - Aviation', 'Transportation - Aviation'),            
        ('Transportation - Rail', 'Transportation - Rail'),            
        ('Energy - Oil & Gas', 'Energy - Oil & Gas'),            
        ('Energy - Power Generation', 'Energy - Power Generation'),            
        ('Utilities - Water Treatment', 'Utilities - Water Treatment'),           
        ('Utilities - Waste Management', 'Utilities - Waste Management'),            
        ('Mining - Metals', 'Mining - Metals'),            
        ('Mining - Minerals', 'Mining - Minerals'),            
        ('Construction - Building', 'Construction - Building'),            
        ('Construction - Infrastructure', 'Construction - Infrastructure'),            
        ('Agriculture - Farming', 'Agriculture - Farming'),            
        ('Agriculture - Livestock', 'Agriculture - Livestock'),            
        ('Retail - Supermarkets', 'Retail - Supermarkets'),            
        ('Retail - Department Stores', 'Retail - Department Stores'),            
        ('Hospitality - Hotels', 'Hospitality - Hotels'),            
        ('Hospitality - Restaurants', 'Hospitality - Restaurants'),            
        ('Education - Schools', 'Education - Schools'),            
        ('Education - Universities', 'Education - Universities'),            
        ('Government - Military', 'Government - Military'),            
        ('Government - Municipalities', 'Government - Municipalities'),            
        ('Technology - Software', 'Technology - Software'),            
        ('Technology - Hardware', 'Technology - Hardware'),            
        ('Finance - Banking', 'Finance - Banking'),            
        ('Finance - Insurance', 'Finance - Insurance'),            
        ('Media - Broadcasting', 'Media - Broadcasting'),            
        ('Media - Publishing', 'Media - Publishing'),            
        ('Other', 'Other')
        ]

    key = models.SlugField(default=org_default)
    name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to="courses/", null=True)

    industry = models.CharField(choices=INDUSTRY_CHOICES, max_length=50)
    domain = models.CharField(choices=DOMAIN_CHOICES, max_length=50)

    client_users = models.ManyToManyField(User, related_name="clients", blank=True)
    our_admin = models.ForeignKey(User, on_delete=models.CASCADE)

def usecase_default():
    length=10
    while True:
        code = ''.join(random.choices(string.ascii_lowercase,k=length))
        break
    return code

class UseCase(models.Model):
    key = models.SlugField(default=usecase_default)
    org = models.ForeignKey(Org, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    desc = models.TextField(max_length=400)

    iframe_link = models.TextField(max_length=1000)

def sensor_default():
    length=12
    while True:
        code = ''.join(random.choices(string.ascii_lowercase,k=length))
        break
    return code

class Sensor(models.Model):
    CATEGORY_CHOICES = [
        ('Temperature', 'Temperature'),
        ('Humidity', 'Humidity'),
        ('Light', 'Light'),
        ('Pressure', 'Pressure'),
        ('Sound', 'Sound'),
        ('Motion', 'Motion'),
        ('Proximity', 'Proximity'),
        ('Gas', 'Gas'),
        ('Color', 'Color'),
        ('Electricity', 'Electricity'),
        ('Magnetic', 'Magnetic'),
        ('Acceleration', 'Acceleration'),
        ('Gyroscope', 'Gyroscope'),
        ('Barometer', 'Barometer'),
        ('Infrared', 'Infrared'),
        ('UV', 'UV'),
        ('GPS', 'GPS'),
        ('Flow', 'Flow'),
        ('pH', 'pH'),
        ('Humectant', 'Humectant'),
        ('Smoke', 'Smoke'),
        ('CO2', 'CO2'),
        ('CO', 'CO'),
        ('Ozone', 'Ozone'),
        ('Water', 'Water'),
        ('Vibration', 'Vibration'),
        ('Weight', 'Weight'),
        ('Level', 'Level'),
        ('Radiation', 'Radiation'),
        ('Other', 'Other')
    ]

    key = models.SlugField(default=sensor_default)
    cat = models.CharField(choices=CATEGORY_CHOICES, max_length=50)
    usecase = models.ForeignKey(UseCase, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)

    active = models.BooleanField(default=False)

# class Alert(models.Model):
#     CATEGORY_CHOICES = [
#         ('Email', 'Email'),
#         ('Logstash', 'Logstash'),
#         ('Reindex', 'Reindex'),
#         ('Slack', 'Slack'),
#     ]
#     LEVEL_CHOICES = [
#         ('High Priority', 'High Priority'),
#         ('Average Level Alert', 'Average Level Alert'),
#         ('Warning', 'Warning'),
#     ]
#     key = models.CharField(max_length=50)
#     title = models.CharField(max_length=100)

#     level = models.CharField(choices=LEVEL_CHOICES, max_length=15)
#     cat = models.CharField(choices=CATEGORY_CHOICES, max_length=15)