from django.contrib import admin
from django.db import models

from .models import Entreprise
from stages.models.entreprise import Entreprise

@admin.register(Entreprise)

class EntrepriseAdmin(admin.ModelAdmin):
    list_display= ["nom","ville","secteur"]
    search_fields = ["nom","ville"]