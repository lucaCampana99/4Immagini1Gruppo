import numpy as np
import csv
class ComparatoreIsto:
    def __init__(self, indexPath):
        self.indexPath = indexPath
    def chi2_distance(self, histA, histB, eps = 1e-10):
        d = 0.5 * np.sum([((a-b)**2) / (a+b+eps) for(a,b) in zip(histA, histB)])
        return d
    def comparaIsto(self, queryFeatures, limit = 10):
        results = {}
        # apertura index file
        with open(self.indexPath) as f:
            reader = csv.reader(f)
            # passo le righe
            for row in reader:
                #comparo le chi squared distance
                features = [float(x) for x in row [1:]]
                d = self.chi2_distance(features, queryFeatures)
                #aggiorno i results
                results[row[0]] = d
            f.close()
        # ritorno i risultati
        return results
