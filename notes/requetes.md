# Requêtes ORM Django

1. Offres des entreprises situées à Sokodé :

```python
Offre.objects.filter(entreprise__ville="Sokodé")
```

2. Étudiants qui possèdent la compétence « Django » :

```python
Etudiant.objects.filter(
	competences__libelle=Competence.ListeCompetences.DJANGO
).distinct()
```

3. Candidatures d'un étudiant, à partir de l'objet étudiant :

```python
etudiant.candidature.all()
```

4. Nombre de candidatures retenues, sans charger les candidatures en mémoire :

```python
Candidature.objects.filter(statut="RETENUE").count()
```

5. Stages dont l'offre vient d'une entreprise située à Sokodé :

```python
Stage.objects.filter(candidature__offre__entreprise__ville="Sokodé")
```

6. Offres qui demandent au moins une compétence possédée par l'étudiant :

```python
Offre.objects.filter(competences__etudiants=etudiant).distinct()
```

# 6

### a)

```python
offre_vide = Offre.objects.create(
    titre="",
    description="Test de titre vide"
)
print(f"2. Offre avec titre vide créée avec l'ID : {offre_vide.id}")

```

### b)

```python
from datetime import date

offre = Offre.objects.first()
etudiant = Etudiant.objects.first()

c1 = Candidature.objects.create(
    etudiant=etudiant,
    offre=offre,
    date_debut=date(2026, 11, 1),
    date_fin=date(2026, 12, 1),
    date_depot=date(2026, 10, 5),
    nb_place=1,
    statut=Candidature.Statut.DEPOSE
)

c2 = Candidature.objects.create(
	etudiant=etudiant,
	offre=offre,
	date_debut=date(2026, 11, 1),
	date_fin=date(2026, 12, 1),
	date_depot=date(2026, 10, 5),
	nb_place=1,
	statut=Candidature.Statut.DEPOSE
)

```
## 1)

a. Que se passe-t-il ?
1. Dates inversées : La création réussit. La base accepte car les dates existent, même si l'ordre est illogique.
2. Titre vide : La création réussit. La base accepte le texte vide "" car ce n'est pas une valeur nulle (NULL).
3. Double candidature : La création échoue (IntegrityError). la contrainte UniqueConstraint bloque le doublon en base.


## 2)

b. Problème et responsabilités
• Le problème commun (1 et 2) : L'absence de validation logique. Les données sont correctes techniquement, mais fausses pour l'application.
• Qui doit refuser ?
	• Dates et Titre vide : Le Modèle. La base ne comprend pas les règles logiques. C'est au modèle Django de bloquer cela .
	• Double candidature : La Base de données. C'est un problème d'unicité pure. 