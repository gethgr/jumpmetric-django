from django.db.models import fields
from rest_framework import serializers
#from .models import Item
from jumpmetric.models import Trial
 
class TrialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trial
        fields = ('fullname', 'height', 'weight', 'age', 'email', 'occupy', 'type_of_trial')