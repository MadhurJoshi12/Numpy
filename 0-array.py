import numpy as np
#One-Dimensional array(1-D)
ar_1d = np.array([10,20,30,40,50])
print(ar_1d)
print("Dimensions:", ar_1d.ndim)

#Two-Dimensional array(2-D)
arr_2d = np.array([[1,2,3], [4,5,6], [7,8,9]])
print(arr_2d)
print("Dimensions:", arr_2d.ndim)
#Multi-Dimensional array(matrix)
matrix_3d = np.array([
  [[2, 4, 6], [8, 10, 12]],   # First "block"
  [[14, 16, 18], [20, 22, 24]]  # Second "block"
])
print(matrix_3d)
print("Dimensions:", matrix_3d.ndim)
arr4 = np.array([
  [
    [[1, 2], [3, 4]],   # First 3D block
    [[5, 6], [7, 8]]
  ],
    [[9, 10], [11, 12]],  # Second 3D block
    [[13, 14], [15, 16]]
  ])
print(arr4)
print("Dimensions:", arr4.ndim)