from A_Sift import Sift
from A_Istogramma import Istogramma
from C_ComparatoreIsto import ComparatoreIsto
from C_ComparatoreSift import ComparatoreSift
import numpy as np
import argparse
import cv2
import json

def salvaPathIndexIsto (self, pathIndexIsto):
	self.pathIndexIsto = pathIndexIsto

def salvaPathIndexSift (self, pathIndexSift):
	self.pathIndexSift = pathIndexSift

def salvaPathInput (self, pathInput):
	self.pathInput = pathInput

def salvaLimite (self, limite):
	self.limite = limite

def mixer(self, numeroFoto):

	# inizializzo i metodi
	cds = Sift()
	cdi = Istogramma((8, 12, 3))

	# carico la query e ne ricavo i descrittori
	query = cv2.imread(self.pathInput)

	# descrivo la query  tramite istogrammi
	featuresIsto = cdi.describe(self.pathInput)
	# ridimensiono la foto e descrivo la query tramite sift
	image = cv2.resize(query, (480,640))
	featuresSift = cds.describe(image)
	# inizializzo i comparatori
	comparatoreIsto = ComparatoreIsto(self.pathIndexIsto)
	comparatoreSift = ComparatoreSift(self.pathIndexSift)

	resultsIsto = comparatoreIsto.comparaIsto(featuresIsto)
	resultsSift = comparatoreSift.comparaSift(featuresSift)
	finalResults = {}
	# calcolo la total score
	for resultID in resultsIsto:
	    #print(resultsSift[resultID])
	    contributo = resultsIsto[resultID]*100
	    print(contributo)
	    print("\n")
	    tScore = resultsSift[resultID] + contributo	    
	    finalResults[resultID] = tScore/1000

	finalResults = sorted([(score, resultID) for (resultID, score) in finalResults.items()])

	return finalResults[:numeroFoto]

	

