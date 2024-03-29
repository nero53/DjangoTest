from django.shortcuts import render, redirect
from .models import *
# Create your views here.


def addRecipe(request):
    if request.method == "POST":
        data = request.POST
        recipe_name = data.get('recipe_name')
        recipe_desc = data.get('recipe_desc')
        recipe_image = request.FILES.get('recipe_image')

        Recipe.objects.create(
            recipe_name = recipe_name,
            recipe_desc = recipe_desc,
            recipe_image = recipe_image
        )

        return redirect('/addRecipe/')

    queryset = Recipe.objects.all()
    context = {'addRecipe' : queryset}

    return render(request, 'add_recipe.html', context)


def deleteRecipe(request, id):
    queryset = Recipe.objects.get(id = id)
    queryset.delete()
    return redirect('/addRecipe/')