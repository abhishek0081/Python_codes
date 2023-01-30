import numpy as np
 
arr = np.array([0, 1, 2, 3, 4])
print(arr)
print('---Exponential Values of arr---')
print(np.exp(arr))
 
arr1 = np.random.randint(0, 6, size = (3, 4))
print('\n-----Two Dimensional Random Array----')
print(arr1)
print('---Exponential Values of Two Dimensional Random Array---')
print(np.exp(arr1))
 
arr2 = np.random.randint(0, 10, size = (2, 3, 4))
print('\n-----Three Dimensional Array----')
print(arr2)
print('---Exponential Values of Three Dimensional Random Array---')
print(np.exp(arr2))