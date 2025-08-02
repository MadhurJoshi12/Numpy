import numpy as np

#Question 9
arr = np.array([[1, 2, 3],[4, 5, 6]])
scalars = np.array([[1],[10]])
result = arr * scalars
print(result)


#Question 10
arr1 = np.array([[1, 2, 3],[4, 5, 6],[7, 8, 9]])
col_means = arr1.mean(axis=0)
result = arr1 - col_means

print("Original Array:\n", arr1)
print("Column Means:", col_means)
print("After Subtracting Column Means:\n", result)


#Question 11
prices = np.array([100,200,300])
discount = 10

final_prices = prices - (prices * discount/100)
print(final_prices)


#Question 12
# Step 1: Create an array
arr = np.array([10, 20, 30, 40, 50])

# Step 2: Find the mean of the array
mean_val = np.mean(arr)
print("Mean:", mean_val)  # Should be 30.0

# Step 3: Compare each element with the mean using broadcasting
greater_than_mean = arr > mean_val
print("Elements greater than mean:", greater_than_mean)

# Step 4 (Optional): Extract the values which are greater than mean
print("Actual values:", arr[greater_than_mean])