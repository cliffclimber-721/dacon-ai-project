import pandas as pd
import graphviz
from sklearn import *
from sklearn.tree import DecisionTreeRegressor

traindata = pd.read_csv("/Users/skywalker721/Desktop/dacon-ai-project/lv1/riding/train.csv")
testdata = pd.read_csv("/Users/skywalker721/Desktop/dacon-ai-project/lv1/riding/test.csv")

X_train = traindata.drop(['count'], axis=1)
Y_train = traindata['count']

model = DecisionTreeRegressor()
model.fit(X_train, Y_train)

