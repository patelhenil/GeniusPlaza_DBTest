from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import Recipes_model, Steps_model, Ingredients_model
from .serializers import Recipes_Serializers, Steps_Serializers, Ingredients_Serializers

# Create your views here.


class Recipes_Viewset(viewsets.ModelViewSet):
    queryset = Recipes_model.objects.all()
    serializer_class = Recipes_Serializers
    #permission_classes = (permissions.IsAuthenticatedOrReadOnly,)



class Steps_Viewset(viewsets.ModelViewSet):
    queryset = Steps_model.objects.all()
    serializer_class = Steps_Serializers



class Ingredients_Viewset(viewsets.ModelViewSet):
    queryset = Ingredients_model.objects.all()
    serializer_class = Ingredients_Serializers


