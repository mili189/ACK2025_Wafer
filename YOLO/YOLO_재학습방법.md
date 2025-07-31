# YOLO 재학습 방법

## 1️. YOLOv11n 재학습 파일을 구글 Colab에서 실행합니다.



## 1-2. 두 번째 셀의 Roboflow의 데이터셋을 불러오는 코드
<img width="2473" height="1343" alt="image" src="https://github.com/user-attachments/assets/9268a5ef-bb55-4c50-8a08-296bc313b565" />


1. Roboflow 사이트의 해당 프로젝트에서 Versions을 들어갑니다.
2. Version1을 선택하고 Download Dataset을 선택합니다.
3. Download options에서 Show Download Code만 선택하여 Continue를 진행합니다.
4. 해당 코드를 복사하여 붙여넣기 합니다.

## 2. GPU 설정 (런타임 유형 바꾸기)
<img width="848" height="613" alt="image" src="https://github.com/user-attachments/assets/b2df114f-e5c1-4bc1-9300-af9f373e0b88" />


- T4 GPU(무료 버전)이나 A100(유료 버전)을 선택하여 진행합니다.
- CPU의 경우 개인 컴퓨터의 CPU를 사용하기 때문에 느릴 수 있습니다.

## 3. 설정 바꾸기

# 모델 학습
results = model.train(data='/content/Wafer-Defect-Pattern-Detection-3/data.yaml', epochs=100, imgsz=640, batch=8)

- epochs는 학습 횟수라고 생각하시면 됩니다. 100회는 T4 GPU(무료 버전) 상에서 런타임이 끊기거나 너무 오래걸리기 때문에 10회 ~ 20회로 조정하시고 실행하면 됩니다.

import os
import shutil
from google.colab import drive

# Google 드라이브 마운트
drive.mount('/content/drive')

# 원본 경로
source_path = '/content/runs'

# 목적지 경로 (본인이 원하는 경로로 설정하기)
destination_path = '/content/drive/MyDrive/ACK_2025/YOLO/Wafer-result'

# 목적지 경로가 없으면 생성
if not os.path.exists(destination_path):
    os.makedirs(destination_path)

# source_path 경로에 있는 모든 파일과 폴더를 이동
for filename in os.listdir(source_path):
    file_path = os.path.join(source_path, filename)
    if os.path.isfile(file_path) or os.path.isdir(file_path):
        shutil.move(file_path, destination_path)

- 위 코드는 재학습 결과를 구글 드라이브 상에서 저장하는 코드입니다. 목적지 경로를 잘 설정하여 실행하면 됩니다.



