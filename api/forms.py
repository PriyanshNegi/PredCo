from django import forms
from .models import *
from django.contrib.admin import widgets

class UserLoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('email', 'password')
        widgets = {
            'email': forms.TextInput(attrs={'placeholder': 'your email id', 'class': 'w3-input w3-border w3-round'}),
            'password': forms.TextInput(attrs={'placeholder': 'password', 'class': 'w3-input w3-border w3-round'}),
            # 'course_img': forms.FileInput(attrs={'placeholder': 'add any image for course', 'class': 'w3-input w3-border w3-round'}),
            # 'course_overview': forms.Textarea(attrs={'placeholder': 'overview', 'class': 'w3-input w3-border w3-round'}),
            # 'course_duration': forms.TimeInput(attrs={'placeholder': 'duration', 'class': 'w3-input w3-border w3-round'}),
            # 'course_level': forms.Select(attrs={'placeholder': 'course level', 'class': 'w3-input w3-border w3-round'}),
        }

class OrgForm(forms.ModelForm):
    class Meta:
        model = Org
        fields = ('name', 'industry', 'domain')
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'organization\'s name', 'class': 'w3-input w3-border w3-round'}),
            # 'course_img': forms.FileInput(attrs={'placeholder': 'add any image for course', 'class': 'w3-input w3-border w3-round'}),
            'industry': forms.Select(attrs={'placeholder': 'industry', 'class': 'w3-input w3-border w3-round'}),
            'domain': forms.Select(attrs={'placeholder': 'domain', 'class': 'w3-input w3-border w3-round'}),
        }

class UseCaseForm(forms.ModelForm):
    class Meta:
        model = UseCase
        fields = ('title', 'desc', 'iframe_link')
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'title for the use case', 'class': 'w3-input w3-border w3-round'}),
            'desc': forms.Textarea(attrs={'placeholder': 'overview', 'class': 'w3-input w3-border w3-round'}),
            'iframe_link': forms.Textarea(attrs={'placeholder': 'overview', 'class': 'w3-input w3-border w3-round'}),
        }

class SensorForm(forms.ModelForm):
    class Meta:
        model = Sensor
        fields = ('title', 'cat', 'active')
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'title for the use case', 'class': 'w3-input w3-border w3-round'}),
            'cat': forms.Select(attrs={'placeholder': 'description', 'class': 'w3-input w3-border w3-round'}),
            'active': forms.CheckboxInput(attrs={'placeholder': 'status', 'class': 'w3-input w3-checkbox w3-border w3-round'})
        }