import pandas as pd
import sklearn
from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import DecisionTreeRegressor

model = DecisionTreeRegressor()

traindata = pd.read_csv("/Users/skywalker721/Desktop/dacon-ai-project/lv1/riding/train.csv")
testdata = pd.read_csv("/Users/skywalker721/Desktop/dacon-ai-project/lv1/riding/test.csv")

X_train = traindata.drop(['count'], axis=1)
Y_train = traindata['count']

model.fit(X_train, Y_train)

