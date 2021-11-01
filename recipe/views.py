from django.http import HttpResponse
from django.shortcuts import render
from .models import Recipe, RecipeName, RecipeIngredient, Direction, Cookware, RecipeCookware, Image, CookTime, ServingSize, Ingredient
from django.views.generic import View
from .forms import RecipeForm
from django.forms import widgets

# Create your views here.
class recipe_view(View):    
    
    def get(self, request):
        form = RecipeForm()
        return render(request, "home.html", {'form': form})

    def post(self, request):
        form = RecipeForm(request.POST)
        if form.is_valid():
            tex = form.cleaned_data['recipename'].id
            recipes = Recipe.objects.filter(recipename_id=tex).values('id', 'category__category', 'subcategory__subcategory', 'recipename__recipename', 'image', 'description')
            ingredients = RecipeIngredient.objects.filter(recipe__in=recipes.values('id'))
            directions = Direction.objects.filter(recipe__in=recipes.values('id'))
            cookwares = RecipeCookware.objects.filter(recipe__in=recipes.values('id'))
            cooktimes = CookTime.objects.filter(recipe__in=recipes.values('id'))
            servingsizes = ServingSize.objects.filter(recipe__in=recipes.values('id'))
        args = {'form': form, 'ingredients': ingredients, 'servingsizes': servingsizes, 'cooktimes': cooktimes, 'recipes': recipes, 'directions': directions, 'cookwares': cookwares}
        return render(request, "home.html", args)