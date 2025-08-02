import numpy as np
# arr = np.array([10,20,30,40,50,60])
# print(arr)
# new_arr = np.insert(arr, 2, 100)
# print(new_arr)

#Now with 2D array
arr_2d = np.array([[1,2],[3,4]])
print(arr_2d)

# insert a new row at index 1
new_arr_2d = np.insert(arr_2d, 1, [5,6], axis=0)        #Here axis=0 means rowwise,axis=1 means columnwise
print(new_arr_2d)                                       # and axis=None means flatter(in the same line)

# Add a new row to only one box(3D)
arr_3d = np.array([
    [[1, 2], [3, 4]],     # table 0
    [[5, 6], [7, 8]]      # table 1
])
# Shape: (2, 2, 2)

# Row to add
new_row = [9, 9]

# Insert row at index 1 for all boxes
new_arr_3d = np.insert(arr_3d, 1, new_row, axis=1)

print(new_arr_3d)
print(new_arr_3d.shape)

