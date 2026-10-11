# researcher2 (반례꾼) 라운드 2 노트

- cert.py: 극대 완전이분쌍 목록 + 마진 LP 로 R^d 배치 탐색 (휴리스틱). verify.py: 유리수 정확 검증.
- 검증 완료 (정확 유리수 검사 통과): C5[K2] R^3, comp(C7)=atlas#1170 R^2, atlas#878/#998/#1002/#1101 R^2, C7[K2] R^3.
- 진행: C5[K3] R^5 (c5k3.py 는 scratchpad).
- 증명 메모: tau<=chi (색칠 -> B0 -> S^{k-1}), tau(K_n)=n, tau>=omega, tau(G-e)<=tau(G/e) (수축 사상).
- 반증 확인: tau 는 마이너 단조 아님 (C4 ≻ K3, tau 2<3). 덧셈형 축약 보조정리 거짓 (K4 -> K2).

# R05 N1 (논객 을, 증명 중심) 노트
- n1_zig.py: SAT 로 zig<=t 판정(교대 완전이분 패턴 금지). n1_rho.py: 극대 완전이분쌍 + 런 수 (독립 점검). n1_hom.py/n1_poset.py: Hom(K2,G) / B0 의 Z2-poset map -> Q_k (SAT). n1_arclab.py: 호 라벨 보조정리 (SAT). n1_cegar.py: 라벨-순서 CEGAR. n1_homZ.py: 정수 호몰로지(SNF), n1_pi1.py: 단순연결 점검.
- 결과: zig(C_8^2)=3 (순서 0,1,2,3,6,4,7,5), tau(C_8^2)=3. tau(C_11^3)=5 (omega=4<tau=5<chi>=6): B0 3-연결(정수 호몰로지 0, pi1=1) + 순서 상한 5.
- B0 의 face poset -> Q_3 은 coC7 에서 UNSAT (tau=3 인데) : B0 poset 지수는 부적절, Hom 이 맞다.
