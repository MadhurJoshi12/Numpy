#Stacking
import numpy as np

arr1 = np.array([1,2,3])
arr2 = np.array([4,5,6])
print(np.vstack((arr1, arr2)))          #vstack = vertically stack
print(np.hstack((arr1, arr2)))          #hstack = horizontally stack


#Spiltting
'''
    np.split()---------->It will split equally
    np.hsplit()---------->It will split horizontally
    np.vsplit()---------->It will split vertically
    
'''
arr = np.array([10,20,30,40,50,60])
print(np.split(arr, 2))
