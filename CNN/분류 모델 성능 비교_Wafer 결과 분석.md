
# 2025-08-05 분류 모델 성능 비교


## 해당 파일에 대해서
- 결함 패턴 이미지 데이터셋 + 바운딩 박스 좌표 데이터셋을 바탕으로 여러 NN 모델과 전이학습 모델을 각각 훈련시켜 정확도, 손실 그래프와 혼동 행렬을 출력시켰습니다.






## 성능 비교 결과

<img width="2121" height="728" alt="image" src="https://github.com/user-attachments/assets/b1aa8328-e7ba-4b7d-adb8-9be6db7dcac8" />

<img width="1116" height="1043" alt="image" src="https://github.com/user-attachments/assets/6750c9ea-ef1c-4612-ae46-78893fcbccbf" />

### 결과

- 총 11개의 분류 모델을 활용하였고 가장 안정적인 모델은 VGG16 모델입니다.

### 장점

- Loc를 제외한 모든 클래스에 대해서 85%의 분류 성능을 확인할 수 있습니다.

- 정확도 그래프와 손실 그래프에서 훈련 셋과 테스트 셋이 평행하게 움직이기 때문에 일반화가 용이하고 과적합이 제어가 되고 있습니다.

### 단점

- 모든 분류 모델이 가지고 있는 취약점이 있습니다. Loc 패턴을 잘 학습하지 못한다는 것입니다. 특히 거의 모든 모델들이 Loc 패턴을 Center 패턴이라고 인식한다는 점이었습니다.

- Loc, Center와 같이 군집형 패턴은 시각적 형태만으로 판단하기 어렵기 때문에 이러한 결과가 나왔습니다.

- 바운딩 박스의 좌표를 같이 입력 데이터로 활용하였지만 위치 구분이 잘 이루어지지 않았습니다.




## 앞으로의 개선 방향

1. 바운딩 박스의 좌표 데이터에 대한 학습 강화
- Loc와 Center를 구분하지 못하는 가장 큰 이유는 위치 학습이 덜 이루어졌다고 생각합니다. 그래서 위치 학습을 보완하는 방향으로 모델을 구성할 예정입니다.

2. Loc, Edge-Loc 클래스의 통합
- 전체적으로 Loc와 Edge-Loc 패턴의 정확도가 많이 낮습니다. 그래서 해당 문제를 해결하기 위해 라벨링 단계에서 가장 모호했던 Edge-Loc와 Loc 클래스를 통합하여 패턴 혼동을 줄이는 방향을 생각해봤습니다.
- 하지만 WM811K 데이터셋에 반하는 방향이기 때문에 심사숙고해야 될 것 같다고 생각합니다.








## 2025-08-06 2회차 성능 비교 결과

<img width="843" height="602" alt="image" src="https://github.com/user-attachments/assets/59b72a76-82a1-4e2d-b6ca-bb4e538a16ba" />








## 2025-08-06 3회차 성능 비교 결과


<img width="868" height="599" alt="image" src="https://github.com/user-attachments/assets/d4aeb2c2-cf42-492d-b971-25ffeda4b6c5" />

- 바운딩 박스의 극좌표계 수치(반지름, 각도)를 추가하여 입력


<img width="1065" height="1051" alt="image" src="https://github.com/user-attachments/assets/39182cf1-cf53-4bad-b803-08fe54ebb883" />

- DenseNet121 모델 기준 Loc 패턴의 정확도가 향상된 것으로 확인됨



## 개선 방향

- 극좌표계 수치 입력을 중심으로 새로운 향상 방법을 연구할 필요가 있어 보임



















