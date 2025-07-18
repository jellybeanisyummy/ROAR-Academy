import numpy as np

def swap_rows(matrix, row1_index, row2_index):
    """Swap two rows in a matrix."""
    # sanity check for valid row indices
    if row1_index < 0 or row2_index < 0 or row1_index >= len(matrix) or row2_index >= len(matrix):
        raise IndexError("Row indices out of bounds.")
    if len(matrix[row1_index]) != len(matrix[row2_index]):
        raise ValueError("Rows must have the same number of columns to swap.")

    m = matrix.copy()
    matrix[row1_index], matrix[row2_index] = m[row2_index], m[row1_index]
    return matrix

def swap_columns(matrix, col1_index, col2_index):
    """Swap two columns in a matrix."""
    # sanity check for valid column indices
    if col1_index < 0 or col2_index < 0 or col1_index >= len(matrix[0]) or col2_index >= len(matrix[0]):
        raise IndexError("Column indices out of bounds.")
    if len(matrix[col1_index]) != len(matrix[col2_index]):
        raise ValueError("Matrix must be square to swap columns.")

    # switch the columns by going to each row and switching the numbers in the right columns
    for row in matrix:
        row[col1_index], row[col2_index] = row[col2_index], row[col1_index]
    
    return matrix

matrix1 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
matrix2 = np.array([[10, 11, 12], [13, 14, 15], [16, 17, 18]])

print(swap_rows(matrix1, 0, 2))  # Swaps first and last rows
print(swap_columns(matrix2, 0, 1))  # Swaps first and second columns