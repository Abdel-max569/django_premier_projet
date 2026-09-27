# Modèle Entreprise

### 1. Identifier une entreprise

On utilise le **nom et la ville** pour identifier une entreprise, car une même entreprise peut avoir plusieurs agences dans des villes différentes.

### 2. Adresse mail

On utilise **EmailField** pour l’adresse mail, car ce champ permet de vérifier que l’adresse saisie a un format correct.

### 3. Secteur d’activité

On utilise une **liste de secteurs prédéfinis**, car cela évite que les mêmes secteurs soient écrits de différentes façons.

Par exemple, on évite d’avoir « Informatique », « informatique » et « Info » pour parler du même secteur.

Le texte libre est plus simple au début, mais il peut créer des problèmes de recherche et de statistiques plus tard. La liste demande un peu plus de travail au début, mais permet de garder des données propres.

### 4. Affichage de l’entreprise

On utilise la méthode **`__str__()`**, car elle permet d'afficher directement le nom de l’entreprise et sa ville lorsqu’on affiche l’objet, sans devoir cliquer dessus.

# Réponses 3.2

### a. La contrainte qui empêche les doublons

La contrainte `UNIQUE` sur le champ `nom` empêche les doublons.

### b. La colonne ajoutée automatiquement

La colonne `id` est ajoutée automatiquement par Django comme clé primaire.

### c. Modification de `max_length`

Après une modification de `max_length`, `makemigrations` crée un nouveau fichier de migration(0002_alter_entreprise_nom.py).

Pour revenir en arrière, il faut supprimer cette migration si elle n’est pas encore appliquée, ou revenir à la migration précédente avec `migrate`.


# Reponse 4 

### a. L’erreur apparaît au moment de valider le formulaire, lorsque Django essaie d’enregistrer l’entreprise avec un nom qui existe déjà

### b. Oui le message sera clair pour la secretaire si elle comprend l'anglais 

# Reponse 5 

### a. Quand on deplace on a une erreur de `TemplateDoesNotExist at /entreprises/` . Il liste les emplacement ou django a essayer de chercher ce template .ca nous permet de savoir on place t'on les templates en django. Cette liste permet de voir le dossier dans lequel Django attendait de trouver le fichier.


### b. Non cette page ne sera pas affiché normalement en ligne , cela depend de l'utilisation de l'attribut `DEBUG` dans le fichier `settings.py`. Si `DEBUG` est à `True`, la page d'erreur détaillée sera affichée. Si `DEBUG` est à `False`, une page d'erreur générique sera affichée à l'utilisateur final.

# Reponse 6
### a. c'esr le fichier db.sqlite3 qui n'ira pas sur github car c'est le fichier de base de données qui est généré automatiquement par Django. Il contient toutes les données de l'application et peut être volumineux. De plus, il peut contenir des informations sensibles ou privées, donc il est préférable de ne pas le partager publiquement.

### b. Les deux fichiers engendrer par uv qui seront commités sont project.toml et uv.lock. Le fichier `project.toml` contient les informations sur le projet et ses dépendances, tandis que le fichier `uv.lock` contient les versions exactes des dépendances installées. Ces fichiers sont nécessaires pour reproduire l'environnement de développement et garantir que l'application fonctionne correctement sur d'autres machines.