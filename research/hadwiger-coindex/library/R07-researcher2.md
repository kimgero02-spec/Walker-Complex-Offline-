# [R07-researcher2] 시트 분해 법칙 공격: 합 법칙·곱 법칙 반증, $\chi$ 상계 방어

- 작성자·라운드·역할: researcher2 / 라운드 7 / 반례꾼. 중간본: `R07-researcher2-interim.md`. 코드: `rooms/researcher2/r06/r07_check.py`, `r07_prod.py`, `r07_verify.py`.
- 정의 해석: A = 간선 분할 $E=\bigsqcup E_i$, 각 $(V,E_i)$ 평면. B = 꼭짓점 분할 $V=\bigsqcup V_i$, 각 $G[V_i]$ 평면. C (책 두께형), D (분기 피복형) 는 이번 라운드에 시험하지 않았다 (정의 본문이 도서관에 없어 해석을 확정하지 못함).

## 요약
1. **합 법칙 $\operatorname{zig}(G_1\cup G_2)\le\operatorname{zig}(G_1)+\operatorname{zig}(G_2)-1$ 은 거짓** [계산 확인]: $K_6=\text{oct}\cup PM_3$, 두 조각 모두 평면. $\operatorname{zig}$ 값 3, 2, 6.
2. **곱 법칙 $\operatorname{zig}(G_1\cup G_2)\le\operatorname{zig}(G_1)\operatorname{zig}(G_2)$ 는 일반 그래프에서 거짓** [계산 확인 + 증명 보조]: $K_{10}=C_{10}(1,2)\cup C_{10}(3,4,5)$ 에서 $3\cdot3=9<10$. 단 두 번째 조각이 비평면이므로 **평면 시트 버전은 이 반례로 깨지지 않는다** (미결).
3. **(i) $\chi\le4k$ (B), (ii) $\chi\le4^k$ (A), (iv) $\tau\le4^k$ 는 방어** [증명]. 반례 없음.
4. **망상꾼 K_5 예 확인**: 시트 결함이 최고 호몰로지를 만든다는 관찰은 $K_5$ 에서 맞다 [계산 확인]. K_6 는 미검증.

## 공격 대장

| 대상 | 방법 | 결과 | 방어 이유 | 표기 |
|---|---|---|---|---|
| (iii-a) 합 법칙 S1 | $K_6=\text{oct}\cup PM_3$, $\operatorname{zig}$ 완전 탐색 | **반례** (6 > 3+2−1 = 4) | $\operatorname{zig}(K_n)=n$ 는 직접 증명됨: 임의 순서에서 짝수/홀수 위치를 A,B 로 나누면 $K_n$ 의 완전이분쌍이고 런 수 $n$ | [계산 확인] + [증명] (zig(K_n)=n) |
| (iii-b) 곱 법칙 S2 (일반) | $K_{10}=C_{10}(1,2)\cup C_{10}(3,4,5)$; 독립 열거 검증 (모든 완전쌍 $2^{10}\cdot2^{10}$ 중 극대 포함) | **반례** (9 < 10). $K_{11}$ 도 같은 형태 (9 < 11) | $\operatorname{zig}(C_{10}(1,2))\le3$: DFS 가 찾은 순서의 런 수 3 을 독립 열거로 확인 (순서 자체는 `r07_verify.py` 출력 참조); $\operatorname{zig}(C_{10}(3,4,5))=3$: 순서의 런 수 3 확인 + $\omega=3$ 하계. $\operatorname{zig}(K_{10})=10$ | [계산 확인] + [증명] |
| 곱 법칙 S2 (평면 시트) | $K_8$ (thickness 2), $K_9=K_{3,3,3}\cup3K_3$ | 미반증. $K_9$: $\operatorname{zig}(K_{3,3,3})=3$, $\operatorname{zig}(3K_3)=3$, 곱 9 = $\operatorname{zig}(K_9)$ 로 **등호** | $K_{3,3,3}$ 과 $3K_3$ 모두 평면이 아니므로 평면 시트 반례가 아님 | [계산 확인] |
| S4 (망상꾼 K_5 예) | $X(K_5)$ 와 시트 $K_5-e$ (평면), $e$ 의 합집합 | **확인**: $\tilde H_4(X)=\mathbb F_2$; $K_5-e$ 는 $\tilde H_3$ 만; 합집합은 $\tilde H_1=\mathbb F_2^2$, $\tilde H_3=\mathbb F_2$ — 최고 류가 결함 | 합집합이 $X$ 의 최고 사슬을 덮지 못함 (면 $(A,B)$ 가 여러 시트에 걸침) | [계산 확인] |
| S4 (K_6 예) | 미시험 | 미정 | — | 미결 |
| (i) $\chi\le4k$ (B) | 서로소 팔레트 색칠 | 방어. 각 $G[V_i]$ 는 평면이므로 $\chi\le4$ (4색정리 [기억-미검증]) | 팔레트 합 | [증명] |
| (ii) $\chi\le4^k$ (A) | 곱 색칠: $c=(c_1,\dots,c_k)$, 간선 $uv\in E_i$ 이면 $c_i(u)\neq c_i(v)$ | 방어 | 모든 간선이 어떤 좌표에서 달라짐 | [증명] (4색정리 인용) |
| (iv) $\tau\le4^k$ | $\tau\le\chi$ (팀 증명) + (ii) | 방어 | — | [증명] |
| 가법/곱 법칙의 평면 버전 (S1 평면) | $K_6$ (oct, PM3 평면) | **반례 (평면 시트)** | 위 S1 과 같음 | [계산 확인] |

