import os
import cv2
from ultralytics import YOLO
import torch


# CUDA 설정
device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")

# YOLO 모델 로드
yolo_model = YOLO("best_v1.pt")

# 데이터 경로 설정
input_root = "YOLO_Dataset"
output_root = "cropped_objects/"

# 클래스 별 폴더 순환
for class_name in os.listdir(input_root):
    category_path = os.path.join(input_root, class_name)
    if not os.path.isdir(category_path):
        continue

    # 클래스 별 저장 경로 설정 및 출력 폴더 생성
    category_output_dir = os.path.join(output_root, class_name)
    os.makedirs(category_output_dir, exist_ok=True)

    print(f"현재 클래스: {class_name}")

    # 클래스 폴더 내 이미지 순환
    for image_name in os.listdir(category_path):
        if not image_name.lower().endswith(('.jpg', '.jpeg', '.png')):
            continue

        image_path = os.path.join(category_path, image_name)
        img = cv2.imread(image_path)


        results = yolo_model.predict(image_path, imgsz=640, conf=0.5, save=False, show=False)
        detections = results[0].boxes

        for idx, box in enumerate(detections):
            x1, y1, x2, y2 = map(int, box.xyxy[0].cpu().numpy())
            cropped_object = img[y1:y2, x1:x2]


            save_path = os.path.join(category_output_dir, f"{os.path.splitext(image_name)[0]}_object_{idx}.png")


            cv2.imwrite(save_path, cropped_object)
            print(f"저장 : {save_path}")


print(" 모든 이미지가 이미지 분리가 완료되었습니다.")





























