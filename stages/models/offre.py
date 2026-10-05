from django.db import models

from .entreprise import Entreprise
from stages.models.entreprise import Entreprise

class Offre(models.Model):
    titre = models.CharField(max_length=100)
    description = models.TextField(max_length=400)
    
    # entreprise = models.ForeignKey(
    #     Entreprise,
    #     related_name="offres",
    #     on_delete= models.PROTECT
    # )
    date_debut = models.DateField()
    date_fin = models.DateField()
    nb_place = models.PositiveIntegerField()
    
    entreprise = models.ForeignKey('Entreprise',related_name="offres",on_delete=models.PROTECT, null=True, blank=True)

   
    class Meta:
        ordering = ["titre"]

   