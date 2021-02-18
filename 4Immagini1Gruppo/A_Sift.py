import cv2
import numpy as np
class Sift:
    def describe(self, image):
        nDescriptors = 20
        sift = cv2.SIFT_create(nDescriptors)
        keypoints, descriptors = sift.detectAndCompute(image, None)
        descriptors = descriptors.flatten()
        size = (nDescriptors * 128) + 384
        if descriptors.size < size:
            descriptors = np.concatenate([descriptors, np.zeros(size - descriptors.size)])
        return descriptors