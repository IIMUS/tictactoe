# pgsql.py

import psycopg2
import base64
from fonctions import input_clavier

#print "---Importation pgsql.py---"

# Constantes
#CONST_PG_TABLE_JOUEURS = 'test_table_py'
CONST_PG_TABLE_COMPTES = 'comptes'
CONST_PG_ATTRIBUT_NOM_COMPTE = 'nom_compte'
CONST_PG_ATTRIBUT_ID_COMPTE = 'id_compte'
CONST_PG_TABLE_PARTIES = 'parties'
CONST_PG_ATTRIBUT_ID_JOUEUR_1 = 'id_joueur_1'
CONST_PG_ATTRIBUT_ID_JOUEUR_2 = 'id_joueur_2'
CONST_PG_ATTRIBUT_ID_VAINQUEUR = 'id_vainqueur'

class Connexion:

    def __init__(self):
        try:
            print "---Connexion---"
            password = input_clavier("Entrez le mot de passe de la base de donnees :", True)
            self.conn = psycopg2.connect("dbname=postgres user=postgres password={0}".format(password))
            self.cur = self.conn.cursor()
        except psycopg2.DatabaseError as error:
                print(error)

    def PG_CONNECT(self):
        try:
            print "---Connexion---"
            password = input_clavier("Entrez le mot de passe de la base de donnees :", True)
            self.conn = psycopg2.connect("dbname=postgres user=postgres password={0}".format(password))
            self.cur = self.conn.cursor()
        except psycopg2.DatabaseError as error:
                print(error)

    def PG_DISCONNECT(self):
        print "---Deconnexion---"
        self.conn.commit()
        self.cur.close()
        self.conn.close()

    def SQL_INSERT(self, _table, _values):
        print "---INSERTION_AVEC: {0} ---".format((_table, _values))
        self.cur.execute("INSERT INTO {0} VALUES {1}".format(_table, _values))
        self.conn.commit()

    def SQL_SELECT(self, _attribut, _table):
        print "---SELECTION_AVEC: {0} ---".format((_attribut, _table))
        self.cur.execute("SELECT {0} FROM public.{1}".format(_attribut, _table))
        return self.cur.fetchall()


#---Tests---
#liste = SQL_SELECT('nom_joueur', 'test_table_py')
#print('Simon' in cur.fetchall())
#print liste
#print ('Simon',) == liste[1]
