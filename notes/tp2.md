# Modélisation du domaine

## 1. Un modèle par fichier
#### a) Qaund on lance ``uv run manage.py makemigrations`` , Django nous repond ``No changes detected`` . Django identifie un modele de maniere unique par la composition du nom de l'application oû le modele se trouve(app_label) et le nom de la classe .  Ce que j'apprend sur ce qu'une migration est qu'une migration est une representation de la base de données a un instant T 



/*
Personne doit-elle avoir sa propre table ? La responsable demande-t-elle jamais « toutes
les personnes », sans distinction ?
— Le tuteur appartient-il à une entreprise, ou seulement au stage qu’il encadre ?
— Une candidature peut-elle donner lieu à deux stages ? Un stage peut-il exister sans candi-
dature ? Quel champ l’interdit, et à quel niveau : Python, ou la base elle-même ?


— « Jamais deux fois à la même offre » : comment le garantir, et qui le vérifie ?
— La promotion : un nombre ou un texte ? Pensez à la statistique que l’IFNTI voudra un
jour : le taux de placement par promotion.
— Le statut d’une candidature : du texte libre, ou une liste fermée ? Que coûte chaque choix
le jour où une faute de frappe s’y glisse ?
— Pour chaque relation, que se passe-t-il à la suppression ? Relisez la dernière phrase
de la responsable avant de répondre.
**/


## 2.
### a) Non Personne ne va pas avoir de table dans la base de données car c'est une classe abstraite. On ne va jamais faire une requete pour recuperer toutes les personnes. On va toujours faire des requetes pour recuperer des etudiants, des tuteurs ou des responsables 

### b) Le tuteur appartient à une entreprise, il n'appartient pas au stage qu'il encadre. Il est donc logique de mettre un champ entreprise dans le modele TuteurEntreprise.

### c) Non une candidature ne ne peut pas donner lieu a  deux stages . Non un stage ne peut pas exister sans candidature , il faut candidater d'abord 

### d) Pour eviter personne beneficie 2 fois la mème offre , il faut cree une clé composé constituer de offre et l'etudiant dans la table candidature  

### e) L'attribut promotion doit etre de type enumeration de chaine (texte) deja defini selon lesquel l'entreprise dispose (liste fermée)

### f) Le statu de la candidature doit etre une liste fermée , car le statu ne changera pas ou n'augmentera pas , donc pour eviter que les gens mettent les valeur qu'ils veulent , il faut opter pour une liste fermée 

### g) Pour chaque relation la suppression est refusé  tant qu'elle contient des relations qui sont rattaché a elle , donc on utilise PROTECT


## 3.

### a) Mes migrations ont crée au total 10 tables . Ceux qui correspondent au modele sont : stages_etudiant_competences  et stages_competence_offres . Ces deux tables viennent de l'association de certaines tables 

### b) Non il ya pas la table personne dans la base de données , car personne est une classe abstraite et on ne peut pas instancier une classe abstraite .Oui c'est cohérent avec mon choix de la partie 2

### c) La regle "jamais deux fois à la même offre" apparait dans le SQL sous forme de contrainte d'unicité sur les champs offre et etudiant dans la table candidature

### d) Dans le SQL on peut voir que les regles de suppression sont appliqué par Django , et si on supprime une ligne directement en SQL sans passer par Django , les regles de suppression ne seront pas appliqué et on risque d'avoir des incoherences dans la base de données. 

Déclarez tous vos modèles dans stages/admin.py. Pour chacun, choisissez les deux ou trois
colonnes qui permettent à la responsable de s’y retrouver dans la liste — pas plus.
Puis, dans l’admin, essayez de supprimer une entreprise qui a publié au moins une offre.
a. Que se passe-t-il ? Est-ce ce que la responsable voulait ?
b. Si vous aviez choisi l’autre comportement, qu’aurait aﬀiché l’admin, et qu’aurait-il supprimé ?

## 4.
### a) La suppression de l'élément Entreprise est impossible car les objets suivants y sont liés , Oui c'est ce que la responsable voulait 

### b) • Avec CASCADE : L'admin affiche une alerte rouge. Il supprime l'entreprise ET supprime définitivement toutes ses offres . <br> • Avec SET_NULL : L'admin affiche une confirmation. Il supprime l'entreprise, mais garde les offres en effaçant le nom de l'entreprise (elles deviennent anonymes)

## 5.
