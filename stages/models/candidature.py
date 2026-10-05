
from django.db import models


from .offre import Offre
from .etudiant import Etudiant

class Candidature(models.Model):
    
    class Statut(models.TextChoices) :
        DEPOSE = "depose", "DEPOSE" 
        RETENUE = "retenue" , "RETENUE"
        REFUSE = "refuse" , "REFUSE"
            
        
    etudiant = models.ForeignKey(
        Etudiant,
        related_name="candidature",
        on_delete=models.PROTECT
    )
        
    date_debut = models.DateField()
    date_fin = models.DateField()
    nb_place = models.PositiveIntegerField()
    date_depot = models.DateField()
    statut = models.CharField(choices=Statut)
    
    offre = models.ForeignKey(
        Offre,
        related_name="candidatures",
        on_delete=models.CASCADE
    )
   
    class Meta:
        ordering = ["date_debut"]
        constraints = [models.UniqueConstraint(
            fields = ["offre","etudiant"],
            name="offre_etudiant"
        )] 

   