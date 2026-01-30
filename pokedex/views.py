from django.http import HttpResponse
from django.template import loader
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
# Asegúrate de importar ambos forms
from .forms import PokemonForm, EntrenadorForm 
from .models import Pokemon, Trainer

# --- Vistas Públicas (Cualquiera puede ver) ---

def index(request):
    pokemons = Pokemon.objects.all()
    trainers = Trainer.objects.all()
    template = loader.get_template('index.html')
    context = {
        'pokemons': pokemons,
        'trainers': trainers,
    }
    return HttpResponse(template.render(context, request))

def pokemon(request, id):
    # Usamos get_object_or_404 es más seguro que .get() por si el ID no existe
    pokemon = get_object_or_404(Pokemon, id=id) 
    template = loader.get_template('display_pokemon.html')
    context = {
        'pokemon': pokemon
    }
    return HttpResponse(template.render(context, request))

def trainer_list(request):
    trainers = Trainer.objects.all() 
    return render(request, 'trainer_list.html', {'trainers': trainers})

def display_trainer(request, id):
    trainer = get_object_or_404(Trainer, id=id)
    template = loader.get_template('display_trainer.html')
    context = {
        'trainer': trainer
    }
    return HttpResponse(template.render(context, request))

# --- Vistas Privadas (Requieren Login) ---

@login_required
def add_pokemon(request):
    if request.method == 'POST':
        form = PokemonForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('pokedex:index')
    else:
        form = PokemonForm()
    
    return render(request, 'pokemon_form.html', {'form': form})

@login_required
def edit_pokemon(request, pokemon_id):
    pokemon = get_object_or_404(Pokemon, pk=pokemon_id)
    if request.method == 'POST':
        form = PokemonForm(request.POST, request.FILES, instance=pokemon)
        if form.is_valid():
            form.save()
            return redirect('pokedex:index')
    else:
        form = PokemonForm(instance=pokemon)
    return render(request, 'pokemon_form.html', {'form': form})

@login_required
def delete_pokemon(request, pokemon_id):
    pokemon = get_object_or_404(Pokemon, pk=pokemon_id)
    pokemon.delete()
    return redirect('pokedex:index')


@login_required
def add_trainer(request):
    if request.method == "POST":
        form = EntrenadorForm(request.POST) 
        if form.is_valid():
            form.save()
            return redirect('pokedex:trainer_list') 
    else:
        form = EntrenadorForm()
    return render(request, 'trainer_form.html', {'form': form})

# --- NUEVAS VISTAS AGREGADAS PARA EDITAR Y ELIMINAR ENTRENADORES ---

@login_required
def edit_trainer(request, id):
    trainer = get_object_or_404(Trainer, pk=id)
    if request.method == 'POST':
        form = EntrenadorForm(request.POST, instance=trainer)
        if form.is_valid():
            form.save()
            return redirect('pokedex:trainer_list')
    else:
        form = EntrenadorForm(instance=trainer)
    return render(request, 'trainer_form.html', {'form': form})

@login_required
def delete_trainer(request, id):
    trainer = get_object_or_404(Trainer, pk=id)
    trainer.delete()
    return redirect('pokedex:trainer_list')

class CustomLoginView(LoginView):
    template_name = 'login_form.html'