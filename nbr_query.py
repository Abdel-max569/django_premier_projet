from django.db import connection, reset_queries
from stages.models import Offre
##offre = Offre.objects.all()   
offres_optimisees = Offre.objects.select_related("entreprise").prefetch_related("competences")
reset_queries()
for offre in offres_optimisees:
    len(connection.queries)
    offre.entreprise.nom
    len(connection.queries)
    list(offre.competences.all())
    len(connection.queries)
    print(connection.queries[-1])

