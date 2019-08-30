from rest_framework import serializers
from .models import Recipes_model, Steps_model, Ingredients_model


class Recipes_Serializers(serializers.ModelSerializer):
    steps = serializers.StringRelatedField(many=True)
    ingredients = serializers.StringRelatedField(many=True)


    class Meta:
        model = Recipes_model
        fields = ('recipe_name', 'foodie', 'steps', 'ingredients')

class Steps_Serializers(serializers.HyperlinkedModelSerializer):


    class Meta:
        model = Steps_model
        fields = ('id', 'step', 'recipe', 'url')


class Ingredients_Serializers(serializers.HyperlinkedModelSerializer):


    class Meta:
        model = Ingredients_model
        fields = ('id', 'ingredient', 'recipe', 'url')