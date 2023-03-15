from django.contrib import admin
from django.contrib.admin import display

from .models import (Favourite, Ingredient, IngredientInRecipe, Recipe,
                     ShoppingCart, Tag)


class IngredientInRecipeInline(admin.TabularInline):
    model = IngredientInRecipe
    extra = 0


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ('name', 'id', 'author', 'added_in_favorites',
                    'ingredients_in_recipe')
    readonly_fields = ('added_in_favorites',)
    list_filter = ('author', 'name', 'tags')
    inlines = (IngredientInRecipeInline,)

    @display(description='Количество в избранных')
    def added_in_favorites(self, obj):
        return obj.favorites.count()

    @display(description='Ингредиенты')
    def ingredients_in_recipe(self, obj):
        return "\n".join([a.ingredient for a in obj.recipes.all()])


@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    list_display = ('name', 'measurement_unit',)
    list_filter = ('name',)


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'color', 'slug',)


@admin.register(ShoppingCart)
class ShoppingCartAdmin(admin.ModelAdmin):
    list_display = ('user', 'recipe',)


@admin.register(Favourite)
class FavouriteAdmin(admin.ModelAdmin):
    list_display = ('user', 'recipe',)
