from django.urls import path

from stages.views import home, offres 

from .views import entreprise

app_name = "stages"
urlpatterns = [
    path ('',home.home,
                name="home"),
    
    path ('entreprises/',entreprise.liste_entreprises,
            name="liste_entreprises"),
    
    path('entreprises/<int:entreprise_id>', entreprise.detail_entreprise, name="detail_entreprise"),
    
    path('offres/', offres.liste_offres, name="liste_offres"),
    
    path('offres/<int:offre_id>', offres.show_offer, name="detail_offre"),
]

