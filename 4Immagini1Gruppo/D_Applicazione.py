from A_Istogramma import Istogramma
from C_ComparatoreIsto import ComparatoreIsto
import argparse
import cv2
import os
from PyQt5.QtGui import *

# python3 Applicazione.py --index index.csv --query queries/_MG_0211.jpg --result-path dataset

# altro argument parser
#ap = argparse.ArgumentParser()
#ap.add_argument("-i", "--index", required = True,
	#help = "dove sono gli indici selezionati")
#ap.add_argument("-q", "--query", required = True,
	#help = "dov'è l'immagine campione")
#ap.add_argument("-r", "--result-path", required = True,
	#help = "dove sono i risultati")
#args = vars(ap.parse_args())



def salvaPathInput (self, pathInput):
	self.pathInput = pathInput

def salvaPathIndex (self, pathIndex):
	self.pathIndex = pathIndex


def applicazione(self, numeroFoto):

	# inizializzazione Istogramma
	cd = Istogramma((8, 12, 3))

	# CARICAMENTO IMMAGINE CAMPIONE
	featuresIsto = cd.describe(self.pathInput)

	# Comparatore
	compara = ComparatoreIsto(self.pathIndex)
	results = compara.comparaIsto(featuresIsto)
	results = sorted([(v, k) for (k, v) in results.items()])

	return results[:numeroFoto]
