from django.db import models
# from .tuteur_entreprise import TuteurEntreprise
class Entreprise(models.Model):
    
    nom = models.CharField(max_length=120 , unique=True)
    ville = models.CharField(max_length=80)
    secteur  = models.CharField(max_length=80)
    contact = models.EmailField()
    
    # tuteur_entreprises = models.ForeignKey(
    #     TuteurEntreprise,
    #     related_name="entreprise",
    #     on_delete=models.PROTECT
        
    # )

    class Meta:
        ordering= ["nom"]
        verbose_name = "entreprise"
        verbose_name_plural = "entreprises"

    def __str__(self):
        return f"{self.nom} ({self.ville})"
     