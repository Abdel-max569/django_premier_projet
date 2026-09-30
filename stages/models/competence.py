from django.db import models
from .offre import Offre

class Competence(models.Model):
    libelle = models.CharField(max_length=100)
    offres = models.ManyToManyField(
                Offre,
                related_name="competences",
               )
   
    class Meta:
        ordering = ["libelle"]

   