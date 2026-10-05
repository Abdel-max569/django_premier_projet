from django.urls import path

from stages.views import offres 
from .views import entreprise

app_name = "stages"
urlpatterns = [
    path ('entreprises/',entreprise.liste_entreprises,
            name="liste_entreprises"),
    
    path('offres/', offres.liste_offres, name="liste_offres"),
    
    # path('offres/<int:offre_id>', offres.liste_offres, name="liste_offres"),
]

