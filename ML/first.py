from lib2to3.pgen2.driver import load_grammar
from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighborsClassifier
import numpy as np
import pandas as pd

from sklearn.model_selection import train_test_split

iris_dataset = load_iris()

X_train , X_test , y_train, y_test = train_test_split(iris_dataset["data"],iris_dataset["target"],random_state=0);
Kn = KNeighborsClassifier(n_neighbors=1);
Kn.fit(X_train,y_train);
x_new = np.array([[5,2.9,1,0.2]]);
prediction = Kn.predict(x_new);
print(f"predicted target value : {prediction}\n");
print("predicted feature name :{}\n".format(iris_dataset["target_names"][prediction]));
print("Test Score : {:.2f}".format(Kn.score(X_test,y_test)))
