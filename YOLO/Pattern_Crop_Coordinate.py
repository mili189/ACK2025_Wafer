import os
import cv2
from ultralytics import YOLO
import torch
import pandas as pd


# CUDA 설정
device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")

# YOLO 모델 로드
yolo_model = YOLO("best_v3.pt")

# 데이터 경로 설정
input_root = "YOLO_Dataset"     # 입력 데이터셋은 각 클래스마다 폴더로 구분되어야 할 것
output_root = "Pattern_Cropped_Coordinated_Dataset_v3/"
os.makedirs(output_root, exist_ok=True)

# 결과 저장 리스트
bbox_dataset = []

# 클래스별 폴더 순회
for class_name in os.listdir(input_root):
    class_name_path = os.path.join(input_root, class_name)
    if not os.path.isdir(class_name_path):
        continue

    # 데이터 출력 경로에서 클래스 별 폴더 생성
    class_name_output_dir = os.path.join(output_root, class_name)
    os.makedirs(class_name_output_dir, exist_ok=True)

    # 클래스 폴더 별 이미지 순회
    for image_name in os.listdir(class_name_path):
        if not image_name.lower().endswith(('.jpg', '.jpeg', '.png')):
            continue

        image_path = os.path.join(class_name_path, image_name)
        img = cv2.imread(image_path)
        h, w = img.shape[:2]    # height, width 변수

        # YOLO 예측 수행
        results = yolo_model.predict(image_path, imgsz=640, conf=0.5, save=False)

        detections = results[0].boxes   # 바운딩 박스들의 좌표, 클래스, 신뢰도 정보

        for idx, box in enumerate(detections):
            x1, y1, x2, y2 = map(int, box.xyxy[0].cpu().numpy())    # 바운딩 박스 좌표
            cropped_image = img[y1:y2, x1:x2]     # 결함 패턴 이미지
            save_name = f"{os.path.splitext(image_name)[0]}_obj{idx}.png"
            save_path = os.path.join(class_name_output_dir, save_name)

        # 이미지 저장   
        cv2.imwrite(save_path, cropped_image)


        # 바운딩 박스 중심과 크기 (정규화)
        x_center = ((x1 + x2) / 2) / w
        y_center = ((y1 + y2) / 2) / h
        bbox_w = (x2 - x1) / w
        bbox_h = (y2 - y1) / h
        bbox_dataset.append({
            "original_image": image_name,
            "cropped_image": save_name,
            "class": class_name,
            "x_center_norm": round(x_center, 6),
            "y_center_norm": round(y_center, 6),
            "width_norm": round(bbox_w, 6),
            "height_norm": round(bbox_h, 6)
            })


# 결과 CSV 저장
df = pd.DataFrame(bbox_dataset)
df.to_csv("bbox_info.csv", index=False)
print("✅ bbox_info.csv 저장 완료.")
