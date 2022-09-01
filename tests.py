import json
from django.test import TestCase
from django.urls import reverse
from django.urls import reverse_lazy

from rest_framework.test import APIRequestFactory
from rest_framework.test import APITestCase

from .model_factories import *
from .serializers import *



# Create your tests here.
class StoriesSerialiserTest(APITestCase):
    Stories1 = None
    Storiesserializer = None
    delete_url = ''

    def setUp(self):
        self.Stories1 = StoriesFactory.create(pk=1,authorFname='shen')
        self.Storiesserializer = StoriesSerializer(instance=self.Stories1)

    def tearDown(self):
        Stories.objects.all().delete()
        StoriesFactory.reset_sequence(0)


    def  StoriesSerilaiserHasCorrectFields(self):
        data = self.Storiesserializer.data
        self.assertEqual(set(data.keys()), set(['authorFname', 'authorLname','authorEmail','authorNumber','scamTitle',
                    'scamType','nameOfScamer','contentOfScamer','emailOfScamer','scamDetail','timestamp']))

    def test_StoriesSerilaiserauthorEmailHasCorrectData(self):
        data = self.Storiesserializer.data
        self.assertEqual(data['authorEmail'], "a88547726@gmail.com")

    def test_StoriesSerilaiserauthorNumberHasCorrectData(self):
        data = self.Storiesserializer.data
        self.assertEqual(data['authorNumber'], "12345678")

    def test_StoriesDetailDeleteIsSuccessful(self):
        response = self.client.delete(self.delete_url, format='json')
        self.assertEqual(response.status_code, 200)

class CooperationSerialiserTest(APITestCase):
    Cooperation1 = None
    Cooperationserializer = None
    

    def setUp(self):
        self.Cooperation1 = CooperationFactory.create(pk=1,organisationName='MOE')
        self.Cooperationserializer = CooperationSerializer(instance=self.Cooperation1)

    def tearDown(self):
        Cooperation.objects.all().delete()
        CooperationFactory.reset_sequence(0)


    def  CooperationSerilaiserHasCorrectFields(self):
        data = self.Cooperationserializer.data
        self.assertEqual(set(data.keys()), set(['organisationName', 'organisationEmail','personInContact','ContactNumber','cooperationDetail',
                    'timestamp']))

    def test_CooperationserializerorganisationNameHasCorrectData(self):
        data = self.Cooperationserializer.data
        self.assertEqual(data['organisationName'], "MOE")

    def test_CooperationserializerorganisationEmailHasCorrectData(self):
        data = self.Cooperationserializer.data
        self.assertEqual(data['organisationEmail'], "MOE@GMAIL.COM")

