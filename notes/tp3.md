# TP — Vues, URLs, templates

## 4.1. Compter les requêtes

### a)
 Nombre de requete : Sans optimisation, il y a 7 requêtes pour 3 offres. <br> La formule est 2N + 1 (où N est le nombre d'offres en base). <br> C'est ce qu'on appelle le problème du N+1 requêtes.

### b)
  Il contient la dernière requête SQL exécutée, qui est un SELECT récupérant les compétences de l'offre <br>  Cela prouve que l'ORM de Django est paresseux (lazy). Il n'exécute la requête SQL pour récupérer les compétences qu'au moment précis où on écrit list(offre.competences.all()), et non pas au début .

### c)
<br> • Avec 200 offres : (2 × 200) + 1 = 401 requêtes. <br> • Avec 2000 offres : (2 × 2000) + 1 = 4001 requêtes.

## 4.2 La correction

#### Tableau comparatif :



| Approche | Comportement et Nombre de requêtes SQL |
| :--- | :--- |
| **Sans rien** | **7 requêtes** : 1 pour l'objet principal, puis 1 par relation accédée. À éviter pour les listes. |
| **Avec `select_related`** | **4 requêtes** : Réalise une jointure SQL (`JOIN`). Idéal pour `ForeignKey` et `OneToOne`. |
| **Avec les deux combinés** | **2 requêtes** : 1 requête jointe (objet + ForeignKey) et 1 requête séparée pour le ManyToMany. |



d. Pourquoi faut-il deux outils différents ?

Il faut deux outils car la page suit deux types de relations radicalement différentes :
• Une relation simple (vers 1 seul objet) : comme une ForeignKey. Django utilise select_related pour faire une jointure SQL (JOIN) et tout ramener en une seule fois.
• Une relation multiple (vers une liste d'objets) : comme un ManyToMany. Faire un JOIN SQL ici dupliquerait inutilement les lignes en base de données. Django utilise donc prefetch_related pour faire une requête à part et assembler les données en mémoire.



e. Pourquoi ajouter une requête est quand même un gain ?

Parce que sans prefetch_related, Django fait 1 requête par ligne affichée (problème du N+1). Si on a 5 lignes, il fait 5 requêtes.
Avec prefetch_related, il ne fait qu'une seule requête supplémentaire au total, peu importe le nombre de lignes. C'est un gain immense car le nombre de requêtes devient fixe.

## 5. Une panne à diagnostiquer

### a) 
Nom de l'erreur :  NoReverseMatch  <br> Ca apparait au chargement de la page 

### b)

b. Comparaison avec une adresse écrite en dur

• Si l'adresse avait été écrite en dur  : La page se chargerait normalement sans aucune erreur. Le problème ne surviendrait qu'au clic sur le lien, qui renverrait alors une erreur 404 Page Not Found.
• Quelle erreur préférer et pourquoi ?
Il vaut mieux découvrir l'erreur NoReverseMatch (via le tag {% url %}).Pourquoi ? Parce qu'elle est immédiate et "bruyante". L'affichage de la page plante tout de suite en mode développement, ce qui nous oblige à réparer le bug immédiatement. Avec une adresse en dur, le bug est "silencieux" : la page s'affiche bien, et nous risquez d'envoyer en production un lien mort (erreur 404) sans nous en rendre compte, à moins de cliquer manuellement sur chaque lien pour les tester.


### 4.3 Le piège

**Oui** elle souffre du même défaut  

**Correction**


```python
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
```