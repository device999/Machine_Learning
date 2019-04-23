
import matplotlib.pyplot as plt
import numpy as np

def plot3():    
    x = np.random.random_integers(10,size=(5))
    y = np.random.random_integers(10,size=(5))
    plt.plot(x,y,color='green')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Visualization')
    plt.show()

def plot6(x1,y1,x2,y2):
    plt.plot(x1,y1,linewidth=2,color='green')
    plt.plot(x2,y2,linewidth=6,color='red')
    plt.title('Visualization')
    plt.show()
    
def plot7(x1,y1,x2,y2):
    plt.plot(x1,y1,linewidth=2,linestyle='--',color='green')
    plt.plot(x2,y2,linewidth=1,linestyle='dashed',color='red')
    plt.title('Visualization')
    plt.show()

def plot8(x1,y1,x2,y2):
    plt.plot(x1,y1,linewidth=2,linestyle='--',color='green',marker='o',
    markerfacecolor='green', markersize=6)
    plt.plot(x2,y2,linewidth=1,linestyle='dashed',marker='o', 
    markerfacecolor='red', markersize=6,color='red')
    plt.title('Visualization')
    plt.show()

def plot10(x1,y1,x2,y2):
    plt.plot(x1, y1,'b*', x2, y2, 'ro')
    plt.show()

def plot11(x1,y1,x2,y2):
    plt.plot(x1, x1,'b*', x2, x2, 'ro')
    plt.show()
    return 1

if __name__ == "__main__":
    x1 = np.random.randint(100,size=(10))
    y1 = np.random.randint(100,size=(10))
    x2 = np.random.randint(100,size=(10))
    y2 = np.random.randint(100,size=(10))
    plot11(x1,y1,x2,y2)