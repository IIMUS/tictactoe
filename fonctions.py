#fonctions.py

from getpass import getpass

def input_clavier(_texte, _password = False):
    try:
        if(not _password):
            return input(_texte)
        else:
            return getpass(_texte)
    except NameError as error:
        print "---NAME_ERROR LORS DE L'INSERTION---:", error
    except IndexError as error:
        print "---INDEX_ERROR LORS DE L'INSERTION---:", error
    except SyntaxError as error:
        print "---SYNTAX_ERROR LORS DE L'INSERTION---:", error
    except KeyError as error:
        print "---KEY_ERROR LORS DE L'INSERTION---:", error
