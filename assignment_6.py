import numpy as np

temperature = np.array([25, 28, 31, 35, 38, 27, 33, 40])

corrected_temperature = temperature + 2

print("Q1(a)")
print("Corrected temperatures:", corrected_temperature)

fahrenheit = (9 / 5) * corrected_temperature + 32

print("\nQ1(b)")
print("Fahrenheit:", fahrenheit)

greater_than_32 = corrected_temperature[corrected_temperature > 32]

print("\nQ1(c)")
print("Readings greater than 32°C:", greater_than_32)

count = np.sum(corrected_temperature > 32)

print("\nQ1(d)")
print("Number of readings greater than 32°C:", count)

print("\nQ1(e)")
print("Vectorization allows NumPy to perform operations on an entire array at once.")
print("Boolean indexing allows us to select only the elements satisfying a condition.")
print("Both methods are generally faster and cleaner than explicitly using a for loop.")

steps = np.array([
    [5000, 6200, 7100],
    [8000, 7500, 9000],
    [4500, 5100, 4800],
    [9000, 8500, 9500]
])

print("\nQ2(a)")
print("Total steps:", steps.sum())

print("\nQ2(b)")
print("Mean steps:", steps.mean())

print("\nQ2(c)")
print("Maximum:", steps.max())
print("Minimum:", steps.min())

print("\nQ2(d)")
print("Total steps for each day:", steps.sum(axis=0))

print("\nQ2(e)")
print("Total steps for each user:", steps.sum(axis=1))

print("\nQ2(f)")
max_index = steps.argmax()
position = np.unravel_index(max_index, steps.shape)
print("Maximum value:", steps[position])
print("User/day position:", position)
print("This corresponds to the 4th user and 3rd day.")

original = np.array([1, 2, 3, 4, 5, 6])

print("\nQ3(a)")
print("Original:", original)

subset = original[1:4]

print("\nQ3(b)")
print("Subset:", subset)

subset[0] = 999

print("\nQ3(c)")
print("Original after modifying subset:", original)
print("Subset:", subset)

copied_array = original[1:4].copy()
copied_array[0] = 500

print("\nQ3(d)")
print("Original after modifying copied array:", original)
print("Copied array:", copied_array)

matrix = np.arange(1, 13).reshape(3, 4)

print("\nQ3(e)")
print("3 x 4 matrix:")
print(matrix)

print("\nQ3(f)")
print("First row:", matrix[0])
print("Last row:", matrix[-1])
print("Second column:", matrix[:, 1])
print("Rows 1-2 and columns 2-3:")
print(matrix[0:2, 1:3])

flattened = matrix.flatten()
raveled = matrix.ravel()

print("\nQ3(g)")
print("Using flatten():", flattened)
print("Using ravel():", raveled)

raveled[0] = 100

print("\nQ3(h)")
print("Ravel after modification:", raveled)
print("Original matrix after modifying ravel:")
print(matrix)

flattened[1] = 200

print("\nQ3(i)")
print("Flatten after modification:", flattened)
print("Original matrix after modifying flatten:")
print(matrix)

print("\nQ3(j)")
print("Shape:", matrix.shape)
print("Dimensions:", matrix.ndim)
print("Size:", matrix.size)
print("Data type:", matrix.dtype)

X = np.array([
    [6, 70, 3],
    [5, 50, 6],
    [8, 80, 2],
    [4, 30, 8]
])

y = np.array([40, 65, 30, 85])

print("\nQ4(a)")
print("Shape of X:", X.shape)
print("Dimensions of X:", X.ndim)

XT = X.T

print("\nQ4(b)")
print("X transpose:")
print(XT)
print("The transpose changes rows into columns and columns into rows.")

XTX = XT @ X

print("\nQ4(c)")
print("X.T @ X:")
print(XTX)

XTX_inv = np.linalg.inv(XTX)

print("\nQ4(d)")
print("Inverse of X.T @ X:")
print(XTX_inv)

beta = XTX_inv @ XT @ y

print("\nQ4(e)")
print("OLS coefficients:")
print(beta)

print("\nQ4(f)")
print("Sleep coefficient:", beta[0])
print("Activity coefficient:", beta[1])
print("Stress coefficient:", beta[2])

print("The coefficients represent the estimated change in assistance score")
print("for a one-unit increase in each feature while the other features are held constant.")

new_user = np.array([5, 40, 7])

predicted_score = new_user @ beta

print("\nQ4(g)")
print("New user:", new_user)
print("Predicted assistance score:", predicted_score)