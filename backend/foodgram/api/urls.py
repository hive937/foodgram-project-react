from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import IngredientViewSet, RecipeViewSet, TagViewSet

app_name = 'api'

router = DefaultRouter()

router.register('ingredients', IngredientViewSet, name='Ingredients')
router.register('tags', TagViewSet, name='Tags')
router.register('recipes', RecipeViewSet, name='Recipes')

urlpatterns = [

    path('', include(router.urls)),
]
