# researcher1 노트 (R04)
- 코드: r4_blowup.py (types/types2: 극대 타입 열거, expand: 타입→쌍, brute: 폐포, check_moment: 유리수 정확 검증, Dsigma: 타입 상계).
- r4_run1: Petersen. r4_run2: Cbar7, W5. r4_run3: types vs types2. r4_run4: C_n^2, ladder, K33. r4_run5: Grotzsch, Clebsch. r4_run6: 무작위 탐색(근거 아님). r4_run7: C_9^2, Grotzsch brute. r4_run8: Clebsch.
- 핵심: tau(G[K_m]) = m*omega 붕괴 (psi <= m(omega-z)). Petersen m>=2 에서 2m.

# R05 N1 (논객 갑)
- n1_lib.py(극대쌍, rho, 평면 Radon 탐색), n1_lib2.py(chainlen, zig DFS), n1_run4.py(poset, 베티), n1_bock.py(Bockstein 판정), n1_run1~9.
- 결과: C_8^2 zig=3 (순서 0,1,2,3,6,4,7,5; 모든 완전이분쌍 직접 열거로 런<=3). ell+1>=zig 무반례. tau<=3 <=> Bockstein(w)=0.

# R48 (임계 구조 쪽, 갭 {7})
- r48_ico.py: 정이십면체 쌍 + 순환 3-정규 교차 (shift 4종): n=24, m=96, 모든 deg 8, h=3, 지배쌍 0, χ∈{4,5}. 정이십면체 비인접쌍 공통이웃 ∈{0,2}. K_8−PM χ=4.
- 핵심: 동일시 환원 R-id (deg_G(v)=6+j, N_B(v) 의 독립집합 j+2 개, 교차 합집합 ≤3) 증명. 정규화(변 극대) 시 한 시트는 h<3 정점 ≤2. 같은 시트 R-id 면역 유형 (3,3),(4,3),(5,2),(5,3). 정이십면체 쌍 = 증명된 환원 전부를 피하는 Euler 등호 증인 → 방전 불가.
