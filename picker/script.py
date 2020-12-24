from sklearn.cluster import KMeans
from collections import Counter
import cv2
import urllib.request as ur
import numpy as np

def get_dominant_color(image, k=4, image_processing_size = None):
    #resize image if new dims provided
    if image_processing_size is not None:
        image = cv2.resize(image, image_processing_size, 
                            interpolation = cv2.INTER_AREA)
    
    #reshape the image to be a list of pixels
    image = image.reshape((image.shape[0] * image.shape[1], 3))

    #cluster and assign labels to the pixels 
    clt = KMeans(n_clusters = k)
    labels = clt.fit_predict(image)

    #count labels to find most popular
    label_counts = Counter(labels)

    #subset out most popular centroid
    dominant_color = clt.cluster_centers_[label_counts.most_common(1)[0][0]]

    return list(dominant_color)

def url_to_image(url):
	# download the image, convert it to a NumPy array, and then read
	# it into OpenCV format
	resp = ur.urlopen(url)
	image = np.asarray(bytearray(resp.read()), dtype="uint8")
	image = cv2.imdecode(image, cv2.IMREAD_COLOR)
	# return the image
	return image

def get_hex_code(colours):
    # rounding up to the nearest integer
    B = round(colours[0])
    G = round(colours[1])
    R = round(colours[2])


    # formatting it to get it in the correct format Eg: #FF00FF
    code = '#%02x%02x%02x' % (R, G, B)

    return (code.upper())
