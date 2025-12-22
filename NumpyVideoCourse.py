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


#Indexing and slicing
arr = np.array([10, 20, 30, 40, 50])
print(arr[2])  #Output: 30
print(arr[1:4])  #Output: [20 30 40]
print(arr[:3])  #Output: [10 20 30]
print(arr[::2]) #start:stop:end  Output: [10 30 50] 
print(arr[::-1]) #reverse the array without loops or extra steps Output: [50 40 30 20 10]

#fancy indexing
arr = np.array([10, 20, 30, 40, 50])
print(arr[[0, 2, 4]])  #Output: [10 30 50]
#list of indices to access multiple elements 

#boolean masking
print(arr[arr > 25])  #Output: [30 40 50] 

#reshaping arrays
arr = np.array([1, 2, 3, 4, 5,5])
reshaped_arr = arr.reshape((2, 3))  #2 rows, 3 columns

# .ravel() is used to flatten a multi-dimensional array into a 1-dimensional array, affecting the original array.
# .flatten() also flattens a multi-dimensional array into a 1-dimensional array but returns a new array, leaving the original array unchanged.

arr_2d = np.array([[1, 2, 3], [4, 5, 6]])
flattened_ravel = arr_2d.ravel()
flattened_flatten = arr_2d.flatten()


#arrays have fixed size, therefore we cannot append or remove elements directly. 
#However, we can create new arrays with the desired changes using functions like np.append() and np.delete().

arr3 = np.array([1, 2, 3, 4, 5])
new_arr = np.append(arr3, [6, 7, 8])  #Appending elements 
new_arr1 = np.insert(arr3, 2, 100)  #Inserting element at index 2 

arr_2d = np.array([[1, 2, 3], [4, 5, 6]])
new_arr_2d = np.insert(arr_2d, 1, [10, 11, 12], axis=0)  #Inserting row at index 1 
#1 means row, axis = 0 means rows, axis = 1 means columns
 
arr4 = np.array([10, 20, 30, 40])
new_arr4 = np.append(arr4, [50, 60])  #Appending elements 
#Output: [10 20 30 40 50 60]

arr5 = np.array([1, 2, 3, 4, 5])
arr6 = np.array([6, 7, 8, 9, 10])
concatenated_arr = np.concatenate((arr5, arr6))  #Concatenating two arrays
#Output: [ 1  2  3  4  5  6  7  8  9 10]

concatenated_arr1 = np.concatenate((arr5, arr6), axis=1)  #Concatenating along columns
#It will raise an error because both arrays are 1-dimensional and cannot be concatenated along axis 1.

arr7 = np.array([10, 20, 30, 40, 50])
new_arr7 = np.delete(arr7, 2)  #Deleting element at index 2

arr_2d = np.array([[1, 2, 3], [4, 5, 6]])
new_arr_2d = np.delete(arr_2d, 1, axis=0)  #Deleting row at index 1 and axis=0 means rows
#Output: [[1 2 3]]

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
print(np.vstack((arr1, arr2)))  #Stacking arrays vertically
print(np.hstack((arr1, arr2)))  #Stacking arrays horizontally 

arr = np.array([1, 2, 3, 4, 5])
print(np.split(arr, 2))  #Splitting array into 2 parts


#Broadcasting is a powerful mechanism in Numpy that allows operations to be performed on arrays of different shapes and sizes without the need for explicit replication of data.
prices = [100, 200, 300]
discount = 10
final_prices = []
for price in prices:
    final_price = price - (price * discount / 100)
    final_prices.append(final_price)
print(final_prices)  #Output: [90.0, 180.0, 270.0]
#inefficient approach

#Using Numpy broadcasting
prices= np.array(prices)
discount = 10
final_prices = prices - (prices * discount/ 100) 
print(final_prices)  #Output: [ 90. 180. 270.] 


matrix = np.array([[1, 2, 3], [4, 5, 6]])
vector = np.array([10, 20, 30])
result = matrix + vector  #Broadcasting addition 
#Output: [[11 22 33] 

#Vectorized operations
list1 = [1, 2, 3,]
list2 = [4, 5, 6]
result = [a + b for a, b in zip(list1, list2)]
#not efficient for large datasets


#buitin functions in numpy
arr = np.array([1, 2, np.nan, 3, 4, 5])
print(np.isnan(arr))  #Check for NaN(Not A Number) 

#np.nan is used to represent missing or undefined values in numerical arrays. 
print(np.nan == np.nan)  #Output: False  it indicates that NaN is not equal to anything, including itself.

cleaned_arr = np.nan_to_num(arr,nan=100)  #Replace NaN with 0(default) , here 100 

#np.isinf() is used to check for infinite values in an array.
arr_inf = np.array([1, 2, np.inf, -np.inf, 5]) 
print(np.isinf(arr_inf))  #Output: [False False  True  True False] 
cleaned_arr = np.nan_to_num(arr_inf, posinf=1000, neginf=-1000)  #Replace inf with large finite numbers  
