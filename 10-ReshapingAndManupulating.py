# Reshape 

import numpy as np

arr = np.array([1,2,3,4,5,6])
reshape_Arr = arr.reshape(2,3)
print(reshape_Arr)


# Flatten 
'''
    .ravel() --> view
    .flatten() --> copy
'''

arr_2d = np.array([[1,2,3], [4,5,6]])
print(arr_2d.ravel())
print(arr_2d.flatten())
