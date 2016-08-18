# -*- coding: utf-8 -*-
"""
Created on Mon Dec 07 11:30:17 2015

@author: AkishinoShiame
"""

import cPickle, gzip, numpy

# Load the dataset
f = gzip.open('mnist.pkl.gz', 'rb')
data = cPickle.load(f)
train_set, valid_set, test_set = data
###### above is origional pkl read file


##### below test seprate file to pic and label 
train_set_pic , train_set_lab = train_set
valid_set_pic , valid_set_lab = valid_set
test_set_pic , test_set_lab = test_set
##### above test seprate file to pic and label

print data

print type(train_set)
print type(valid_set)
print type(test_set)

print ("train set picture\n")
print type(train_set_pic)
#output train_set label
print ("train set label\n")
print type(train_set_lab)


print ("valid set picture\n")
#output valid_set picture
print type(valid_set_pic)
#output valid_set label
print ("valid set label\n")
print type(valid_set_lab)


#output test_set picture
print ("test set\n")
print type(test_set_pic)
#output test_set label
print type(test_set_lab)

###### below is origional pkl read file
f.close()