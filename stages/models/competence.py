from django.db import models
from .offre import Offre

class Competence(models.Model):
    class ListeCompetences(models.TextChoices):
        PYTHON = 'PYTHON', 'Python'
        DJANGO = 'DJANGO', 'Django'
        SQL = 'SQL', 'SQL'
        JAVASCRIPT = 'JS', 'JavaScript'
        HTML_CSS = 'HTML_CSS', 'HTML / CSS'

    libelle = models.CharField(
        max_length=100,
        choices= ListeCompetences,
    )
    
    offres = models.ManyToManyField(
                Offre,
                related_name="competences",
               )
   
    class Meta:
        ordering = ["libelle"]
        
        
        
    def __str__(self):
        return self.get_libelle_display()    

   