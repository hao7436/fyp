import factory

from django.test import TestCase
from django.conf import settings
from django.core.files import File

from .models import *
from random import randint
from random import choice

class StoriesFactory(factory.django.DjangoModelFactory):
    authorFname='shen'
    authorLname='hao'
    authorEmail='a88547726@gmail.com'
    authorNumber='12345678'
    scamTitle='Impersonation-scams'
    scamType='moh'
    nameOfScamer='22222222'
    contentOfScamer='try to upload data'
    emailOfScamer='a88547726@gmail.com'
    scamDetail='BEWARE OF SCAM CALLS CLAIMING TO BE FROM "MOH"'
    timestamp ='2022-07-20 04:49:43.146957'

    class Meta:
        model = Stories

class CooperationFactory(factory.django.DjangoModelFactory):
    organisationName = 'MOE'
    organisationEmail = 'MOE@GMAIL.COM'
    personInContact = 'JOHN'
    ContactNumber = '12345678'
    cooperationDetail = 'i want to cooperation with you to come out with a anti scam event'
    timestamp = '2022-07-22T03:54:05.607894Z'

    class Meta:
        model = Cooperation

