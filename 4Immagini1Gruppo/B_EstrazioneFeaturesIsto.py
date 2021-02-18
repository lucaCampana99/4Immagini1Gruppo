from A_Istogramma import Istogramma
import argparse
import glob
import cv2

# COME CAMBIARE DATASET: 
# 1: trascina il dataset scelto   all'interno della cartella dell'applicazione 
# 2: copia la sottostante riga di codice, sostituendo a dataset2 il nome del dataset scelto
# python3 B_EstrazioneFeaturesIsto.py --dataset dataset2 --index index.csv
# 3: compila B_EstrazioneFeaturesIsto, all'interno del terminale incolla la riga precedentemente copiata

# costruisco il parser
parser = argparse.ArgumentParser()
parser.add_argument("-d", "--dataset", required = True,
	help = "immagini da confrontare")
parser.add_argument("-i", "--index", required = True,
	help = "indice dove sono conservate le features")
args = vars(parser.parse_args())
# inizializzo il descrittore immagine istogramma
cdi = Istogramma((8, 12, 3))
# apro e scrivo nel output index file
output = open(args["index"], "w")
# passo ogni immagine
for imagePath in glob.glob(args["dataset"] + "/*.jpg"):
	# estraggo l'imageID
	imageID = imagePath[imagePath.rfind("/") + 1:]
	#leggo l'immagine
	#image = cv2.imread(imagePath)
	# descrivo l'immagine tramite le features dell'istogramma
	featuresIsto = cdi.describe(imagePath)
    # scrivo queste features in un file index
	featuresIsto = [str(f) for f in featuresIsto]
	output.write("%s,%s\n" % (imageID, ",".join(featuresIsto)))
# chiudo il file index
output.close()
