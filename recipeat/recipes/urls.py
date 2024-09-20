from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
     # ex: /recipes/5/
    path("<int:recipe_id>/", views.detail, name="detail"),
    # ex: /recipes/5/results/
    path("<int:recipe_id>/results/", views.results, name="results"),
    # ex: /recipes/5/submit/
    path("<int:recipe_id>/submit/", views.submit, name="submit"),
]