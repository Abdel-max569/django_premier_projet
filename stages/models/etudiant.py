from django.db import models
from .competence import Competence

class Etudiant(models.Model):
    matricule = models.CharField(max_length=50)
    promotion = models.CharField(max_length=30)
    
    competences = models.ManyToManyField(
                                    Competence,
                                    related_name = "etudiants",
                )

    class Meta:
        ordering = ["promotion"]

    def __str__(self):
        return f"{self.matricule}-{self.promotion }"