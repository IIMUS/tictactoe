'''
IA.py
Julien Corriveau-Trudel
27 nov 2017
'''

CONST_NB_COLONNES = 3;
CONST_NB_LIGNES =3;

def afficher_tableau(tableau, nb_lignes, nb_colonnes):
    "Affichage du tableau"
    text = "";
    for i in range (0,nb_lignes):
        for j in range (0,nb_colonnes):
            if j is not 0:
                text = text + '|'
            text = text[0:len(text)] + tableau[3*(i)+(j)]
        if i is not nb_lignes - 1:
            text= text + "\n" + "-----" + "\n"
    return text


Tableau = [ "X", "X", "O", "X", "X", "O", "X", "X", "O"];

print (afficher_tableau(Tableau, CONST_NB_LIGNES, CONST_NB_COLONNES))
