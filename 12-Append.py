import numpy as np

arr = np.array([10,20,30])
new_arr = np.append(arr, [40,50,60])

print(new_arr)


arr1 = np.array([1,2,3])
arr2 = np.array([4,5,6])

new_arrr = np.concatenate((arr1, arr2))
print(new_arrr)
