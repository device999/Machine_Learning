import matplotlib.pyplot as plt
import numpy as np

def task1(x,y):
    plt.scatter(x,y, color='r')
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.title("Scatter plot")
    plt.show()

def task3(x,y):
    areas = np.random.randint(50,size=(100))
    colors = np.random.randint(1000,size=(100))
    plt.scatter(x,y,s=areas,c=colors)
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.title("Scatter plot")
    plt.show()

def task4(x,y):
    z = np.random.randint(500,size=(100))
    plt.scatter(z,x,color='y',label='Math marks')
    plt.scatter(z,y,color='r',label='Math marks')
    plt.xlabel('Marks Range')
    plt.ylabel('Marks Scored')
    plt.legend()
    plt.show()


if __name__ == "__main__":
    x1 = np.random.randint(500,size=(100))
    y1 = np.random.randint(500,size=(100))
    task4(x1,y1)