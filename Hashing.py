'''Image Indexing by Hashing '''

import pandas as pd
import json

df = pd.read_csv("C:\\Users\\Apoorv\\Desktop\\Machinelearning_Assignment\\tops_1.csv", dtype=str) 

'''Deleting values with dulplicate ID '''

df = df.drop_duplicates(subset='ID', keep="last")
df = df.reset_index(drop=True)

''' Make two list: 1. New value for image 2. Duplicate value '''

distinct = {}
for i in range(df.shape[0]):
    url = df.image[i].split(';')[1]
    if url in distinct:
        distinct[url].append(i)
    else:
        distinct[url] = [i]
		
duplicate = {}
for key, value in distinct.items():
    if len(value) > 1:
        duplicate[df.ID[value[0]]] = [df.ID[x] for x in value[1:]]
		
''' Output in JSON '''
		
json.dump(duplicate, indent=4, fp=open("C:\\Users\\Apoorv\\Desktop\\Machinelearning_Assignment\\out.json","w"))
