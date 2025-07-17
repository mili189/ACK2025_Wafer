# 제목 : Wafer Bin Map 이미지 변환
# 목적 : WM811K.pkl 파일의 웨이퍼 데이터 이미지 변환 작업 수행
# 작성일 : 2025-07-17
# 최근 업데이트일 : 2025-07-17


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import os
from tqdm import tqdm


# 데이터 불러오기
df = pd.read_pickle("WM811K.pkl")


# 라벨 정규화
def normalize_label(x):
    if isinstance(x, np.ndarray):
        return str(x[0])
    elif isinstance(x, (list, tuple)):
        return str(x[0])
    else:
        return str(x)


 
df['trainTestLabel'] = df['trainTestLabel'].apply(normalize_label)
df['failureType'] = df['failureType'].apply(normalize_label)


# 출력 폴더 설정
output_root = "WaferBinMapImage_Dataset"
os.makedirs(output_root, exist_ok=True)


# 웨이퍼 맵 Viridis 이미지 변환 및 640x640 크기로 저장하는 함수
def save_wafer_map_image(array, save_path, size = (640,640)):
    
    # 1. 웨이퍼 맵 시각화
    plt.figure(figsize=(10,10)) # figsize(10,10): 고해상도 저장
    plt.axis('off')
    plt.imshow(array, cmap = 'viridis',interpolation='nearest') # Die 간 경계를 선명하게 유지 (흐림 방지)
    
    # 2. 임시 저장
    temp_path = "temp.png"
    plt.savefig(temp_path, bbox_inches='tight', pad_inches=0, dpi=300)  # dpi300 : 이미지 선명도 확보
    plt.close

    # 3. Resize 및 최종 저장
    img = Image.open(temp_path).convert('RGB')
    img = img.resize(size, Image.LANCZOS)   # 640x640 크기 재조정
    img.save(save_path)
    os.remove(temp_path)




# tqdm으로 인한 진행 상황을 보여주며 저장
for i in tqdm(range(len(df))):
    label = df.iloc[i]['failureType']
    wafer = df.iloc[i]['waferMap']

    # 라벨 디렉터리 생성
    label_dir = os.path.join(output_root, label)
    os.makedirs(label_dir, exist_ok=True)

    # 저장 경로
    save_path = os.path.join(label_dir, f"{i}.png")

    # 저장
    save_wafer_map_image(wafer, save_path)










