
# result.png : Version1의 재학습에 대한 손실 그래프와 성능 지표를 보여줍니다.

<img width="2400" height="1200" alt="results" src="https://github.com/user-attachments/assets/18b37a62-6448-42a6-930f-ef2a68b2b19c" />


### 설명

X축 : Epoch(훈련 횟수),  Y축 : Loss Value(손실 값)

loss : 손실 그래프를 의미하며 YOLO 모델이 얼마나 틀렸는지에 대한 수치입니다.

box_loss : 바운딩 박스로 처리된 객체에 대한 위치 예측이 실제 위치와 얼마나 차이가 나는지를 측정합니다.

cls_loss : 객체가 어떤 클래스인지에 대해서 분류할 때의 오류를 측정합니다.

dfl_loss : 정밀 위치 예측을 의미하며 바운딩 박스의 경계 좌표에 대한 오류를 측정합니다.

train loss : 학습 데이터의 손실 그래프

val loss : 검증 데이터의 손실 그래프

precision : 정확도

recall : 재현율

mAP : 객체 탐지 모델이 얼마나 정확하게 예측하였는지를 측정하는 지표

mAP50 : 바운딩 박스가 50%가 걸쳐도 정답으로 판단하는 지표

mAP50-95 : 5%부터 95%까지 5% 간격으로 각각의 mAP를 계산하고 평균값을 도출하는 지표

### 그래프에서 확인할 수 있는 정보

- loss Value가 낮아지면 박스 위치 정확도(box_loss), 분류 성능(cls_loss), 경계선 위치 정밀도(dfl_loss)가 향상되고 오류가 적음을 의미합니다.

- 손실 그래프가 우하향 곡선을 그리면 학습이 잘 진행됨을 의미합니다.

- 학습 손실과 검증 손실이 비슷한 그래프 형태를 가져야 일반화가 용이합니다.

- 만약 학습 손실은 낮아지는데 검증 손실이 오르거나 정체되면 과적합을 생각해볼 필요가 있습니다.


### Version3 결과

- 손실 그래프는 Version1과 마찬가지로 정상적으로 감소하고 있고 과적합은 보이지 않습니다.

- precision이 0.90까지, Recall이 0.87까지 상승함

- mAP50은 0.92으로 높은 성능을 보여줌, mAP50-95은 0.82으로 적당한 성능을 나타냄.

- 모델이 효과적으로 학습되었고 성능과 위치 정밀도도 괜찮은 정도라고 보여짐

### Version3 개선 사항

- Recall을 0.90까지 올리고 싶음

- mAP50-95를 0.85 ~ 0.90까지 올리고 싶음


# confusion_matrix.png : Version1의 재학습에 대한 혼동 행렬을 보여줍니다.

<img width="3000" height="2250" alt="confusion_matrix" src="https://github.com/user-attachments/assets/159c6751-f5d7-4d51-8c41-ee356340b684" />


<img width="3000" height="2250" alt="confusion_matrix_normalized" src="https://github.com/user-attachments/assets/2ef4ddd9-10d1-453d-b427-253fe118ba8a" />


### Verison3 혼동행렬 결과

- Center, Donut, Edge-Ring, Random 클래스에 대해서 0.97 이상의 정확도로 분류함

- Edge-Loc, Loc, Scratch가 Version1에 비해 상대적으로 정확도가 상승함. 데이터 증강 기법이 정확도 상승에 기여하였다고 생각함

- Near-full의 정확도가 0.92 정도로 정확도가 올라감. 데이터 증강 기법을 다양하게 적용시킨 부분이 긍정적으로 작용함



### Version3 개선 사항

- Edge-Loc와 Loc에 대한 개선이 필요함

- 더 이상 유의미한 증강 기법이 없기 때문에 다른 부분에서 찾아야 함









