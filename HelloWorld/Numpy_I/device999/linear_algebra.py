import numpy as np

if __name__ == '__main__':
    # Write a NumPy program to compute the multiplication of two given matrixes.
    matrix1 =  np.random.randint(10,size=(3,3))
    matrix2 =  np.random.randint(10,size=(3,3))
    print(matrix1)
    print(matrix2)
    print(matrix1*matrix2)
    print("------------------------------")
    # Write a NumPy program to compute the determinant of an array. 
    matrixFull = np.random.randint(5,size=(3,3))
    result =  np.linalg.det(matrixFull)
    print(matrixFull)
    print(result)
    print("------------------------------")
    # Write a NumPy program compute the inverse of a given matrix.
    print("------------------------------")
    inverseMatrix =  np.linalg.inv(matrixFull)
    print(inverseMatrix)
    # Write a NumPy program compute the sum of the diagonal element of a given array.
    print("------------------------------")
    diagonalSum = np.trace(matrixFull)
    print(diagonalSum)