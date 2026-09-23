from django.db import models

class Entreprise(models.Model):
    
    nom = models.CharField(max_length=120 , unique=True)
    ville = models.CharField(max_length=80)
    secteur  = models.CharField(max_length=80)
    contact = models.EmailField()

    class Meta:
        ordering= ["nom"]
        verbose_name = "entreprise"
        verbose_name_plural = "entreprises"

    def __str__(self):
        return f"{self.nom} ({self.ville})"
     