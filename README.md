### ACK2025

현재 반도체 공정은 미세공정을 통한 고집적화, 성능향상, 소형화 및 저전력화가 요구되었었고 이를 실현하고 있다. 하지만 공정 미세화에 따라 공정 마진이 감소하면서 반도체 품질 관리의 중요성이 확대되고 있다. 특히 EDS 테스트는 칩의 전기적 특성을 측정하여 칩의 작동 여부를 판별하여 양품과 불량을 선별하는 테스트이다. 이 테스트를 통해 웨이퍼 내 불량 칩의 분포가 특정 패턴을나타내며 공정 내 오류 발생을 분석할 수 있다. 이러한 오류를 보완하여 수율 향상 및 제조 안정성을 확보할 수 있기 때문에 품질 관리가 매우 중요하다.
하지만 기존 산업 현장에서는 고집적화된 웨이퍼 맵을 육안으로 검사하는 방식은 검사 시간을 필연적으로 늘리고 검사자의 주관적 판단은 인적 오류의 가능성을 높일 수 있다. 이를 해결하기 위해서 웨이퍼 맵 상 결함 패턴을 자동으로 탐지하고 분류하는 웨이퍼 결함 패턴 분류 알고리즘을 구현하였다. 이 알고리즘을 통해 생산 라인을 자동화하고 일관된 판별 기준을 확립하여 검사 효율을 극대화하고 판별 오류를 최소화하고자 한다.



주제 : 딥러닝을 활용한 웨이퍼 결함 패턴 판별

- 저자 : 이성재, 용규순, 김민지, 류병석, 오준석, 김영균
  
## 1️⃣ 데이터셋
- MIR-WM811K dataset
- [1] Ming-Ju Wu, Jyh-Shing Roger Jang, and Jui-Long Chen, "Wafer Map Failure Pattern Recognition and Similarity Ranking for Large-Scale Data Sets," in IEEE Transactions on Semiconductor Manufacturing, vol. 28, no. 1, pp. 1-12, Feb. 2015, doi: 10.1109/TSM.2014.2364237.
- [2] MIR-WM811K: Dataset for wafer map failure pattern recognition, 2015 http://mirlab.org/dataset/public/
 
## 2️⃣ 내용 {PPT}
<img width="1280" height="720" alt="슬라이드1" src="https://github.com/user-attachments/assets/21388df7-c2e4-4363-af38-6d13f08c5055" />
<img width="1280" height="720" alt="슬라이드2" src="https://github.com/user-attachments/assets/c7b9df89-8e71-4207-a54d-336685e2f501" />
<img width="1280" height="720" alt="슬라이드3" src="https://github.com/user-attachments/assets/8efe3647-4771-48e9-8ade-a78c11c96712" />
<img width="1280" height="720" alt="슬라이드4" src="https://github.com/user-attachments/assets/f1f9b779-3d67-43ec-bce6-f36dd3f634b7" />
<img width="1280" height="720" alt="슬라이드5" src="https://github.com/user-attachments/assets/016a2846-77fe-467d-9bb7-7ccb97f96feb" />
<img width="1280" height="720" alt="슬라이드6" src="https://github.com/user-attachments/assets/47837c47-2388-4181-8392-b377bb52e231" />
<img width="1280" height="720" alt="슬라이드7" src="https://github.com/user-attachments/assets/70069570-6695-469f-9d38-674658ab26ec" />
<img width="1280" height="720" alt="슬라이드8" src="https://github.com/user-attachments/assets/6a0ff562-3622-4747-9431-51f2618e4bfc" />
<img width="1280" height="720" alt="슬라이드9" src="https://github.com/user-attachments/assets/95f24c63-f5f3-42de-a493-b4cfffbc43cd" />
<img width="1280" height="720" alt="슬라이드10" src="https://github.com/user-attachments/assets/068f2762-1319-422e-9bb7-f6fce8202eba" />
<img width="1280" height="720" alt="슬라이드11" src="https://github.com/user-attachments/assets/d1c47612-0f94-43bd-96bc-0a0078dd00b2" />
<img width="1280" height="720" alt="슬라이드12" src="https://github.com/user-attachments/assets/f3177280-7d9a-4e3a-b3e0-e06e4b7bc193" />
<img width="1280" height="720" alt="슬라이드13" src="https://github.com/user-attachments/assets/472cf04f-dadb-427f-9755-2e98a58880f1" />
<img width="1280" height="720" alt="슬라이드14" src="https://github.com/user-attachments/assets/21c9e164-5dc6-47c1-8415-1bd3d56453ba" />
<img width="1280" height="720" alt="슬라이드15" src="https://github.com/user-attachments/assets/9ba38597-a789-4892-a1b5-895888412456" />
<img width="1280" height="720" alt="슬라이드16" src="https://github.com/user-attachments/assets/c1706119-362f-44d7-bb51-ff0a686a0f81" />
<img width="1280" height="720" alt="슬라이드17" src="https://github.com/user-attachments/assets/c7073fc4-37ae-454e-9606-41f39f676af7" />
<img width="1280" height="720" alt="슬라이드18" src="https://github.com/user-attachments/assets/7b8a6071-37fa-48e5-8beb-300b6e41379e" />
<img width="1280" height="720" alt="슬라이드19" src="https://github.com/user-attachments/assets/1f730c17-e7c8-4c9f-ac55-011166901735" />
<img width="1280" height="720" alt="슬라이드20" src="https://github.com/user-attachments/assets/8c98b819-3154-4cbe-a005-0eab82b3d5ac" />
<img width="1280" height="720" alt="슬라이드21" src="https://github.com/user-attachments/assets/58ac646a-b376-40ad-907d-5fb0e634101b" />



## 3️⃣ 연구 결과

<img width="1662" height="801" alt="image" src="https://github.com/user-attachments/assets/ad20b34a-984a-4048-b542-74844597b323" />


## 4️⃣ 한계 & 보완할 점들

- YOLOv11n과 다중 브랜치 분류 모델로 재학습을 완료한 모델은 검출 및 분류에 한계가 보임
- 웨이퍼 이미지를 추가하여 성능을 높이고 특징 분류의 매커니즘을 향상시켜 오분류 사례를 줄이는 방향으로 보완해야 함





