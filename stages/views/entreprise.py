from django.shortcuts import get_object_or_404, render

from stages.models.offre import Offre
from django.db.models import Prefetch
from stages.models import Entreprise
from ..models import Entreprise

def liste_entreprises(request):
    return render(
        request,
        "stages/entreprises/liste_entreprises.html",
        {"entreprises": Entreprise.objects.all()},
    )
    
    
# def detail_entreprise(request, entreprise_id):
#     return render(
#         request,
#         "stages/entreprises/detail_entreprise.html",
#         {"entreprise": get_object_or_404(Entreprise , pk=entreprise_id)},
#     )    




def detail_entreprise(request, entreprise_id):
    return render(
        request,
        "stages/entreprises/detail_entreprise.html",
        {
            "entreprise": get_object_or_404(
                Entreprise.objects.prefetch_related(
                    Prefetch("offres", queryset=Offre.objects.prefetch_related("competences"))
                ),
                pk=entreprise_id
            )
        },
    )
