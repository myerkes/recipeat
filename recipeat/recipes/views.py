from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from django.template import loader

from .models import Recipe, Ingredient, Instruction


def index(request):
    latest_recipe_list = Recipe.objects.all()
    context = {"latest_recipe_list": latest_recipe_list}
    return render(request, "recipes/index.html", context)

def detail(request, recipe_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    return render(request, "recipes/detail.html", {"recipe": recipe})


def results(request, recipe_id):
    response = "You're looking at the results of recipe %s."
    return HttpResponse(response % recipe_id)


def submit(request, recipe_id):
    return HttpResponse("You're voting on recipe %s." % recipe_id)