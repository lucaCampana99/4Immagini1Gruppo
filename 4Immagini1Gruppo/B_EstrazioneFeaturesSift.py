from A_Sift import Sift
import argparse
import numpy as np
import glob
import cv2
import json
import pandas as pa
import pickle

# COME CAMBIARE DATASET: 
# 1: trascina il dataset scelto   all'interno della cartella dell'applicazione 
# 2: copia la sottostante riga di codice, sostituendo a dataset2 il nome del dataset scelto
# python3 B_EstrazioneFeaturesSift.py --dataset dataset2 --indexsift index.json
# 3: compila B_EstrazioneFeaturesSift, all'interno del terminale incolla la riga precedentemente copiata

# costruisco il parser
parser = argparse.ArgumentParser()
parser.add_argument("-d", "--dataset", required = True,
	help = "immagini da confrontare")
parser.add_argument("-i", "--indexsift", required = True,
	help = "indice dove sono conservate le features")
args = vars(parser.parse_args())
# inizializzo il descrittore
cds = Sift()
results = {}
#output = open(args["indexsift"], "w")
for imagePath in glob.glob(args["dataset"] + "/*.jpg"):
    # estraggo l'imageID
	imageID = imagePath[imagePath.rfind("/") + 1:]
    #leggo l'immagine
	image = cv2.imread(imagePath)
	image = cv2.resize(image, (480,640))
	#gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    #image8bit = cv2.normalize(gray, None, 0, 255, cv2.NORM_MINMAX).astype('uint8')
	#estraggo le features
	featureSift  =  cds.describe(image)
	#np.reshape(featureSift, 16)
	features = featureSift.tolist()
    #aggiorno i risultati
	results[imageID] = features
	#results = results[imageID].toList()
	#apro il file json
	with open ("index.json", "w") as output:
		json.dump(results, output)
	output.close()
