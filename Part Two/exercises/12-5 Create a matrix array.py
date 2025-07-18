import numpy as np

def set_array(L, row, col, order):
    '''Create a matrix array with specified dimensions and order.
    order == True means rows first, False means columns first.
    '''
    if len(L) != row * col:
        raise ValueError("Length of list does not match specified dimensions.")
    
    if order:
        return np.array(L).reshape((row, col), order='C')
    else:
        return np.array(L).reshape((row, col), order='F')
    
aList = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# Create a 3x3 matrix with rows first
matrix_row_first = set_array(aList, 3, 3, True)
print("Matrix with rows first:\n", matrix_row_first)
# Create a 3x3 matrix with columns first
matrix_col_first = set_array(aList, 3, 3, False)
print("Matrix with columns first:\n", matrix_col_first)