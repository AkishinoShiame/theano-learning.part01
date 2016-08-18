# -*- coding: utf-8 -*-
"""
Created on Wed Dec 23 21:35:36 2015

@author: AkishinoShiame
"""

import cPickle, gzip, numpy

# Load the dataset
f = gzip.open('training_data.pkl.gz', 'rb')
data = cPickle.load(f)
train_set, label = data
###### above is origional pkl read file




print data

print type(data)

print ("train set picture\n")
print type(train_set)
#output train_set label
print ("train set label\n")
print type(label)

###### below is origional pkl read file
f.close()