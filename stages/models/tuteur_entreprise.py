from django.db import models

from .personne import Personne

from .entreprise import Entreprise

class TuteurEntreprise(Personne):
    pass
    entreprise = models.ForeignKey(
        Entreprise, 
        related_name="entreprise",
        on_delete=models.CASCADE
    )
    

    
    
    
    