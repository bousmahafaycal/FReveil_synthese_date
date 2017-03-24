"""
Ce module devra par la suite etre importer dans le FReveil 
Module créé le : 2017_3_24
Nom initial du module : synthese_date

"""
from config import *
from synthese import *

def start(arguments):
	# Cette fonction sera la fonction qui sera lancée par le module. argument est une liste contenant les arguments passés au lancement du module
	
	a = Synthese()
	a.syntheseDate()


		