import numpy as np
import cv2
import csv
from A_Sift import Sift
import json
import pandas as pa
import re
import scipy  as sp
import scipy.spatial

class ComparatoreSift:
    def __init__(self, indexPath):
        self.indexPath = indexPath
        
    # Matcher con distanza euclidea
    def euclidea(self, features, queryFeatures):
        d = np.linalg.norm(queryFeatures - features)
        return d

    def comparaSift(self, queryFeatures, limit = 10):
        results = {}
        # apro il file json 
        with open (self.indexPath) as input:
            self.data = json.load(input)     
            #attraverso un ciclo for 'matcho' i risultati scritti sul file con le query features
            for k, v in self.data.items():
                # riconverto le features in un array numpy
                features = np.array(v)
                # calcolo la distanza euclidea
                d= self.euclidea(features, queryFeatures)
                #scrivo i risultati del match
                results[k] = d
            input.close()
            
        return results

