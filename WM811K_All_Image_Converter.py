# 제목 : Wafer Bin Map 데이터 필터링 및 이미지 변환
# 목적 : WM811K.pkl 파일의 웨이퍼 데이터의 필터링 수행 및 이미지 변환
# 작성일 : 2025-07-20
# 최근 업데이트일 : 2025-07-20


# 라이브러리 설정
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import os
from tqdm import tqdm
import io
import gc
import shutil


# 웨이퍼 빈맵 데이터 불러오기
WBM_Source = pd.read_pickle('WM811K.pkl')


# 필터링 함수
def remove_00(x):
  try:
    arr = list(x)

  except Exception:
    return False
  
  return len(arr) == 2 and arr[0] == 0 and arr[1] == 0

# mask 설정
mask = ~(
    WBM_Source['failureType'].apply(remove_00) &
    WBM_Source['trainTestLabel'].apply(remove_00)
)

# 필터링
WBM_Filtered = WBM_Source[mask].reset_index(drop=True)


# 데이터의 용량 비교
print(f"원본: {WBM_Source.shape[0]}, 필터링 후: {WBM_Filtered.shape[0]}")

# failureType의 고유값 확인
print(WBM_Filtered['failureType'].astype(str).unique())

# 각 failureType의 유형별 빈도 확인
failure_counts = WBM_Filtered['failureType'].astype(str).value_counts().to_dict()
print(failure_counts)




# 출력 폴더 설정
output_root = 'WBM_Image_Dataset'
os.makedirs(output_root, exist_ok=True)


# 웨이퍼 맵 Viridis 이미지 변환 및 640x640 크기로 저장하는 함수
def save_wafer_map_image(array, save_path, size = (640,640)):

    # 1. 웨이퍼 맵 시각화
    fig = plt.figure(figsize=(10,10)) # figsize(10,10): 고해상도 저장
    plt.axis('off')
    plt.imshow(array, cmap = 'viridis',interpolation='nearest') # Die 간 경계를 선명하게 유지 (흐림 방지)

    # 2. 이미지 저장을 위한 메모리 버퍼 사용    
    buf = io.BytesIO()
    plt.savefig(buf, format='png', bbox_inches='tight', pad_inches=0, dpi=300)
    plt.close()

    # 3. Figure 정리 및 메모리 해제
    plt.clf()       # Figure 내용 삭제
    plt.close(fig)  # Figure 객체 종료
    buf.seek(0)     # 버퍼 읽기 준비

    # PIL을 활용한 이미지 Resize
    img = Image.open(buf).convert('RGB')
    img = img.resize(size, Image.LANCZOS)
    img.save(save_path)
    img.close()
    buf.close()

    # 사이클 참조, 내부 참조 보유 등으로 사용되는 메모리 회수
    gc.collect()





# tqdm으로 인한 진행 상황을 보여주며 저장
for i in tqdm(range(len(WBM_Filtered))):
    label = WBM_Filtered.iloc[i]['failureType']
    wafer = WBM_Filtered.iloc[i]['waferMap']

    # 라벨 디렉터리 생성
    label_dir = os.path.join(output_root, label)
    os.makedirs(label_dir, exist_ok=True)

    # 저장 경로
    save_path = os.path.join(label_dir, f"{i}.png")

    # 저장
    save_wafer_map_image(wafer, save_path)




















