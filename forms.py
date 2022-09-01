from django import forms
from django.forms import ModelForm
from .models import *
from django.contrib.auth.models import User

class storyForm(forms.Form):
    authorFname = forms.CharField(max_length=256,label='authorFname')
    authorLname = forms.CharField(max_length=256,label='authorLname')
    authorEmail = forms.CharField(max_length=256,label='authorEmail')
    authorNumber = forms.CharField(max_length=256,label='authorNumber')
    scamTitle = forms.CharField(max_length=256,label='scamTitle')
    scamType = forms.CharField(max_length=256,label='scamType')
    nameOfScamer = forms.CharField(max_length=256,label='nameOfScamer')
    contentOfScamer = forms.CharField(max_length=256,label='contentOfScamer')
    emailOfScamer = forms.CharField(max_length=256,label='emailOfScamer')
    scamDetail = forms.CharField(widget=forms.Textarea,label='scamDetail')
    timestamp = forms.DateTimeField(label='timestamp')

class CooperationForm(forms.Form):
    organisationName = forms.CharField(max_length=256,label='organisationName')
    organisationEmail = forms.CharField(max_length=256,label='organisationEmail')
    personInContact = forms.CharField(max_length=256,label='personInContact')
    ContactNumber = forms.CharField(max_length=256,label='ContactNumber')
    cooperationDetail = forms.CharField(max_length=256,label='cooperationDetail')
    timestamp = forms.DateTimeField(label='timestamp')


class JoinActivitesForm(forms.Form):
    activitesTitle = forms.CharField(max_length=256,label='activitesTitle')
    joinerName = forms.CharField(max_length=256,label='joinerName')
    joinerEmail = forms.CharField(max_length=256,label='joinerEmail')
    joinerContactNumber = forms.CharField(max_length=256,label='joinerContactNumber')
    joinerDob  = forms.CharField(max_length=256,label='joinerDob')
    joinAs = forms.CharField(max_length=256,label='joinAs')
    