from django.db import models

from .personne import Personne
from .competence import Competence

class Etudiant(Personne):
    matricule = models.CharField(max_length=50)
    promotion = models.CharField(max_length=30)
    
    competences = models.ManyToManyField(
                                    Competence,
                                    related_name = "etudiants",
                )

    class Meta:
        ordering = ["promotion"]

    def __str__(self):
        return f"{self.nom}-{self.prenom} ({self.matricule})"