from django.urls import path, include
from .views import Recipes_Viewset, Ingredients_Viewset, Steps_Viewset
from rest_framework import routers


router = routers.DefaultRouter()
router.register('recipes', Recipes_Viewset)
router.register('steps', Steps_Viewset)
router.register('ingredients', Ingredients_Viewset)


urlpatterns = [
    path('', include(router.urls))
    # path('', include('RecipesAPI.urls'))

]