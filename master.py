'''
master.py
Emrick St-Pierre
21/11/2017
'''

from fonctions import input_clavier
from partie import Partie

#C'est ici que le jeu de tic tac toe doit etre code

# definitions fonctions

def loop_jouer(_nom_joueur1, _nom_joueur2):
    while(True):
        try:
            c = input("Voulez-vous jouer une partie? Oui:1 Non:0 ")
            if(c == 1):
                Partie(_nom_joueur1, _nom_joueur2).jouer()
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

#main

loop_jouer("joueur 1", "joueur 2")

'''
Note: les commentaires ne doivent pas contenir de
caracteres en dehors du code ASCII standard, donc
pas d'accents
'''
