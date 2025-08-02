
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

### Version1 개선 사항

- Recall을 0.90까지 올리고 싶음

- mAP50-95를 0.85 ~ 0.90까지 올리고 싶음


# confusion_matrix.png : Version1의 재학습에 대한 혼동 행렬을 보여줍니다.

<img width="3000" height="2250" alt="confusion_matrix" src="https://github.com/user-attachments/assets/9d79c694-c3a8-4655-ac02-bcdfec21f948" />

<img width="3000" height="2250" alt="confusion_matrix_normalized" src="https://github.com/user-attachments/assets/46c0635d-3921-4c2e-903d-8d6f0a407dce" />

### Verison1 결과

- Center, Donut, Edge-Ring, Random 클래스에 대해서 0.97의 정확도로 분류함

- Edge-Loc, Loc은 상대적으로 낮은 정확도를 나타냄. 심지어 background와의 혼동이 심함

- Near-full의 정확도가 0.85 정도로 머물러 있는 이유는 데이터가 가장 적을 뿐더러 현 Version에서 증강 기법을 적용하지 않았기 때문이라고 생각됨



### Version1 개선 사항

- Edge-Loc와 Loc에 대한 개선이 필요함

- 새로운 Version에서는 데이터 증강 기법을 활용할 필요가 있음









