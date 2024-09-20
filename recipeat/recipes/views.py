from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, Http404
from django.template import loader

from .models import Recipe, Ingredient, Instruction
from .forms import RecipeURLForm
from .utils.recipe_scraper import RecipeScraper

from django.views.generic.edit import CreateView
from recipes.forms import *


def index(request):
    latest_recipe_list = Recipe.objects.all()
    context = {"latest_recipe_list": latest_recipe_list}
    return render(request, "recipes/index.html", context)

def detail(request, recipe_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    instructions = recipe.instruction_set.all()
    ingredients = recipe.ingredient_set.all()
    return render(request, "recipes/detail.html", {
        "recipe": recipe,
        "ingredients": ingredients,
        "instructions": instructions
    })


def submit(request, recipe_id):
    return HttpResponse("You're voting on recipe %s." % recipe_id)

# class RecipeCreate(CreateView):
#     model = Recipe
#     form_class = RecipeCreateForm
#     template_name = 'recipes/submit_recipe_form.html'
#     success_url = '../recipe'


def submit_recipe(request):
    if request.method == 'POST':
        form = RecipeURLForm(request.POST)
        if form.is_valid():
            recipe_url = form.cleaned_data['recipe_url']
            try:
                # Use RecipeScraper to get the recipe details
                scraper = RecipeScraper(recipe_url)
                parsed_ingredients = scraper.parsed_ingredients()
                instructions = scraper.instructions_list()

                # Save the scraped data to the database
                recipe = Recipe.objects.create(
                    title=scraper.title(),
                    yields=scraper.yields(),
                    total_time=scraper.total_time(),
                    image=scraper.image(),
                )

                # Save each ingredient as a separate object
                for idx, ingredient in enumerate(parsed_ingredients, start=1):
                    units = []
                    for amount in ingredient.amount:
                        units.append(str(amount.unit))
                    Ingredient.objects.create(
                        recipe=recipe,
                        comment = ingredient.comment if ingredient.comment else '',
                        name = ingredient.name.text,
                        preparation = ingredient.preparation if ingredient.preparation else '',
                        purpose = ingredient.purpose if ingredient.purpose else '',
                        quantity = ingredient.amount[0].quantity,
                        quantity_max = ingredient.amount[0].quantity,
                        sentence = ingredient.sentence,
                        size = ingredient.size if ingredient.size else '',
                        unit = ingredient.amount[0].unit,
                        unit_text = ' '.join(units)
                    )

                # Save each instruction as a separate object
                for idx, instruction in enumerate(instructions, start=1):
                    Instruction.objects.create(
                        recipe=recipe,
                        step=idx,
                        text=instruction
                    )

                return redirect('recipe_success')  # Redirect to a success page or recipe detail page

            except Exception as e:
                form.add_error('recipe_url', f"Error scraping the recipe: {str(e)}")

    else:
        form = RecipeURLForm()

    return render(request, 'recipes/submit_recipe.html', {'form': form})

# views.py
def recipe_success(request):
    return render(request, 'recipes/recipe_success.html')

