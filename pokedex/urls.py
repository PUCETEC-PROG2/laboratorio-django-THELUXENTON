from django.urls import path, include
from . import views
from oauth2_provider import urls as oauth2_urls

app_name = 'pokedex'

urlpatterns = [
    path("", views.index, name="index"),
    path("trainers/", views.trainer_list, name="trainer_list"),    
    path("add_trainer/", views.add_trainer, name="add_trainer"),
    path("trainer/<int:id>/", views.display_trainer, name="display_trainer"),
    path("edit_trainer/<int:id>/", views.edit_trainer, name="edit_trainer"),
    path("delete_trainer/<int:id>/", views.delete_trainer, name="delete_trainer"),
    path("<int:id>/", views.pokemon, name="pokemon"),
    path("add_pokemon/", views.add_pokemon, name="add_pokemon"),
    path("edit_pokemon/<int:pokemon_id>/", views.edit_pokemon, name="edit_pokemon"),
    path("delete_pokemon/<int:pokemon_id>/", views.delete_pokemon, name="delete_pokemon"),
    path("login/", views.CustomLoginView.as_view(), name="login"),
    path('o/', include((oauth2_urls, 'oauth2_provider'), namespace='oauth2_provider')),
]