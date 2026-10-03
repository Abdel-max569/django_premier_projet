# peuplement.py
import datetime
from stages.models import (
    Competence, EnseignantReferent, Entreprise, 
    Etudiant, Offre, TuteurEntreprise, Stage, Candidature
)

print("Début du peuplement...")

# 1. Cinq compétences via votre classe TextChoices
c_python, _ = Competence.objects.get_or_create(libelle=Competence.ListeCompetences.PYTHON)
c_django, _ = Competence.objects.get_or_create(libelle=Competence.ListeCompetences.DJANGO)
c_sql, _ = Competence.objects.get_or_create(libelle=Competence.ListeCompetences.SQL)
c_js, _ = Competence.objects.get_or_create(libelle=Competence.ListeCompetences.JAVASCRIPT)
c_html, _ = Competence.objects.get_or_create(libelle=Competence.ListeCompetences.HTML_CSS)

ent1, _ = Entreprise.objects.get_or_create(nom="Alpha Tech", ville="Sokodé", secteur="Informatique", contact="contact@alpha.tg")
ent2, _ = Entreprise.objects.get_or_create(nom="Sokodé Digital", ville="Sokodé", secteur="Réseau", contact="info@sokodedigital.tg")
ent3, _ = Entreprise.objects.get_or_create(nom="Lomé Software", ville="Lomé", secteur="Développement", contact="rh@lomesoft.tg")


tut1, _ = TuteurEntreprise.objects.get_or_create(nom="Ouro", prenom="Salif", date_naissance="1985-05-12", email="salif@alpha.tg", sexe="H", entreprise=ent1)
tut2, _ = TuteurEntreprise.objects.get_or_create(nom="Tchagnao", prenom="Ali", date_naissance="1990-11-20", email="ali@sokodedigital.tg", sexe="H", entreprise=ent2)


ens1, _ = EnseignantReferent.objects.get_or_create(nom="Koffi", prenom="Jean", date_naissance="1978-04-02", email="jean.koffi@ifnti.tg", sexe="H")
ens2, _ = EnseignantReferent.objects.get_or_create(nom="Amavi", prenom="Eya", date_naissance="1983-09-15", email="eya.amavi@ifnti.tg", sexe="F")


et1, _ = Etudiant.objects.get_or_create(nom="Traoré", prenom="Abdel", date_naissance="2003-01-10", email="abdel@etudiant.ifnti.tg", sexe="H", matricule="IFNTI202301", promotion="2023-2026")
et2, _ = Etudiant.objects.get_or_create(nom="Mensa", prenom="Abla", date_naissance="2004-06-15", email="abla@etudiant.ifnti.tg", sexe="F", matricule="IFNTI202302", promotion="2023-2026")
et3, _ = Etudiant.objects.get_or_create(nom="Ayeva", prenom="Fousséni", date_naissance="2002-03-22", email="fousseni@etudiant.ifnti.tg", sexe="H", matricule="IFNTI202303", promotion="2023-2026")
et4, _ = Etudiant.objects.get_or_create(nom="Gado", prenom="Rita", date_naissance="2003-08-05", email="rita@etudiant.ifnti.tg", sexe="F", matricule="IFNTI202304", promotion="2023-2026")
et5, _ = Etudiant.objects.get_or_create(nom="Diallo", prenom="Moussa", date_naissance="2002-12-30", email="moussa@etudiant.ifnti.tg", sexe="H", matricule="IFNTI202305", promotion="2023-2026")


et1.competences.add(c_python, c_django)
et2.competences.add(c_html, c_js)
et3.competences.add(c_sql, c_python)
et4.competences.add(c_django, c_sql)
et5.competences.add(c_python, c_js)

# 6. Trois offres d'emploi avec compétences associées
off1, _ = Offre.objects.get_or_create(titre="Stage Développeur Python", description="Mission Django à Sokodé", entreprise=ent1)
off1.competences.add(c_python, c_django)

off2, _ = Offre.objects.get_or_create(titre="Administrateur Base de Données", description="Optimisation SQL", entreprise=ent2)
off2.competences.add(c_sql)

off3, _ = Offre.objects.get_or_create(titre="Intégrateur Web Front-End", description="Création d'interfaces modernes", entreprise=ent3)
off3.competences.add(c_html, c_js)

# 7. Six candidatures aux statuts variés (en utilisant vos choix de statut)
cand1, _ = Candidature.objects.get_or_create(etudiant=et1, offre=off1, date_debut="2026-02-01", date_fin="2026-05-01", nb_place=1, date_depot="2026-01-05", statut="RETENUE")
cand2, _ = Candidature.objects.get_or_create(etudiant=et2, offre=off1, date_debut="2026-02-01", date_fin="2026-05-01", nb_place=1, date_depot="2026-01-06", statut="REFUSEE")
cand3, _ = Candidature.objects.get_or_create(etudiant=et3, offre=off2, date_debut="2026-03-01", date_fin="2026-06-01", nb_place=1, date_depot="2026-01-10", statut="RETENUE")
cand4, _ = Candidature.objects.get_or_create(etudiant=et4, offre=off2, date_debut="2026-03-01", date_fin="2026-06-01", nb_place=1, date_depot="2026-01-12", statut="EN_COURS")
cand5, _ = Candidature.objects.get_or_create(etudiant=et5, offre=off3, date_debut="2026-04-01", date_fin="2026-07-01", nb_place=1, date_depot="2026-01-15", statut="EN_COURS")
cand6, _ = Candidature.objects.get_or_create(etudiant=et1, offre=off3, date_debut="2026-04-01", date_fin="2026-07-01", nb_place=1, date_depot="2026-01-16", statut="ANNULEE")

# 8. Deux stages issus de candidatures retenues cohérentes
# (Le tuteur tut1 bosse chez ent1 qui possède off1 / Le tuteur tut2 bosse chez ent2 qui possède off2)
Stage.objects.get_or_create(sujet="Développement d'un module ERP", enseignant_referent=ens1, tuteur_entreprise=tut1, candidature=cand1)
Stage.objects.get_or_create(sujet="Audit et indexation SQL", enseignant_referent=ens2, tuteur_entreprise=tut2, candidature=cand3)

print("Peuplement terminé avec succès !")
