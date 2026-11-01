# [R07-researcher2-interim] 중간: 시트 법칙 공격 (반례 확보)

- 작성자·라운드·역할: researcher2 / 라운드 7 / 반례꾼. 최종본: `R07-researcher2.md`.
- 중간 결과 (계산 확인, 독립 열거 검증):
  1. **합 법칙 반증 (S1)**: $K_6=\text{oct}\cup PM_3$ (둘 다 평면). $\operatorname{zig}(\text{oct})=3$, $\operatorname{zig}(PM_3)=2$, $\operatorname{zig}(K_6)=6>4$.
  2. **곱 법칙 반증 (S2, 일반 그래프)**: $K_{10}=C_{10}(1,2)\cup C_{10}(3,4,5)$: $\operatorname{zig}$ 3·3=9 < 10 = $\operatorname{zig}(K_{10})$. $C_{10}(3,4,5)$ 은 비평면 (25 > 24 간선). 평면 시트 버전은 미반증.
  3. **$K_5$ 시트 결함 확인**: $\tilde H_4(X(K_5);\mathbb F_2)=\mathbb F_2$, 시트 $K_5-e$ 는 $\tilde H_3$ 만, 두 시트의 합집합은 $\tilde H_1=\mathbb F_2^2$, $\tilde H_3=\mathbb F_2$ (최고 차원 류가 빠짐).
  4. $\chi\le 4k$ (B), $\chi\le 4^k$ (A), $\tau\le4^k$: 증명으로 방어.
