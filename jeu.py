#jeu.py

#
from fonctions import input_clavier
from partie import Partie
from pgsql import Connexion
from pgsql import CONST_PG_TABLE_COMPTES, CONST_PG_ATTRIBUT_NOM_COMPTE, CONST_PG_ATTRIBUT_ID_COMPTE
from pgsql import CONST_PG_TABLE_PARTIES, CONST_PG_ATTRIBUT_ID_JOUEUR_1, CONST_PG_ATTRIBUT_ID_JOUEUR_2, CONST_PG_ATTRIBUT_ID_VAINQUEUR

# Definitions fonctions
def loop_jouer(_nom_joueur1, _nom_joueur2, _connexion):
    while(True):
        try:
            c = input("Voulez-vous jouer une partie? Oui:1 Non:0 ")
            if(c == 1):
                p = Partie(_nom_joueur1, _nom_joueur2)
                nom_vainqueur = p.jouer()
                id_joueur1 = find_id_compte(_connexion, _nom_joueur1)
                id_joueur2 = find_id_compte(_connexion, _nom_joueur2)
                print nom_vainqueur
                """Ajouter partie a l'historique des parties"""
                if(nom_vainqueur != 0):
                    print "---Ajout de la victoire de {0} a l'historique---".format(nom_vainqueur)
                    #_connexion.SQL_INSERT(CONST_PG_TABLE_PARTIES, (str(len(_connexion.SQL_SELECT("*", CONST_PG_TABLE_PARTIES)) + 1), id_joueur1, id_joueur2, id_vainqueur))
                    ajouter_partie_bd(_connexion, id_joueur1, id_joueur2, find_id_compte(_connexion, nom_vainqueur))
                else:
                    print "---Ajout de la partie nulle a l'historique---"
                    #_connexion.SQL_INSERT(CONST_PG_TABLE_PARTIES, (str(len(_connexion.SQL_SELECT("*", CONST_PG_TABLE_PARTIES)) + 1), id_joueur1, id_joueur2, 0))
                    ajouter_partie_bd(_connexion, id_joueur1, id_joueur2, 0)
                print "Merci d'avoir joue"
            if(c == 0):
                print "Au revoir"
                break
            if(c != 1 and c != 0):
                print "Entree invalide: {0}".format(c)
        except NameError as error:
            print "---NAME_ERROR LORS DE L'INSERTION---:", error
        except SyntaxError as error:
            print "---SYNTAX_ERROR LORS DE L'INSERTION---:", error

def ajouter_partie_bd(_connexion, _id_joueur1, _id_joueur2, _id_vainqueur):
    _connexion.SQL_INSERT(CONST_PG_TABLE_PARTIES, (str(len(_connexion.SQL_SELECT("*", CONST_PG_TABLE_PARTIES)) + 1), _id_joueur1, _id_joueur2, _id_vainqueur))

def ajouter_compte_bd(_nom):
    tmp_c = Connexion()
    tmp_c.SQL_INSERT(CONST_PG_TABLE_COMPTES, (str(len(tmp_c.SQL_SELECT("*", CONST_PG_TABLE_COMPTES)) + 1), _nom))
    return tmp_c

def get_liste_noms_bd():
    return Connexion().SQL_SELECT(CONST_PG_ATTRIBUT_NOM_COMPTE, CONST_PG_TABLE_COMPTES)

def check_nom_bd(_nom):
    if(("{0}".format(_nom),) in get_liste_noms_bd()):
        print _nom, "est dans la BD"
        return True
    else:
        print _nom, "n'est pas dans la BD"
        return False

def find_id_compte(_connexion, _nom_compte):
    liste_bd = tuple(_connexion.SQL_SELECT('*', CONST_PG_TABLE_COMPTES))

    for i in range(len(liste_bd)):
        if(liste_bd[i][1] == _nom_compte):
            return liste_bd[i][0]
    return False

def creer_compte():
    print "Creer compte"
    input_nom = input_clavier("Choisissez votre nom de joueur :")
    if(check_nom_bd(input_nom)):
        print "Echec creation compte"
        print "Nom {0} deja utilise".format(input_nom)
        return False
    if(type(input_nom) != str):
        print "Echec creation compte"
        print "Veuillez entrer un string"
        return False
    else:
        print "Creation compte reussie"
        #ajouter_nom_bd(input_nom)
        #return True
        return ajouter_compte_bd(input_nom)

def identifier_compte():
    print "Identifier compte"
    input_nom = input_clavier("Identifiez-vous avec votre nom de joueur pour pouvoir jouer : ")
    tmp_c = Connexion()
    liste_noms_bd = tmp_c.SQL_SELECT(CONST_PG_ATTRIBUT_NOM_COMPTE, CONST_PG_TABLE_COMPTES)
    if(("{0}".format(input_nom),) in liste_noms_bd):
        print  "Identification reussie"
        #print input_nom, "est dans la BD"
        return (tmp_c, input_nom)
    else:
        print "Echec identification"
        #print input_nom, "n'est pas dans la BD"
        return False

# Main
print "Bienvenue a Tic Tac Toe"
print "Connectez-vous ou creez un compte"
while(True):
    input_cc = input_clavier("0: S'identifier, 1: Creer un compte")
    if(input_cc != 1 and input_cc != 0):
        print "Veuillez entrer 0 ou 1"
    if(input_cc == 1):
        connexion = creer_compte()
        if(connexion != False):
            identifier_compte()
            break
    if(input_cc == 0):
        tmp_tup = identifier_compte()
        if(tmp_tup != False):
            connexion = tmp_tup[0]
            nom_compte_actif = tmp_tup[1]
            id_compte_actif = find_id_compte(connexion, nom_compte_actif)
            compte_actif = (id_compte_actif, nom_compte_actif)
            print "Compte actif: {0}".format(compte_actif)
            break



loop_jouer(nom_compte_actif, nom_compte_actif, connexion)


"""
Gestion de comptes utilisateurs sans mot de passe
Verifie si le nom d'utilisateur est dans le fichier
    Si non, cree l'utilisateur dans le fichier
envoie vers le menu de jeu

Gestion de comptes utilisateurs avec mot de passe

Gestion de scores, statistiques, classement
"""
