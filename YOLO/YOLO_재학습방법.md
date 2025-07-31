# YOLO 재학습 방법

## 참고 영상
- 유튜브 : https://www.youtube.com/watch?v=RaY_9i6XOos

## 1️. YOLOv11n 재학습 파일을 구글 Colab에서 실행합니다.



## 1-2. 두 번째 셀의 Roboflow의 데이터셋을 불러오는 코드
<img width="2473" height="1343" alt="image" src="https://github.com/user-attachments/assets/9268a5ef-bb55-4c50-8a08-296bc313b565" />


1. Roboflow 사이트의 해당 프로젝트에서 Versions을 들어갑니다.
2. Version1을 선택하고 Download Dataset을 선택합니다.
3. Download options에서 Show Download Code만 선택하여 Continue를 진행합니다.
4. 해당 코드를 복사하여 붙여넣기 합니다.

<img width="1488" height="291" alt="image" src="https://github.com/user-attachments/assets/6d16d4cb-cf6b-49c0-ad2b-dfcce3ac12f8" />
- 해당 코드의 출력 결과는 위 이미지처럼 출력되어야 합니다. 이후의 코드에서 data.yaml을 사용해야 하기 때문입니다.

## 2. GPU 설정 (런타임 유형 바꾸기)
<img width="848" height="613" alt="image" src="https://github.com/user-attachments/assets/b2df114f-e5c1-4bc1-9300-af9f373e0b88" />


- T4 GPU(무료 버전)이나 A100 GPU(유료 버전)을 선택하여 진행합니다.
- CPU의 경우 개인 컴퓨터의 CPU를 사용하기 때문에 느릴 수 있습니다.

## 3. 설정 바꾸기

<img width="1343" height="115" alt="image" src="https://github.com/user-attachments/assets/c182f1c9-f476-409f-8472-8731193cd9ae" />

- epochs는 학습 횟수라고 생각하시면 됩니다. 100회는 T4 GPU(무료 버전) 상에서 런타임이 끊기거나 너무 오래걸리기 때문에 10회 ~ 20회로 조정하시고 실행하면 됩니다.

<img width="1342" height="722" alt="image" src="https://github.com/user-attachments/assets/f932ed3b-be9a-4263-9f0b-5d6afb00e3cf" />

- 위 코드는 재학습 결과를 구글 드라이브 상에서 저장하는 코드입니다. 목적지 경로를 잘 설정하여 실행하면 됩니다.



