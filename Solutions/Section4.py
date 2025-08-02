import numpy as np
#Question 13
# Step 1: Create array with NaN and Inf
arr = np.array([1, np.nan, 2, np.inf, 3, -np.inf])

# Step 2: Replace NaN with 0, +inf with 1000, -inf with -1000
cleaned = np.nan_to_num(arr, nan=0, posinf=1000, neginf=-1000)

print("Original array:", arr)
print("Cleaned array:", cleaned)


#Question 14
arr = np.array([1, 2, np.nan, 4, np.nan])
nan_count = np.isnan(arr).sum()

print("Number of NaNs:", nan_count)


#Question 15
arr = np.array([1, np.inf, 2, -np.inf, 3])

inf_indices = np.where(np.isinf(arr))
print("Indices with Inf or -Inf:", inf_indices)
