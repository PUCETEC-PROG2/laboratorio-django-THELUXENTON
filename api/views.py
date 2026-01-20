from django.shortcuts import render
from rest_framework import viewsets
# Importamos explícitamente todos los permisos necesarios
from rest_framework.permissions import IsAuthenticated, AllowAny # <--- Añadido AllowAny
from oauth2_provider.contrib.rest_framework import (
    TokenHasReadWriteScope, 
    TokenHasScope, 
    OAuth2Authentication
)

from pokedex.models import Pokemon, Trainer
from .serializers import PokemonSerializer, EntrenadorSerializer


class PokemonViewSet(viewsets.ModelViewSet):
    queryset = Pokemon.objects.all()
    serializer_class = PokemonSerializer
    
    authentication_classes = [OAuth2Authentication]
    # No definimos permission_classes globalmente, lo manejamos en el método:
    required_scopes = ['write']  

    # Permisos para PokemonViewSet (Lectura abierta, Escritura con token)
    def get_permissions(self):
        # Para POST, PUT, PATCH, DELETE (modificación), exigimos autenticación
        if self.request.method in ['POST', 'PUT', 'PATCH', 'DELETE']:
            return [TokenHasScope(), IsAuthenticated()]
        
        # Para GET, HEAD, OPTIONS (lectura), permitimos a cualquiera
        return [AllowAny()] 


class EntrenadorViewSet(viewsets.ModelViewSet):
    queryset = Trainer.objects.all()
    serializer_class = EntrenadorSerializer
    authentication_classes = [OAuth2Authentication]
    required_scopes = ['write']

    # --- PARA PERMITIR VER LA LISTA SIN LOGIN ---
    def get_permissions(self):
        # Para escribir (POST, PUT, DELETE) pedimos login
        if self.request.method in ['POST', 'PUT', 'PATCH', 'DELETE']:
            return [TokenHasScope(), IsAuthenticated()]
        
        # Para leer (GET), dejamos pasar a cualquiera (AllowAny)
        return [AllowAny()]