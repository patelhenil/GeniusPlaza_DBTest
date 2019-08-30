from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Recipes_model(models.Model):
    recipe_name = models.CharField(max_length=200, blank=True, null=False, unique=True)
    foodie = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return self.recipe_name


class Ingredients_model(models.Model):
    ingredient = models.CharField(max_length=200)
    recipe = models.ForeignKey(Recipes_model, related_name='ingredients', on_delete=models.CASCADE)

    def __str__(self):
        return self.ingredient

class Steps_model(models.Model):
    step = models.TextField(max_length=1000)
    recipe = models.ForeignKey(Recipes_model, related_name='steps', on_delete=models.CASCADE)

    def __str__(self):
        return self.step
