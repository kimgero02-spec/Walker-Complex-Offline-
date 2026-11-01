# [R02-researcher1-interim] 중간 결과 (반례꾼 공격용, 최종 보고서 아님)

- 작성자: researcher1 / 라운드 2 / 역할: 연구원. 공격 환영, 특히 A-3 (사상 Ψ 의 연속성)과 A-4 (연결성 인용).

## A. 그림 1 화살표 해석과 cd ≤ τ
- [계산 확인, 이미지 판독] Steiner Figure 1 (p.3): `cd(H) ≤ coind(B0(G))+1` 은 "≤" 로 직접 적혀 있다. 체인 `χ ≥ zig ≥ Xind(Hom(K2,G))+2 ≥ ind(B)+2 ≥ ind(B0)+1 ≥ ch-ind(B0)+1 ≥ coind(B0)+1` 도 같은 방향 (작은 쪽이 화살표 끝).
- [증명 스케치] 임의의 Kneser 표현 $\mathcal H=(V,E)$ (KG(H)=G, 모든 e 비공집합) 에 대해 $\operatorname{cd}(\mathcal H)\le\operatorname{coind}(B_0(G))+1=\tau(G)$.
  1. $\Sigma$ = 부호 집합 $S\subseteq V^{\pm}$ (±v 동시 포함 금지) 의 복합체 = $\partial$(교차다면체) $\cong S^{N-1}$, $N=|V|$, 대척 $S\mapsto -S$.
  2. $\Psi(S)=(A,B)$, $A=\{e\in E: e\subseteq S^+\}$, $B=\{e\in E: e\subseteq S^-\}$. $e\in A, f\in B$ 이면 $e\cap f=\emptyset$ 이므로 $A\times\{1\}\cup B\times\{2\}$ 는 $B_0(G)$ 의 면. $\Psi$ 는 포함 순서 보존, $\Psi(-S)=\text{swap}\,\Psi(S)$.
  3. $\Lambda=\{S:\ S^+,S^-$ 가 각각 간선을 포함하지 않음$\}$ (부분복합체). $\Psi(S)=\varnothing \iff S\in\Lambda$. 그러므로 $\Psi$ 는 $\Sigma\setminus\Lambda$ 위에서 정의된 등변 포셋 사상 $\Delta(\Sigma\setminus\Lambda)\to\Delta(\text{faces of }B_0)$ 를 준다.
  4. $S\in\Lambda$ 의 비부호 집합 $U(S)=V\setminus(S^+\cup S^-)$ 에서 $(S^+,S^-)$ 는 $E_{U}$ 의 진적 2-색칠이므로 $U(S)$ 는 "좋은" 집합. $\operatorname{cd}=c$ 이면 $|U(S)|\ge c$, 즉 $|S|\le N-c$. 따라서 $\Lambda\subseteq$ ($N-c-1$)-골격.
  5. $X=S^{N-1}\setminus|\text{skel}_{N-c-1}|\subseteq Y=S^{N-1}\setminus|\Lambda|\simeq_{\mathbb Z_2}\Delta(\Sigma\setminus\Lambda)$. Alexander 쌍대로 $X$ 는 $(c-2)$-연결, 따라서 $S^{c-1}\to X$ 가 존재 ⇒ $\operatorname{coind}(B_0)\ge c-1$.
- [증명 스케치 상태] 외부 사실 3개 인용: (F1) $|K|\setminus|L|\simeq\Delta(F(K)\setminus F(L))$ 등변; (F2) $d$-구면의 $j$-골격 여집합은 $(d-j-2)$-연결; (F3) $k$-연결 자유 $\mathbb Z_2$-공간에는 등변 $S^{k+1}\to X$ 존재.
- 함정(확인함): 단순히 $\Sigma$ 전체에 $\Psi$ 를 적용하면 $\Psi(\{+v\})=\varnothing$ 이 되어 Borsuk–Ulam 모순 ($G=K_3$, 쓸모없는 원소 1개 추가하면 $S^3\to S^2$). $\Lambda$ 제거가 필수.

## B. 수치 확인 (소규모, 증명 검증용)
- [계산 확인] 정규 Kneser 표현 $K(n,k)$ (ground $[n]$): $\operatorname{cd}$ 가 $K(5,2)=3$, $K(6,2)=4$ 로 $\tau=\chi$ 와 일치 (Dol'nikov 타이트).
- [계산 확인] Schrijver 표현 (안정 $k$-집합, ground $[n]$): $\operatorname{cd}(S(6,2))=2$, $S(7,2)=3$, $S(8,3)=0$, 모두 $\le\tau$ (4, 5, 4). 표준 표현은 타이트하지 않음.
- [계산 확인] 정점 $\ge 5$ 인 비-Kneser 예: 극대 독립집합 표현의 cd 는 $C_5$:1, $\overline{C_7}$:1, $C_5[K_2]$:0. 선(line) 표현 $\overline{C_5}$, $\overline{C_7}$: cd 1. Petersen 의 외곽 5-사이클을 $K(5,2)$ 에서 떼어 낸 표현: cd 1. → 이 표현들에서는 cd 가 $\tau$ (3,3,4) 에 못 미침. 즉 $\max_{\mathcal H}\operatorname{cd}(\mathcal H)=\tau$ 는 표준 표현에서 성립하지 않음.
- 코드: `rooms/researcher1/cd_check.py`, `cd_kneser.py`, `cd_ind.py`, `cd_line.py`.

## C. 귀결 (잠정)
1. Steiner 정리 3 ($\operatorname{cd}\ge t\Rightarrow K_t$ 마이너) 은 τ 로 옮겨지지 않는다: $\operatorname{cd}\le\tau$ 이므로 $\tau\ge t$ 로부터 $\operatorname{cd}\ge t$ 를 얻지 못함 (방향이 반대).
2. 역으로 S1($\tau$ 판)은 정리 3 의 모든 적용을 포함하는 더 강한 주장이다.
3. [그림 1 체인 의존] $\tau\le\operatorname{zig}$ ⇒ 정리 2 로부터 S3 ($\tau\ge t\Rightarrow$ 홀수 $K_{\lfloor t/2\rfloor+1}$ 마이너) 가 성립. R01 에서 "열림"이던 S3 가 이 체인으로 닫힌다. 단 체인의 각 부등식은 문헌 인용이므로 [문헌 확인] 표시.
4. $\tau\le\chi$ 이므로 S4 색칠 버전 $S4(\chi)\Rightarrow S4(\tau)$ (각 $t$). Dirac($t=4$) [기억-미검증] 로 $t\le4$ 는 참. 반례 후보는 $t\ge5$.

## D. 열린 문제
- 추측 C: 모든 $G$ 에 대해 $\max_{\mathcal H}\operatorname{cd}(\mathcal H)=\tau(G)$? 현재 증거는 Kneser 류에서만. 반증 가능 (다른 표현으로 $\overline{C_7}$ 에서 cd 3 을 찾으면 지지, 증명 불가 시 기각 쪽).
- 정리 2 의 odd 버전이 $\tau$ 를 $t$ 까지 올리는지 (S2) — 미해결.
