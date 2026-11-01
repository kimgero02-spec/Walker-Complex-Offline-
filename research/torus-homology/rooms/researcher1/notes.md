# researcher1 작업 노트 (라운드 1)
- homology.py: 자체 정수 SNF + 모델 생성기 (CW 수동, Δ 수동/Kuhn N=1, 단체: Kuhn N>=3, union-find 격자, 7꼭짓점)
- results.json: 실행 결과
- 교차검증: sympy smith_normal_form 과 d2 대각성분 일치 (T 3x3: [1], K 3x3: [1,2]); 7꼭짓점 ker d2 생성원 계수 전부 ±1 (기본류)
- 관찰: Kuhn N=2 (2x2 격자)는 단체 복합체가 아님(같은 꼭짓점쌍 변 중복) 그러나 Δ-복합체로서 호몰로지는 정상.
- 관찰: 모든 T^n 모델에서 CW 경계사상 전부 0 → H_k = Z^{C(n,k)}; 클라인 병은 d2 의 SNF 에 2 가 등장 → Z/2 꼬임.
