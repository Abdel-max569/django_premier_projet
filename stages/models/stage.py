from django.db import models

from .enseignant_referent import EnseignantReferent
from .tuteur_entreprise import TuteurEntreprise

class Stage(models.Model):    
    sujet = models.TextField(max_length=255)
    enseignant_referent = models.ForeignKey(
        EnseignantReferent,
        related_name="stages",
        on_delete=models.PROTECT
        
    )
    
    tuteur_entreprise = models.ForeignKey(
            TuteurEntreprise,
            related_name="stages",
            on_delete=models.PROTECT
            
        )
  
   

   