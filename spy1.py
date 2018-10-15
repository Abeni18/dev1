# -*- coding: utf-8 -*-
"""
Created on Thu Oct 11 18:45:15 2018

@author: Abenezer
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from pandas.plotting import scatter_matrix
#import keras
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
#Data Preprocessing
dataset = pd.read_csv('KIA1.csv')

#dataset.hist()
#plt.show()

#print(dataset.head(10))

X = dataset.iloc[:,:-1].values
y = dataset.iloc[:,49 ].values

'Filling the missing data'

from sklearn.preprocessing import Imputer 
#create object
imputer = Imputer(missing_values = 'NaN', strategy = 'mean', axis = 0)
imputer.fit(X)
# overiting X with the new X with filled missing data
X = imputer.transform(X)

#plt.plot(X[:,48])
#plt.hist(X[0:10,:])

' Encoding Catagorical Data'

# label ecoding y
labelencoder_y = LabelEncoder()
labelencoder_y.fit_transform(y)

# onehot endcoding x
onehotencoder = OneHotEncoder(categorical_features = [48])
X = onehotencoder.fit_transform(X).toarray()

plt.scatter(X[:100,2],y[:])






























