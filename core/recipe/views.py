from django.shortcuts import render

# Create your views here.


def addRecipe(request):
    return render(request, 'add_recipe.html')