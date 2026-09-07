import numpy as np

arr = np.array([10, 20, 30, 40, 50])

print("Q1")
print("Original array:", arr)
print("Addition of 2:", arr + 2)
print("Multiplication by 3:", arr * 3)
print("Division by 2:", arr / 2)

arr = np.array([1, 2, 3, 6, 4, 5])

print("\nQ2(a)")
print("Original array:", arr)
print("Reversed array:", arr[::-1])

x = np.array([1, 2, 3, 4, 5, 1, 2, 1, 1, 1])

values, counts = np.unique(x, return_counts=True)
max_count = counts.max()
most_frequent = values[counts == max_count]

print("\nQ2(b)(i)")
print("Most frequent value:", most_frequent)
print("Frequency:", max_count)

for value in most_frequent:
    print("Indices of", value, ":", np.where(x == value)[0])

y = np.array([1, 1, 1, 2, 3, 4, 2, 4, 3, 3])

values, counts = np.unique(y, return_counts=True)
max_count = counts.max()
most_frequent = values[counts == max_count]

print("\nQ2(b)(ii)")
print("Most frequent value(s):", most_frequent)
print("Frequency:", max_count)

for value in most_frequent:
    print("Indices of", value, ":", np.where(y == value)[0])

arr = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])

print("\nQ3")
print("Array:")
print(arr)
print("1st row, 2nd column:", arr[0, 1])
print("3rd row, 1st column:", arr[2, 0])

Rhythmpreet = np.linspace(10, 100, 25)

print("\nQ4")
print("Array:")
print(Rhythmpreet)
print("Dimensions:", Rhythmpreet.ndim)
print("Shape:", Rhythmpreet.shape)
print("Total elements:", Rhythmpreet.size)
print("Data type:", Rhythmpreet.dtype)
print("Total bytes:", Rhythmpreet.nbytes)

print("Transpose using reshape:")
print(Rhythmpreet.reshape(25, 1))

print("Transpose using T after reshaping:")
print(Rhythmpreet.reshape(1, 25).T)

ucs420_Rhythmpreet = np.array([
    [10, 20, 30, 40],
    [50, 60, 70, 80],
    [90, 15, 20, 35]
])

print("\nQ5")
print("Original array:")
print(ucs420_Rhythmpreet)

print("Mean:", np.mean(ucs420_Rhythmpreet))
print("Median:", np.median(ucs420_Rhythmpreet))
print("Maximum:", np.max(ucs420_Rhythmpreet))
print("Minimum:", np.min(ucs420_Rhythmpreet))
print("Unique elements:", np.unique(ucs420_Rhythmpreet))

reshaped_ucs420_Rhythmpreet = ucs420_Rhythmpreet.reshape(4, 3)

print("Reshaped array:")
print(reshaped_ucs420_Rhythmpreet)

resized_ucs420_Rhythmpreet = np.resize(ucs420_Rhythmpreet, (2, 3))

print("Resized array:")
print(resized_ucs420_Rhythmpreet)