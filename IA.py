'''
IA.py
Julien Corriveau-Trudel
27 nov 2017
'''

CONST_NB_COLONNES = 3
CONST_NB_LIGNES = 3

def afficher_tableau(tableau):
    "Affichage du tableau"
    text = ""
    for lig in range(0, CONST_NB_LIGNES):
        for col in range(0, CONST_NB_COLONNES):
            if col is not 0:
                text = text + '|'
            text = text[0:len(text)] + tableau[3 * (lig) + (col)]
        if lig is not CONST_NB_LIGNES - 1:
            text = text + "\n" + "-----" + "\n"
    return text

def pos_tab(num_lig, num_col):
    "Renvoie la position de 0 a 8 selon la ligne et la colonne donnee. Renvoie 10 si les entrees sont erronees."
    pos = 0
    if (num_lig >= 1 and num_lig <= 3) and (num_col >= 1 and num_col <=3):
        pos = 3 * (num_lig-1) + (num_col-1)
    else:
        pos = 10
    return pos

def placer_char(tableau, pos, char):
    "Placer le charactere a la position donnee"
    tableau[pos] = char
    return

def estPlein(tableau):
    for i in tableau:
        if i != 'X' and i != 'O':
            return 0

    return 1

def estGagnant(tableau, char):
    for i in range(0, CONST_NB_COLONNES):
        if colonneGagnante(tableau, char, i+1) == 1:
            return 1
    for i in range(0, CONST_NB_LIGNES):
        if ligneGagnante(tableau, char, i+1) == 1:
            return 1
    if diagGagnante(tableau, char, 1) == 1:
        return 1
    return diagGagnante(tableau, char, 2)

def ligneGagnante(tableau, char, num_lig):
    nb_char = 0
    for i in range(0,CONST_NB_COLONNES):
        if tableau[pos_tab(num_lig, i+1)] == char:
            nb_char += 1
    if nb_char == 3:
        return 1
    else:
        return 0

def colonneGagnante(tableau, char, num_col):
    nb_char = 0
    for i in range(0, CONST_NB_LIGNES):
        if tableau[pos_tab(i+1, num_col)] == char:
            nb_char += 1
    if nb_char == 3:
        return 1
    else:
        return 0

def diagGagnante(tableau, char, num_dia):
    nb_char = 0
    if num_dia == 1:
        if tableau[0] == char and tableau[4] == char and tableau[8] == char:
            return 1
    elif num_dia == 2:
        if tableau[2] == char and tableau[4] == char and tableau[6] == char:
            return 1
    return 0

def IA_joue(tableau, char_IA):
    "Retourne le tableau avec l'action de l'IA."
    val_tab = list(tableau)
    list_val_tab = []
    for i in range(0, len(tableau)):
        if val_tab[i] != 'X' and val_tab[i] != 'O':
            val_tab[i] = minimax(list_val_tab, Tableau, i, 1, char_IA,0)

    placer_char(tableau, meilleur_pos(val_tab), char_IA)
    return tableau

def minimax(list_val_tab,m_val_tab, pos, estTourIA, char_IA, profondeur):
    del list_val_tab[profondeur:]
    list_val_tab.append(list(m_val_tab))
    
    if char_IA == 'X':
        char_joueur = 'O'
    if char_IA == 'O':
        char_joueur = 'X'
    meilleurScore = 0

    if list_val_tab[profondeur][pos] != 'X' and list_val_tab[profondeur][pos] != 'O':
        if estTourIA == 1:
            list_val_tab[profondeur][pos] = char_IA
            if estGagnant(list_val_tab[profondeur], char_IA):
                meilleurScore = 15 - profondeur
            else:
                for i in range(0, len(m_val_tab)):
                    valeur = minimax(list_val_tab, list_val_tab[profondeur], i, 0, char_IA, profondeur + 1)
                    meilleurScore = max(valeur, meilleurScore)

        else:
            list_val_tab[profondeur][pos] = char_joueur
            if estGagnant(list_val_tab[profondeur], char_joueur):
                meilleurScore = -15 + profondeur
            else:
                for i in range(0, len(m_val_tab)):
                    valeur = minimax(list_val_tab,list_val_tab[profondeur], i, 1, char_IA, profondeur + 1)
                    meilleurScore = min(valeur, meilleurScore)

    return meilleurScore

def meilleur_pos(tableau):
    "Renvoie la meilleur position a jouer"
    meilleurPos = 0
    for i in range(0,len(tableau)):
        if tableau[i] != 'X' and tableau[i] != 'O' and tableau[i] != '':
            if tableau[meilleurPos] == 'X' or tableau[meilleurPos] == 'O':
                meilleurPos = i
            elif int(tableau[i]) >= int(tableau[meilleurPos]):
                meilleurPos = i

    return meilleurPos



Tableau = ["", "", "", \
           "", "O", "X", \
           "O", "X", "O"]
IA_joue(Tableau, 'X')

print(afficher_tableau(Tableau))
