from django.shortcuts import get_object_or_404, render
from django.http import HttpRequest

from ..models import Offre

def liste_offres(request:HttpRequest):
    return render(
        request,
        "stages/offres/liste_offres.html",
        {
            "offres": Offre.objects.select_related("entreprise")
                                    .prefetch_related("competences")
        }
        )


def show_offer(request:HttpRequest , offre_id:int):
    return render(
        request,
        "stages/offres/show_offer.html",
        {"offre":get_object_or_404(Offre,pk=offre_id)}
    )