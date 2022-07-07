import pandas as pd
import numpy as np

# 데이터 불러오기
traindata = pd.read_csv("/Users/skywalker721/Desktop/dacon-ai-project/lv1/riding/train.csv")
testdata = pd.read_csv("/Users/skywalker721/Desktop/dacon-ai-project/lv1/riding/test.csv")

# shape을 이용해 train과 test의 행열 개수를 파악
print(traindata.shape)
print(testdata.shape)

# 상위 5개 데이터 확인 -> head()
# 하위 5개 데이터 확인 -> tail()
print("======= show traindata =======")
print(traindata.head())
print("======= show testdata =======")
print(testdata.head())