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

`count()` demande le décompte à la base de données et ne construit pas les
objets `Candidature`. La base actuelle enregistre le statut sous la valeur
`"RETENUE"` (en majuscules).

5. Stages dont l'offre vient d'une entreprise située à Sokodé :

```python
Stage.objects.filter(candidature__offre__entreprise__ville="Sokodé")
```

6. Offres qui demandent au moins une compétence possédée par l'étudiant :

```python
Offre.objects.filter(competences__etudiants=etudiant).distinct()
```
