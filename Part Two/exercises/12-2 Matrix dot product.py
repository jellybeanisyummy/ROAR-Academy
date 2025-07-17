import numpy as np

# question 1
scalar = 2
matrix = np.array([[6, -9, 1], [4, 24, 8]])

# Multiply the matrix by the scalar
scaled_matrix = scalar * matrix
print("Scaled Matrix:", scaled_matrix)

# question 2
identity_matrix = np.eye(2)
result_matrix = np.dot(identity_matrix, matrix)
print("Result of Identity Matrix multiplied by the original matrix:", result_matrix)

# question 3
matrix_1 = np.array([[4, 3], [3, 2]])
matrix_2 = np.array([[-2, 3], [3, -4]])
dot_product = np.dot(matrix_1, matrix_2)
print("Dot Product of Matrix 1 and Matrix 2:", dot_product)