
import pandas as panda
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

dataSet = panda.read_csv("iris.data")
x = dataSet.iloc[:, :-1].values
labeledY = dataSet.iloc[:, 4].values
print(labeledY)

label = {"Iris-setosa": 0, "Iris-versicolor": 1, "Iris-virginica": 2}
cleanY = [label[x] for x in labeledY]
print(cleanY)
X_train, X_test, y_train, y_test = train_test_split(x, cleanY, test_size=0.25, shuffle=True, random_state=0)
