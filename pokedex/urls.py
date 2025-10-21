from django.urls import path
from pokedex import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:id>/", views.pokemon, name="pokemon"),
    path("trainer/<int:id>/", views.display_trainer, name="display_trainer"),
]