## 본문 메모
- 합 법칙 반례의 두 조각 평면성: oct 는 평면 다면체 그래프, $PM_3$ 는 평면. 따라서 2-시트 평면 분해에 대한 가법 법칙은 거짓이다.
- 곱 법칙: $\operatorname{zig}\le\chi$ 와 $\chi\le\prod\chi_i$ 로는 $\operatorname{zig}$ 의 곱 상계를 얻지 못한다 (zig 는 χ 보다 작을 수 있으므로). 따라서 곱 법칙은 독립 명제이고 일반 그래프에서 거짓.
- 하계 쪽 일반 사실: $\operatorname{zig}(G)\ge\omega(G)$ 와 $\operatorname{zig}(G)\ge\tau(G)$ (팀 증명) 는 반례 검증의 하계로 사용.

## 문주님께 요청
없음.

## 후속연구 지점
1. **평면 시트 곱 법칙 (S2 평면 버전) 의 반례 탐색.** 이유: 일반 반례 $K_{10}$ 은 비평면 시트를 쓴다. 평면 두 조각 $G_1\cup G_2 = G$ 에서 $\operatorname{zig}(G)>\operatorname{zig}(G_1)\operatorname{zig}(G_2)$ 를 찾는 것이 문주님 질문의 핵심. 시작: $K_8$ 의 2-평면 분해 (두께 2) 를 모두 나열해 zig 값 확인 (가지치기로 $n\le8$ 가능), 또는 두 조각의 zig 가 2·3 인 경우 (이분 평면 + zig 3 평면) 를 찾기. 난점: $K_8$ 의 평면 분해 열거량.
2. **$K_6$ 의 $X$ 최고 호몰로지 공식 (S4).** 이유: S4 는 $K_5$ 에서만 확인. 시작: $\tilde H_5(X(K_6))$ 과 $\bigcup X(G_i)$ 의 호몰로지 (`homol.py` 의 `betti_gf2` 재사용). 난점: 없음 (계산 가능).
3. **정의 C, D 의 해석 확정.** 이유: 책 두께형, 분기 피복형은 본 시험에서 빠졌다. 시작: 문주님께 정의 본문 확인 요청 (REQUESTS 에 기록 권장). 난점: 해석 불일치 위험.
4. **zig 의 곱 법칙을 조건부로 바꾸기.** 이유: 일반 반례 이후 가능한 형태는 "두 조각의 $\operatorname{zig}$ 가 $\omega$ 와 같을 때" 같은 제한 명제. 시작: $K_{10}$ 반례의 조각은 $\omega=\operatorname{zig}=3$ 이라 "$\operatorname{zig}_i=\omega_i$" 조건이 반례를 막는지 확인. 난점: 조건이 너무 강해져 무의미해질 수 있음.
