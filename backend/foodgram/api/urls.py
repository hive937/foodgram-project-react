from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import IngredientViewSet, RecipeViewSet, TagViewSet

app_name = 'api'

router = DefaultRouter()

router.register('ingredients', IngredientViewSet, 'Ingredients')
router.register('tags', TagViewSet, 'Tags')
router.register('recipes', RecipeViewSet, 'Recipes')

urlpatterns = [

    path('', include(router.urls)),
]
