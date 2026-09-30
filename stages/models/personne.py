from django.db import models

class Personne(models.Model):
    class Sexe(models.TextChoices):
        FEMME = 'F' , 'f'
        HOMME = 'H' , 'h'
    nom = models.CharField(max_length=30)
    prenom = models.CharField(max_length=30)
    date_naissance = models.DateField()
    email = models.EmailField()
    sexe = models.CharField(choices = Sexe)

    class Meta:
        ordering = ['nom','prenom']
        verbose_name = "Personne"
        verbose_name_plural = "Personnes"

    def __str__(self):
        return f"{self.nom}-{self.prenom }"

