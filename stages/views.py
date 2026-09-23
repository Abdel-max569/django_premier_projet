from django.shortcuts import render

from .models import Entreprise

def liste_entreprises(request):
    return render(
        request,
        "stages/liste_entreprises.html",
        {"entreprises": Entreprise.objects.all()},
    )
