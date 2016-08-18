# -*- coding: utf-8 -*-
"""
Created on Sat Dec 19 19:08:39 2015

@author: AkishinoShiame
"""

import cPickle

#print pickle file for test
f = cPickle.load(file('weights.pkl', 'rb'))
sets = cPickle.load(f)

#picset , labset = sets

print ("ALL")
print (sets)
"""
print ("seperated pic(in 1)")

for i in range(784):
    print picset[0][i], ",",
    
print ("seperated lab")
print labset
"""

f.close()