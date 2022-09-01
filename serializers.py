from rest_framework import serializers
from .models import *
from drf_writable_nested import WritableNestedModelSerializer

class StoriesSerializer(WritableNestedModelSerializer,serializers.ModelSerializer):
    class Meta:
        model = Stories
        fields = ['pk','authorFname', 'authorLname','authorEmail','authorNumber','scamTitle',
                    'scamType','nameOfScamer','contentOfScamer','emailOfScamer','scamDetail','timestamp']

class CooperationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cooperation
        fields = ['organisationName', 'organisationEmail',
                'personInContact', 'ContactNumber', 'cooperationDetail', 'timestamp']


class JoinActivitesSerializer(serializers.ModelSerializer):
    class Meta:
        model = JoinActivites
        fields = ['activitesTitle', 'joinerName','joinerEmail', 'joinerContactNumber',
                 'joinerDob', 'joinAs']

