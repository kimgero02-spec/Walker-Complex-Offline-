# [R03-researcher1-interim] $\tau(C_5[K_m])=2m$ : 모멘트 곡선 구성이 성공

- 작성자·라운드·역할: researcher1 / 라운드 3 / 연구원 (지점 1). 중간본. 최종본은 R03-researcher1.md.

## 핵심
1. **극대 완전이분쌍 분류** [증명] ($n\ge5$, $G=C_n[K_m]$, 무방향 쌍): (P) 블롭 $i$ 의 비공집합 $S$ 에 대해 $\{S,\ (K^i\setminus S)\cup K^{i-1}\cup K^{i+1}\}$; (Q) 인접 블롭 $i,i+1$ 에서 $S\subsetneq K^i$, $T\subsetneq K^{i+1}$ 비공집합일 때 $\{S\cup T,\ (K^i\cup K^{i+1})\setminus(S\cup T)\}$. 개수 $n(2^m-1)+n(2^m-2)^2/2$ (n=5: m=2,3,4 에서 25, 125, 565; m=2,3 은 brute force 와 일치).
2. **구성** [증명]: 정점 $(i,s)$ 를 $\gamma(t)=(t,t^2,\dots,t^{2m-1})$ 에 $t=im+s+1$ 로 둔다(블롭이 곡선 위에서 연속 구간). Gale 보조정리(부호변화 $\le d$ 이면 엄격 분리)로 (Q) 는 $2m$ 점이라 항상 분리, (P) 는 부호변화 $\le m+1\le2m-1$ ($m\ge2$) 이라 분리. 따라서 $\tau(C_n[K_m])\le 2m$, $\omega=2m$ 이므로 **$\tau(C_n[K_m])=2m$ ($m\ge2$, $n\ge5$)**.
3. 귀결: $\chi(C_5[K_m])\ge\lceil5m/2\rceil$ 와 합쳐 $\chi-\tau\ge\lceil m/2\rceil$, 간극 비유계. $m=1$ 에서는 (P) 부호변화 2 > $d=1$ 이라 실패(정합: $\tau(C_n)=3$).
4. 점검 코드 `rooms/researcher1/r3_moment.py`: $C_5[K_m]$ $m=2,3,4$, $C_7[K_2],C_7[K_3],C_6[K_2]$ 에서 최대 부호변화 $=2m-1$ 이고 LP 실패 0 (증명의 점검일 뿐, 근거 아님).

R03 반례꾼·망상꾼 보고서는 작성 시점에 아직 없음. 상세 증명은 최종본.
