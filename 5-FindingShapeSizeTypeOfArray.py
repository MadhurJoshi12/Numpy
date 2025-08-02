import numpy as np

#Shape
#It helps ous to find the structure of a array. Means how many rows and column it have.
arr_2d = np.array([[1,2,3], [4,5,6]])
print(arr_2d.shape)



#Size
#It helps ous to figure out the total number of element in an array
arr = np.array([[10,20,30], [40,50,60]])
print(arr.size)


#ndim       ----->n dimensions
#It help ous to find the number dimensions in the array
arrr_1d = np.array([1,2,3])
arrr_2d = np.array([[1,2,3], [4,5,6]])
arrr_3d = np.array([[[1,2],[3,4],[5,6],[7,8]]])

print(arrr_1d.ndim)
print(arrr_2d.ndim)
print(arrr_3d.ndim)


#dtype      ---->datatype
#It help ous to find the data type of the array
arrr = np.array([10,20,30.5,40])
print(arrr.dtype)
