import pandas as pd
import numpy as np
from pandas import DataFrame

traindata = pd.read_csv("/Users/skywalker721/Desktop/dacon-ai-project/lv1/riding/train.csv")
testdata = pd.read_csv("/Users/skywalker721/Desktop/dacon-ai-project/lv1/riding/test.csv")

# nan 은 데이터에 값이 없음을 의미하고 null 과 같은 개념
df = pd.DataFrame({
    'name':['kwon', 'shin', 'cho'],
    'age':[30, np.nan, 19],
    'class':[np.nan, np.nan, 1]
})

# isnull() 메서드를 사용하면 Dataframe에서 nan 값을 확인할 수 있다
print(df.isnull())
print("="*40)

# sum() 을 추가하면 각 열별 missing value 수 확인 가능
print(df.isnull().sum())
print("="*40)

# info() 를 사용하면 기본 정보를 알 수 있다.
print(df.info())
print("="*40)

# dropna() 는 Dataframe 객체에서 행을 삭제
# fillna() 는 행 추가
print(df.dropna())
print("="*40)
print(df.fillna(0))
print("="*40)