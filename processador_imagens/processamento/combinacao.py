import numpy as np
from skimage.color import rgb2gray
from skimage.exposure import match_histograms
from skimage.metrics import structural_similarity

def finde_difference(image1,image2):
    assert image1.shape == image2.shape, "Specify 2 images with same shape."

    gray_image1 = rgb2gray(image1)
    gray_image2 = rgb2gray(image2)

    (score,difference_image)= structural_similarity(gray_image1,gray_image2,full=True)
    print("Smilarity of the image:", score)
    normalized_difference_image = (difference_image - np.min(difference_image))/(np.max(difference_image)-np.min(difference_image))
    return normalized_difference_image

def transfer_histogram():
    matched_image = match_histograms(image1,image2,multichannel=True)
    return matched_image