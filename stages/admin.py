from django.contrib import admin
from django.db import models
from django.contrib.admin import ModelAdmin

from stages.models.etudiant import Etudiant
from stages.models.offre import Offre
from stages.models.stage import Stage

from .models import Entreprise
from stages.models.entreprise import Entreprise
from stages.models.competence import Competence
from stages.models.candidature import Candidature
from stages.models.enseignant_referent import EnseignantReferent
from stages.models.tuteur_entreprise import TuteurEntreprise

@admin.register(Entreprise)
class EntrepriseAdmin(admin.ModelAdmin):
    list_display= ["nom","ville","secteur"]
    search_fields = ["nom","ville"]
    
@admin.register(Etudiant)    
class EtudiantAdmin(admin.ModelAdmin):
    list_display= ["nom","prenom","sexe"]
    search_fields= ["nom","prenom","sexe"]


@admin.register(Competence)   
class CompetenceAdmin(admin.ModelAdmin):
    list_display = ["libelle"] 
    search_fields = ["libelle"] 
    
    
@admin.register(Candidature)   
class CandidatureAdmin(admin.ModelAdmin):
    list_display = ["date_debut","nb_place","date_depot","date_fin","statut"] 
    search_fields = ["date_debut","nb_place","date_depot","date_fin","statut"]

@admin.register(Offre)   
class OffreAdmin(admin.ModelAdmin):
    list_display = ["titre","description"] 
    search_fields = ["titre","description"] 
 
@admin.register(Stage)   
class StageAdmin(admin.ModelAdmin):
    list_display = ["sujet"] 
    search_fields = ["sujet"] 

@admin.register(EnseignantReferent)   
class EnseignantReferentAdmin(admin.ModelAdmin):
    list_display = ["nom","prenom","sexe"] 
    search_fields = ["nom","prenom","sexe"] 


@admin.register(TuteurEntreprise)   
class TuteurEntrepriseAdmin(admin.ModelAdmin):
    list_display = ["nom","prenom","sexe"] 
    search_fields = ["nom","prenom","sexe"] 
                                  