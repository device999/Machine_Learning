import numpy as np

if __name__ == '__main__':
    # Write a NumPy program to create a 3x3 matrix with values ranging from 2 to 10.
    # Write a NumPy program to create a 2x2 empty matrix.
    matrix1 =  np.arange(2,11).reshape(3,3)
    print(matrix1)
    matrix2 = np.random.randint(100,size= (2,2))
    print(matrix2)
    # Write a NumPy program to reverse an array (first element becomes last).
    print(np.flip(matrix2[::-1],1))
    print("------------------------------")
    # Write a NumPy program to add two arrays A and B of sizes (3,3) and (,3).
    matrixFirst = np.random.randint(10,size=(3,3))
    matrixSecond = np.arange(2,5)
    print(matrixFirst)
    print(matrixSecond)
    print("------------------------------")
    print(matrixFirst+matrixSecond)
    print("------------------------------")
    # Write a NumPy program to get the unique elements of an array.
    uniqueArray=np.unique(np.array([10,10,20,20,30,50,60,60]))
    print(uniqueArray)
    print("------------------------------")
    # Write a NumPy program to extract first element of the second row and fourth element of fourth row from a given (4x4) array.
    matrix4x4 = np.random.randint(100,size= (4,4))
    print(matrix4x4)
    matrix4x4[1,0] = matrix4x4[1,0]-matrix4x4[3,3]
    print(matrix4x4)
    print("------------------------------")