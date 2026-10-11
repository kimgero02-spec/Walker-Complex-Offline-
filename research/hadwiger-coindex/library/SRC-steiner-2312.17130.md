# [SRC] Steiner, *Hadwiger's conjecture and topological bounds* (arXiv:2312.17130v2)

- 원문: `inbox/f955a10c-2312.17130.pdf` (문주님 업로드, 12쪽)
- 오케스트레이터 작성 요약. **읽은 범위: 1–7쪽 (정리 2·3·4, 보조정리 5, 정의 1–5, 그림 1 까지).** 8–12쪽(정리 2 증명 후반, 정리 3·4 증명, 참고문헌)은 아직 읽지 않았음.
- arxiv.org 직접 접속은 조직 정책으로 차단되어 업로드본만 사용.

## 정의 (논문 Definition 1 — 우리 `τ` 와 대조용)
- 상자 복합체 $B(G)$, $B_0(G)$: 정점 $V(G)\times\{1,2\}$. $X$ 가 $B_0(G)$ 의 면 ⇔ 두 투영 $X_1, X_2$ 가 완전 이분쌍을 이루고 $X_1, X_2$ 각각이 공통 이웃을 가짐. (`B` 는 이웃 조건 없이 완전 이분쌍만 요구.)
- 우리 문제의 $\tau(G)=\operatorname{coind}(B_0(G))+1$ 은 논문 그림 1의 **"coind(B₀(G))+1"** 칸에 해당. 이 칸은 χ 의 하한이다. [계산 확인: 그림 1 판독]

## 그림 1 (위상 하한 계층, 논문 Figure 1)
$\chi \ge \operatorname{zig} \ge \operatorname{Xind}(\operatorname{Hom}(K_2,G))+2 \ge \operatorname{ind}(B)+2 \ge \operatorname{ind}(B_0)+1$, 그리고 $\operatorname{ch-ind}_{\mathbb Z_2}(B)+2 = \operatorname{ch-ind}_{\mathbb Z_2}(B_0)+1$.
옆 가지: $\operatorname{cd}(\mathcal H) \le \operatorname{coind}(B_0)+1$, $\operatorname{coind}(B)+2$, $\operatorname{conn}(B_0)+2$, $\operatorname{conn}(B)+3$, $\operatorname{conn}_{\mathbb Z_2}(B)+3=\operatorname{conn}_{\mathbb Z_2}(B_0)+2$.
- 이 그림의 오프셋은 `STATUS.md` 의 "변형들의 오프셋 [기억-미검증]" 목록과 **일치**한다 ($\operatorname{coind}(B)+2$, $\operatorname{ind}(B_0)+1$, $\operatorname{ind}(B)+2$, $\operatorname{conn}(B_0)+2$, $\operatorname{conn}(B)+3$). 즉 기억-미검증 표시를 [문헌 확인]으로 올릴 수 있음. [문헌 확인: 논문 그림 1, 출처는 Matoušek–Ziegler 및 Daneshpajou–Meunier]

## 주요 결과
- **정리 1 (Dol'nikov, Kříž):** Kneser 표현 $\mathcal H$ 가 있으면 $\chi(G)\ge \operatorname{cd}(\mathcal H)$.
- **정리 2:** $\operatorname{zig}(G)\ge t$ ⇒ $G$ 가 홀수 마이너로 $K_{\lfloor t/2\rfloor+1}$ 을 포함. 그림 1 에서 zig 가 위상 하한들의 가장 강한 것이므로, 그 하한들 중 하나라도 $\ge t$ 이면 같은 결론.
- **정리 3:** Kneser 표현에서 $\operatorname{cd}(\mathcal H)\ge t$ ⇒ $G$ 가 $K_t$ 마이너 포함. → Hadwiger 가 Dol'nikov–Kříž 하한이 tight 인 그래프(Kneser 등)에서 성립.
- **정리 4:** Schrijver 그래프 $S(n,k)$ 는 $K_{n-2k+2}$ 를 홀수 마이너로 포함. (Odd Hadwiger 의 Kneser/Schrijver 경우.)

## 우리 과제와의 연결 (오케스트레이터 판단)
1. **S3 (DK 하한과 τ 의 대소):** 정리 3 은 $\operatorname{cd}(\mathcal H)\ge t \Rightarrow K_t$ 마이너. $\tau$ 와 $\operatorname{cd}$ 의 관계(그림 1 에서 cd 는 coind(B₀)+1 아래에 있음)는 **$\operatorname{cd}\le\tau$** 임을 뜻한다. 따라서 Steiner 정리 3 은 τ 가 아니라 cd 에 대한 결과이고, τ 에 직접 옮겨지지 않는다. [계산 확인 불필요: 그림 1 의 화살표 방향으로부터. 단, 화살표 방향 해석은 한 번 더 검증 필요]
2. **S3 는 τ 에 적용된다 (정정, 오케스트레이터 R02):** 그림 1 의 사슬은 $\chi\ge\operatorname{zig}\ge\operatorname{Xind}(\operatorname{Hom}(K_2,G))+2\ge\operatorname{ind}(B)+2\ge\operatorname{ind}(B_0)+1\ge\operatorname{ch\text{-}ind}_{\mathbb Z_2}(B_0)+1\ge\operatorname{coind}(B_0)+1=\tau(G)$ 이므로 $\tau\le\operatorname{zig}$. 따라서 $\tau(G)\ge t\Rightarrow\operatorname{zig}(G)\ge t\Rightarrow$ (정리 2) 홀수 $K_{\lfloor t/2\rfloor+1}$ 마이너. 즉 **S3 는 τ 에 대해 성립한다.** [문헌 확인: 그림 1(3쪽 이미지를 오케스트레이터가 직접 판독) + 정리 2; 사슬의 각 부등식은 Matoušek–Ziegler / Daneshpajou–Meunier 인용 의존]. 이 항목의 이전 판("바로 나오지 않는다")은 오케스트레이터의 방향 착오였으며 철회한다. 단, 정리 2 의 증명 자체(7쪽 이후)는 직접 읽지 않았다.
3. **8번 "Kneser/Schrijver 에서 odd Hadwiger 성립"** 은 우리 문제의 "$\tau$ 가 tight 인 족"(STATUS 후속 4번) 후보에 대응. 단, 이는 cd 기준이고 τ 기준이 아님.
4. 이 논문은 $\operatorname{coind}(B_0)$ 에 대해 **직접 결과를 주지 않는다.** 1–7쪽 기준 coind 를 다룬 정리는 없음. 남은 8–12쪽 확인 필요.

## 아직 확인 안 된 것
- 8–12쪽: 정리 2·3·4 의 증명 세부, Odd Hadwiger 의 Schrijver 증명, 참고문헌의 [25] (Delcourt–Postle 계열) 내용.
- "STATUS 의 열린 문제: 논문의 coindex 진술 여부" → **1–7쪽에는 coindex 진술 없음 (부분 답: 없음으로 보임, 8–12쪽 확인 전까지 확정 아님).**

## 문주님께 요청 해결 여부
- REQUESTS #1 (Steiner 원문): 업로드로 **부분 해결** (1–7쪽 읽음). 8–12쪽 읽기 필요.
