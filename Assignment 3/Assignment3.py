# -*- coding: utf-8 -*-
"""Untitled3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1WfibYkqTtAik-e7di_TFnXEMBRSrlgF6
"""

import numpy as np
x =np.random.randint(20, size=15)
print("Original array:")
print(x)
x=x.reshape (3, 5)
print(x)
max_vals = np.max(x, axis=1)
mask = np.equal(x, max_vals[:, np.newaxis])
x = np.where(mask, 0, x)
print("Maximum value replaced by 0:")
print(x)

arr = np.ndarray(shape=(4, 3), dtype=np.int32)

print("Shape:", arr.shape)
print("Type:", type(arr))
print("Data type:", arr.dtype)

arr = np.array([[3, -2], [1, 0]])
eigenvalues, eigenvectors = np.linalg.eig(arr)
print("Eigenvalues:", eigenvalues)
print("Right Eigenvectors:")
for i in range(len(eigenvectors)):
    print(eigenvectors[:, i])

arr = np.array([[0, 1, 2], [3, 4, 5]])
sum = np.trace(arr)
print("Sum of diagonal elements:", sum)

arr = np.array([[1, 2], [3, 4], [5, 6]])
arr1 = np.reshape(arr, (3, 2))
arr2 = np.reshape(arr, (2, 3))

print("Original array:\n", arr)
print("Reshaped to 3x2:\n", arr1)
print("Reshaped to 2x3:\n", arr2)

import matplotlib.pyplot as plt
languages = ["Java", "Python", "PHP", "JavaScript", "C#", "C++"]
popularity = [22.2, 17.6, 8.8, 8, 7.7, 6.7]
fig, ax = plt.subplots()
ax.pie(popularity, labels=languages, autopct='%1.1f%%',explode=[0.1,0,0,0,0,0])

ax.set_title('Popularity of Programming Languages')
plt.show()