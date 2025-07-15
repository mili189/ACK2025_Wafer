# 제목 : Wafer Bin Map 시각화
# 목적 : WM811K.pkl 파일의 웨이퍼 데이터 시각화
# 작성일 : 2025-07-14
# 최근 업데이트일 : 2025-07-15


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# WM811K 파일 불러오기 (WM811K 파일의 각 행은 각각의 웨이퍼 정보를 나타냄)
df=pd.read_pickle("WM811K.pkl") 

# df 데이터 프레임의 전체 구조를 요약해서 보여줌
df.info()

# 배열이나 리스트인 경우 첫 번째 원소를 문자열로 반환하는 함수 정의
def normalize_label(x):
    if isinstance(x, np.ndarray):
        return str(x[0])
    elif isinstance(x, (list, tuple)):
        return str(x[0])
    else:
        return str(x)

# 위 함수를 trainTestLabel 리스트에 적용, 문자열이 아닌 np.ndarray(['Training']) 같은 이상값을 모두 'Training' 형태로 통일
df['trainTestLabel'] = df['trainTestLabel'].apply(normalize_label)


# 정규화 확인 (trainTestLabel의 모든 값의 클래스가 str이어야 함)
print(df['trainTestLabel'].apply(type).value_counts())


# 훈련용 데이터와 테스트 데이터를 구분하여 인덱스 저장
trainIdx=df[df['trainTestLabel']=='Training'].index
testIdx=df[df['trainTestLabel']=='Test'].index

# 각 데이터에서 존재하는 결함 유형 목록을 추출하여 분석
trainFailureType=df.loc[trainIdx,'failureType']     # 훈련용 데이터의 결함 유형
testFailureType=df.loc[testIdx,'failureType']       # 테스트 데이터의 결함 유형
uniqueType=df.loc[trainIdx,'failureType'].unique()  # 훈련용 데이터에서 나타나는 결함 유형 중복없이 저장
uniqueType.sort()   # 결함 유형 정렬
print(uniqueType)   # 결함 유형 출력

# Wafer map 시각화 예시
idx=trainFailureType[trainFailureType==uniqueType[0]].index # 첫 번째 결함 유형의 데이터를 선택하여 저장 (Center Type)
exampleIdx=idx[0]   # 첫 번째 결함 유형의 데이터의 첫 예시를 저장
plt.imshow(df.iloc[exampleIdx]['waferMap'],)    # df의 위치 접근
plt.title('WaferMap')   # 시각화 창 생성
plt.show() 

