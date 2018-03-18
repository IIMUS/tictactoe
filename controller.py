from model import Model
from viewer import Viewer

class Controller:
    """
    Classe s'occupant des interactions entre l'utilisateur et l'application. Lorsqu'il comprend ce que l'utilisateur
    veut faire, il delegue la tache a ses membres.

    Attributs:
        modele (Model): contient toutes les donnees necessaires au jeu, ainsi que les algorithmes pour les manipuler.
        afficheur (Viewer): contient les methodes d'affichage du systeme.
    """

    def __init__(self):
        print("Controller::__init__")
        self.modele = Model()
        self.afficheur = Viewer()

    def start(self):
        """
        On appelle cette methode lorsque l'application est prete a gerer les interactions de l'utilisateur.
        """
        print("Controller::start")
        self.afficheur.afficher_menu_principal()

    def jouer(self):
        print("Controller::jouer")

    def preferences(self):
        print("Controller::preferences")

    def quitter(self):
        print("Controller::quitter")
