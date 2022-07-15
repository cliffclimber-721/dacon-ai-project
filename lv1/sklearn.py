import pandas as pd
from sklearn import *

traindata = pd.read_csv("/Users/skywalker721/Desktop/dacon-ai-project/lv1/riding/train.csv")
testdata = pd.read_csv("/Users/skywalker721/Desktop/dacon-ai-project/lv1/riding/test.csv")

X_train = traindata.drop(['count'], axis=1)
Y_train = traindata['count']

model = DecisionTreeClassifier()
model.fit(X_train, Y_train)

