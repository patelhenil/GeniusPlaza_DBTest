from django.contrib import admin
from .models import Recipes_model, Steps_model, Ingredients_model

# Register your models here.

admin.site.register(Recipes_model)
admin.site.register(Steps_model)
admin.site.register(Ingredients_model)