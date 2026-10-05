from django.shortcuts import render
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

