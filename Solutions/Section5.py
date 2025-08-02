import numpy as np

#Question 16
prices = np.array([150, 200, 50, 300, 120, 90, 400])
discounts = np.array([10, 20, 10, 5, 20, 10, 5])

final_prices = prices - (prices * discounts/100)
print(final_prices)


#Question 17
celsius = np.array([0, 10, 20, 37, 100])
F = celsius * 9/5 + 32
print(F)


#Question  18
arr = np.random.randint(0, 101, (5, 5))
print("Matrix:\n", arr)

print("Max:", np.max(arr))
print("Min:", np.min(arr))
print("Mean:", np.mean(arr))

#--> Replacing even with 0
arr[arr % 2 == 0] = 0
print("Matrix after replacing even numbers with 0:\n", arr)

#--> Normalization
normalized = (arr - arr.min()) / (arr.max() - arr.min())
print(normalized)

#--> Outliers

# Step 1: Calculate mean and standard deviation
mean = np.mean(arr)
std = np.std(arr)

# Step 2: Calculate thresholds
upper_threshold = mean + 2 * std                    #In data analysis, a threshold is a boundary value
lower_threshold = mean - 2 * std                    #used to decide what is "normal" and what is not.

# Step 5: Detect outliers
'''Outliers are values that are way too different from the rest.
They can be too high or too low compared to most other values.'''
outliers = arr[(arr > upper_threshold) | (arr < lower_threshold)]

print("\nMean:", mean)
print("Standard Deviation:", std)
print("Upper Threshold:", upper_threshold)
print("Lower Threshold:", lower_threshold)
print("Outliers:", outliers)
