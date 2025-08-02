## **Practice Questions based on numpy.**



#### ✅ *Section 1: Basics \& Indexing*

1-Create a 1D NumPy array with values from 10 to 50 (inclusive), and extract every 5th element.

--->arr = np.array(\[10, 20, 30, 40, 50])

2-Replace the value 30 with 300 using indexing.

3-Create a 3x3 identity matrix using NumPy.

4-Reverse this array: arr = np.array(\[1, 2, 3, 4, 5])



#### ✅ *Section 2: Reshaping \& Slicing*

5-Convert a 1D array of 16 elements into a 4x4 matrix.

6-From a 5x5 matrix, extract the center 3x3 matrix.

7-Flatten a 2D array using both .ravel() and .flatten(). Show the difference using editing the first element after each.

8-Split this array into two parts:

--->arr = np.array(\[10, 20, 30, 40, 50, 60])



#### ✅ *Section 3: Broadcasting \& Math Ops*

9-Multiply each row of this matrix by a different scalar:

--->arr = np.array(\[\[1, 2, 3], \[4, 5, 6]])

--->scalars = np.array(\[\[1], \[10]])

10-Subtract the column mean from each column in a 3x3 matrix.

11-Create a NumPy array and apply a 10% discount to all elements using broadcasting.

12-Check which elements in an array are greater than the mean of the array.



#### ✅ *Section 4: NaN, Inf, \& Cleaning*

13-Create an array with np.nan and np.inf values. Use np.nan\_to\_num() to replace them with custom values.

14-Count how many np.nan values are in an array.

15-Find the indices where the array has np.inf or -np.inf.



#### ✅ *Section 5: Real-World Scenarios*

16-Simulate prices of 7 items. Apply 3 different discount percentages to them (some items get same discount).

17-Given a list of temperatures in Celsius, convert them to Fahrenheit using broadcasting.

18-Create a random 5x5 matrix of integers (0-100), and:

--->Find the max, min, mean

--->Replace all even numbers with 0

--->Normalize a matrix (scale values to 0–1 range).

--->Detect outliers in a 1D array (anything > mean + 2\*std).
