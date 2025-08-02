import numpy as np

# Question 5
arr = np.arange(1,17)
reshape_arr = arr.reshape(4,4)
print(reshape_arr)


# Question 6
arr1 = np.arange(1,26)
reshape_arr1 =arr1.reshape(5,5)
center = reshape_arr1[1:4, 1:4]
print(center)


#Question 7
arr2 = np.array([[1,2,3],[4,5,6]])
print(arr2.ravel())
print(arr2.flatten())

r = arr2.ravel()
f = arr2.flatten()

r[1] = 100
f[2] = 100
print(arr2) #Here you can see the difference


#Question 8
arr3 = np.array([10, 20, 30, 40, 50, 60])
print(np.split(arr3,2))
