"""
partie.py
Emrick St-Pierre
25 Novembre 2017
"""

class Partie:
    # Declaration membres
    conv = {}
    num = []
    joueurs = ()

    # Constructeurs
    def __init__(self, _nom_joueur1, _nom_joueur2):
        # Definition membres
        self.conv = {-1:"X", 1:"O", 0:" "}
        self.dessin = ["O", "X"]
        self.num = [1, -1]
        self.tour = 1
        self.board = {x: 0 for x in range(9)}
        self.joueurs = (_nom_joueur2, _nom_joueur1) #(O, X)

    # Definitions fonctions
    def afficher_board(self):
        for i in range(3):
            for j in range(3):
                print "{0}|".format(self.conv[self.board[3*i + j]]),
            print "\n"

    def verif(self):
        for i in range(3):
            if(abs(self.board[3*i + 0] + self.board[3*i + 1] + self.board[3*i + 2]) == 3):
                print("{0} gagne!".format(self.dessin[self.tour%2]))
                return True
            if(abs(self.board[i + 0] + self.board[i + 3] + self.board[i + 6]) == 3):
                print("{0} gagne!".format(self.dessin[self.tour%2]))
                return True
        if(abs(self.board[0] + self.board[4] + self.board[8]) == 3):
            print("{0} gagne!".format(self.dessin[self.tour%2]))
            return True
        if(abs(self.board[2] + self.board[4] + self.board[6]) == 3):
            print("{0} gagne!".format(self.dessin[self.tour%2]))
            return True
        return False

    # Methode principale
    def jouer(self):
        self.afficher_board()
        while(self.tour < 10):
            try:
                while(True):
                    print "Tour a {0}".format(self.joueurs[self.tour%2])
                    c = input("Sur quelle case jouez-vous un {0}? ".format(self.dessin[self.tour%2]))
                    break
                if(c == 'q'):
                    tour = 10
                    return 0
                    break
                if(self.board[c] != 0):
                    print("La case sur laquelle vous voulez jouer est deja utilisee")
                    self.afficher_board()
                else :
                    self.board[c] = self.num[self.tour%2]
                    self.afficher_board()
                    if(self.verif()):
                        print "Victoire de {0}".format(self.joueurs[self.tour%2])
                        return self.joueurs[self.tour%2]
                        break
                    self.tour += 1
            except NameError as error:
                print "---NAME_ERROR LORS DE L'INSERTION---:", error
            except IndexError as error:
                print "---INDEX_ERROR LORS DE L'INSERTION---:", error
            except SyntaxError as error:
                print "---SYNTAX_ERROR LORS DE L'INSERTION---:", error
            except KeyError as error:
                    print "---KEY_ERROR LORS DE L'INSERTION---:", error
        if(self.tour == 10):
            print("Match nul!")
            return 0
