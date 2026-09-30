from django.db import models

from .entreprise import Entreprise

class TuteurEntreprise(models.Model):
    pass
    entreprise = models.ForeignKey(
        Entreprise, 
        related_name="entreprise",
        on_delete=models.CASCADE
    )
    

    
    
    
    