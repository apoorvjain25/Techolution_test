from colordescriptor import ColorDescriptor
import argparse
import numpy as np
import cv2

ap = argparse.ArgumentParser()

''' Input both images '''

ap.add_argument("-q", "--query", required = True,
	help = "Path to the query image")
ap.add_argument("-q1", "--query1", required = True,
	help = "Path to the query image")
	
args = vars(ap.parse_args())

cd = ColorDescriptor((8, 12, 3))

''' Extracting features of both images '''

query = cv2.imread(args["query"])
features = cd.describe(query)

query1 = cv2.imread(args["query1"])
features1 = cd.describe(query1)

'''Calculating the similarity between images using chi-square distance method'''

def chi2_distance(histA, histB, eps = 1e-10):
		d = 0.5 * np.sum([((a - b) ** 2) / (a + b + eps)
			for (a, b) in zip(histA, histB)])

		return d


d = chi2_distance(features, features1) 
print("Value of similarity is:",d)   

'''the lesser the value of d the more similar it is, for identical d=0'''

''' Check if image match '''

if d<=0.5:
	print("match")
else:
	print("not_match")





