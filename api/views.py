from rest_framework.decorators import api_view
from rest_framework.response import Response
# from .models import Item
from jumpmetric.models import Trial
from .serializers import TrialSerializer
from rest_framework import serializers
from rest_framework import status
 

#from suppliers.serializers import SomeSerializer




@api_view(['GET'])
def ApiOverview(request):
    api_urls = {
        'all_items': '/',
        'Search by Type of trial': '/?type_of_trial=type_of_trial',
        'Search by Fullname': '/?fullname=fullname',
        'Add': '/create',
        'Update': '/update/pk',
        'Delete': '/item/pk/delete'
    }
 
    return Response(api_urls)


@api_view(['POST', 'GET'])
def add_items(request):
    trial = TrialSerializer(data=request.data)
 
    # validating for already existing data
    if Trial.objects.filter(**request.data).exists():
        raise serializers.ValidationError('This data already exists')
 
    if trial.is_valid():
        trial.save()
        return Response(trial.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def view_items(request):
    # checking for the parameters from the URL
    if request.query_params:
        trials = Trial.objects.filter(**request.query_params.dict())
    else:
        trials = Trial.objects.all()
 
    # if there is something in items else raise error
    if trials:
        serializer = TrialSerializer(trials, many=True)
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)