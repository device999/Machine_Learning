import numpy as np

if __name__ == "__main__":
    randomList = np.random.randint(0, 50, 20)
    print(randomList)
    print("------------------------------")
    # Write a NumPy program to get the n largest values of an array.
    print (randomList[np.argsort(randomList)[-1:]])
    # Write a NumPy program to find the most frequent value in an array.
    print("------------------------------")    
    print(np.bincount(randomList).argmax())
