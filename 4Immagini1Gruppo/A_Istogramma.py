#imagine descriptor (Istogramma di colore)
#tecnica HSV

# importo le librerie
import numpy as np
import cv2
import imutils
class Istogramma:
	def __init__(self, bins):
		# salvo il numero di bins dell'istogramma
		self.bins = bins

	def describe(self, image):
		image = cv2.imread(image)
		image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    # le features ci servono per valutare l'immagine
		features = []
		# ricavo le dimensioni per suddividere l'immagine
		(h, w) = image.shape[:2]
		(cX, cY) = (int(w * 0.5), int(h * 0.5))
    # divido l'immagine in 4 rettangoli
		segments = [(0, cX, 0, cY),(cX, w, 0, cY), (cX, w, cY, h), (0, cX, cY, h)]

		for (startX, endX, startY, endY) in segments:
			# creo una maschera per ogni segment
			Mask = np.zeros(image.shape[:2], dtype = "uint8")
			cv2.rectangle(Mask, (startX, startY), (endX, endY), 255, -1)
			# estraggo gli istogrammi da ogni maschera, la funzione histogram ritorna l'istogramma delle varie regioni
			hist = self.histogram(image, Mask)
      #aggiungo l'istogramma belle varie regioni alle features
			features.extend(hist)
    # return the feature vector
		return features

  # estrazione istogramma 3D dalle varie regioni, usando un numero preciso di bins
	def histogram(self, image, mask):
		hist = cv2.calcHist([image], [0, 1, 2], mask, self.bins,[0, 180, 0, 256, 0, 256])
    #normalizzazione istogramma 3D
		hist = cv2.normalize(hist, hist).flatten()
		return hist