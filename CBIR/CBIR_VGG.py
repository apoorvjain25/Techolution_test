from VGG import VGGNet

import numpy as np

ap = argparse.ArgumentParser()

''' Input image '''

ap.add_argument("-query", required = True,
	help = "Path to query which contains image to be queried")

ap.add_argument("-query1", required = True,
	help = "Path to query which contains image to be queried")
	
args = vars(ap.parse_args())

''' importing model '''

model = VGGNet()

''' extracting image features '''

query = model.extract_feat(query)
query1 = model.extract_feat(query1)

''' Compare featues '''

scores = np.dot(query, query1)

print ("Image with highest similarity:", scores)
