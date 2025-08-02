import numpy as np

arr = np.array([10,20,30,40,50,60])
print(arr)
new_arr = np.delete(arr, 0)
print(new_arr)


arr_2d = np.array([[1,2,3], [4,5,6]])
print(arr_2d)
new_arr2 = np.delete(arr_2d, 0 , axis=0)        #Yaha 0 means first row and axis=0 means we are talking about rows
print(new_arr2)
