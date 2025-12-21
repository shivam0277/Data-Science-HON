import numpy as np

temperatures = np.array([30, 32, 34, 33])
average = np.mean(temperatures)
print("Average temperature:", average)

# Advantages of Numpy:
# 1. Performance: Numpy operations are implemented in C and optimized for performance, making them significantly faster than standard Python lists for numerical computations.
# 2. Memory Efficiency: Numpy arrays use less memory compared to Python lists, allowing for efficient storage and manipulation of large datasets. 
# 3. Convenience: Numpy provides a wide range of mathematical functions and operations that can be applied directly to arrays, simplifying code and improving readability.

#numpy arrays are memory efficient, fast, and provide a wide range of functionalities for numerical computations.
# Arrays - 1-d array, 2-d array, multi-dimensional array

#creating arrays from lists
arr = np.array([1, 2, 3, 4, 5])
print(arr)

#with default values
arr_zeros = np.zeros(3)  #1 * 3 array of zeros or 1-d array 
print(arr_zeros)

ones_array = np.ones((3, 2))
print(ones_array)

filled_array = np.full((2, 2), 7)  #2 * 2 array filled with 7
print(filled_array) 

arr = np.arange(0, 10, 2)  #array with values from 0 to 10 with step of 2
print(arr)

#creating arrays with random values
identity_matrix = np.eye(3)  #3 * 3 identity matrix
print(identity_matrix)

#shape is used to define the dimensions of the array
arr_2d = np.array([[1, 2, 3], [4, 5, 6]])
print("2D Array shape:", arr_2d.shape) 

#ndim is used to get the number of dimensions of the array 
arr_3d = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
print(arr_3d.ndim)
#Output: 3 

#dtype is used to get the data type of the elements in the array
arr_float = np.array([1.0, 2.0, 3.0])
print(arr_float.dtype)
#Output: float64 

#astype() is used to change the data type of the elements in the array
arr_int = arr_float.astype(np.int)
print(arr_int.dtype)
#Output: int32 or int64 depending on the system

arr-y = np.array([10, 20, 30, 40, 50])
print(arr+5)

#mathematical operations on arrays
arr3 = np.array([1, 2, 3])
print(np.sum(arr3))  #Output: 6
print(np.mean(arr3))  #Output: 2.0
print(np.std(arr3))   #Output: 0.816496580927726
print(arr3 + 10)  #Output: [11 12 13]



