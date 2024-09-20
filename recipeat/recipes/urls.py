from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
     # ex: /recipes/5/
    path("<int:recipe_id>/", views.detail, name="detail"),
    # ex: /recipes/5/submit/
    path("<int:recipe_id>/submit/", views.submit, name="submit"),
    path('submit-recipe/', views.submit_recipe, name='submit_recipe'),
    path('recipe-success/', views.recipe_success , name='recipe_success'),  # Add your success view here
]