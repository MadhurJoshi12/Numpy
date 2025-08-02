import numpy as np

# Indexing
arr = np.array([10,20,30,40,50])
print(arr[0])
print(arr[2])
print(arr[-1])



# Slicing
arr2 = np.array([10,20,30,40,50,60])
print(arr2[1:5]) #index 1 to 4
print(arr2[:4])  #index 0 to 3
print(arr2[::2]) #every second element
print(arr2[::-1])    #It will reverse



# Fancy Indexing
arr3 = np.array([10,20,30,40,50])
print(arr3[[0,2,4]])



# Filtering 
arr4 = np.array([10,20,30,40,50])
print(arr4[arr4 > 25])
