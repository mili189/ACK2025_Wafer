import os, cv2, torch, pandas as pd, numpy as np
from ultralytics import YOLO

device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
yolo_model = YOLO("best_v3.pt")

input_root  = "YOLO_Dataset"
output_root = "Pattern_Image_Coordinated_Dataset_v5"
os.makedirs(output_root, exist_ok=True)

bbox_dataset = []

def clip_box(x1,y1,x2,y2,w,h):
    return max(0,x1), max(0,y1), min(w,x2), min(h,y2)

# 각도 구간(bin) 설정 (좌표 브랜치 임베딩용)
N_RAD_BINS = 8
N_SEC_BINS = 16
TWO_PI = 2*np.pi
EPS = 1e-6

for class_name in os.listdir(input_root):
    class_dir = os.path.join(input_root, class_name)
    if not os.path.isdir(class_dir):
        continue

    out_dir = os.path.join(output_root, class_name)
    os.makedirs(out_dir, exist_ok=True)

    for image_name in os.listdir(class_dir):
        if not image_name.lower().endswith((".jpg",".jpeg",".png")):
            continue

        image_path = os.path.join(class_dir, image_name)
        img = cv2.imread(image_path)
        if img is None:
            continue
        H, W = img.shape[:2]
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # 1) 웨이퍼 중심/반경 추정 (실패 시 이미지 중심/대략 반경)
        

        # 정규화 중심/반경 (전부 이미지 크기 기준으로 0~1)
        wafer_cx = 0.5
        wafer_cy = 0.5
        # 반경도 0~1로 정규화 (W,H가 다르면 min 사용)
        wafer_r_norm = 0.5

        # 2) YOLO 예측
        results = yolo_model.predict(image_path, imgsz=640, conf=0.5, save=False)
        dets = results[0].boxes

        for idx, box in enumerate(dets):
            # --- 바운딩박스 픽셀 좌표 확보/클리핑 ---
            x1, y1, x2, y2 = map(int, box.xyxy[0].cpu().numpy())
            x1, y1, x2, y2 = clip_box(x1,y1,x2,y2,W,H)
            if x2 <= x1 or y2 <= y1:
                continue

            # --- 크롭 저장 (← 들여쓰기 수정: 박스마다 저장) ---
            cropped = img[y1:y2, x1:x2]
            save_name = f"{os.path.splitext(image_name)[0]}_obj{idx}.png"
            save_path = os.path.join(out_dir, save_name)
            cv2.imwrite(save_path, cropped)

            # --- 정규화된 박스 특징 (CSV 기본 4개) ---
            xc = ((x1 + x2) / 2) / W
            yc = ((y1 + y2) / 2) / H
            bw = (x2 - x1) / W
            bh = (y2 - y1) / H

            # --- 웨이퍼 중심 기준 반경/각도 (정규화) ---
            dx = xc - wafer_cx
            dy = yc - wafer_cy
            dist_norm = np.sqrt(dx*dx + dy*dy)                          # 이미지 정규화 좌표에서의 거리
            r_norm = dist_norm / max(wafer_r_norm, EPS)                  # 웨이퍼 반경으로 나눠 0~1
            r_norm = float(np.clip(r_norm, 0.0, 1.0))

            theta = float(np.arctan2(dy, dx))                            # 라디안(-π~π)
            sin_th, cos_th = float(np.sin(theta)), float(np.cos(theta))

            # --- 파생 특징 (좌표 브랜치에 유용) ---
            area_norm   = float(bw * bh)
            aspect_log  = float(np.log((bw+EPS)/(bh+EPS)))
            edge_margin = float(1.0 - r_norm)

            # --- (선택) 구간화(임베딩용) ---
            rad_bin = int(np.clip(np.floor(r_norm * N_RAD_BINS), 0, N_RAD_BINS-1))
            sec_bin = int(np.floor(((theta % TWO_PI) / TWO_PI) * N_SEC_BINS))

            bbox_dataset.append({
                "original_image": image_name,
                "cropped_image": save_name,
                "class": class_name,

                # 기본 좌표(정규화)
                "x_center_norm": round(xc, 6),
                "y_center_norm": round(yc, 6),
                "width_norm":  round(bw, 6),
                "height_norm": round(bh, 6),

                # 웨이퍼 기준 극좌표 (정규화 반경 + 각도)
                "wafer_cx_norm": round(wafer_cx, 6),
                "wafer_cy_norm": round(wafer_cy, 6),
                "wafer_r_norm":  round(wafer_r_norm, 6),
                "r_norm":        round(r_norm, 6),
                "theta_rad":     round(theta, 6),
                "sin_theta":     round(sin_th, 6),
                "cos_theta":     round(cos_th, 6),

                # 파생 특징
                "area_norm":     round(area_norm, 6),
                "aspect_log":    round(aspect_log, 6),
                "edge_margin":   round(edge_margin, 6),

                # 임베딩용 구간
                "rad_bin": rad_bin,
                "sec_bin": sec_bin
            })

# CSV 저장
df = pd.DataFrame(bbox_dataset)
df.to_csv("bbox_info_v5.csv", index=False)
print("✅ bbox_info_v5.csv 저장 완료.")