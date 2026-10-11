# [SRC] Norin, Steiner, *A Proof of the Linear Hadwiger Conjecture* (arXiv:2610.05291v1, 4 Oct 2026)

- 원문: `inbox/8e13b0f3-2610.05291.pdf` (문주님 업로드, 41쪽)
- 오케스트레이터 작성 요약. **읽은 범위: 1–4쪽 (서론, 정리 2–5 의 진술과 증명 골격, 기법 목록, AI 사용 고지).** 5–41쪽 (정리 4·5 증명, 부록의 정리 9·15) 은 아직 읽지 않음.
- arxiv.org 직접 접속은 정책으로 차단되어 업로드본만 사용.

## 주장
- **정리 2:** 절대상수 $C$ 가 있어 모든 그래프 $\chi(G)\le C\cdot h(G)$ (Linear Hadwiger). 즉 Hadwiger 의 **선형 약화** 를 증명했다고 주장.
- 증명 골격 (1–2쪽):
  - 정리 3 (Delcourt–Postle 계열 귀결): $h(G)<t$ 이고 $\mathsf v(G)\le t\log^5 t$ 이면 $\chi\le Ct$. 이로부터 "작은 차수에서의 선형 Hadwiger" 로 문제 축소.
  - 정리 4: $h(G)<t$, $\mathsf v(G)\le t(\log t)^{1/2-\varepsilon}$ 이면 $\chi\le(4+\varepsilon)t$.
  - 정리 5 (부트스트랩): $\mathrm{LH}(\alpha)\Rightarrow\mathrm{LH}(\tfrac43\alpha)$.
  - $\tfrac13(\tfrac43)^{10}\approx 5.92\ge 5$ 로 $\mathrm{LH}(5)$ 를 얻음.

## 우리 과제와의 관계 (오케스트레이터 판단)
1. **우리 문제는 τ 에 관한 것이고, 이 논문은 χ 와 Hadwiger 수 h 에 관한 것이다.** 이 논문은 τ 의 S1 에 직접 답하지 않는다. S1 (Hadwiger 의 τ 판)이 참이라도 이 논문에서 나오는 것은 χ 의 선형 상한뿐이다.
2. **S1 과의 간접 연결:** 정리 2 는 $\chi\le Ch$ 이므로 τ 에도 $\tau\le\chi\le Ch$ 를 준다. 즉 τ 의 "$K_t$ 마이너 없음 ⇒ τ 작음" 방향은 얻지 않는다 (τ 는 χ 의 하한이므로 χ 상한은 τ 상한을 주지 않음). **결론: 이 논문은 S1 에 대해 새 정보를 주지 않는다.** [계산 확인 불필요: 부등식 방향에 근거]
3. **기법 중 우리 과제에 쓸 만한 것:** (a) Reed–Seymour 분수 선형 Hadwiger, (b) Delcourt–Postle 의 chromatic separability (색칠 문제를 "chromatically inseparable" 유도 부분그래프 연구로 환원), (c) 짝 독립 집합 커버를 쓰는 분수 색수 LP 변형, (d) 수축에서 두 배 리프팅. 특히 (b)의 "inseparable 부분그래프" 개념은 STATUS 의 S4 탐색(τ>ω 이면서 Hajós 실패)과 비슷한 "최소 반례 축소" 아이디어로 읽을 수 있음. [추측: 대응 관계는 아직 검증 안 됨]
4. **신뢰성 주의:** 본 논문은 **AI 가 증명을 생성**했다고 고지한다 (ChatGPT "Astra 6", 검토는 GPT-6 Pro). 논문은 Lean 형식화가 있다고 하지만 (`github.com/snorin239/LinearHadwiger`) 우리는 접속하지 못했다. 따라서 **정리 2 의 증명은 아직 독립 검증되지 않았다.** 확정 주장으로 쓰지 말 것.
5. 이 논문은 χ 기준이므로, 우리 STATUS 의 "정점 ≥8 전수" 나 "S1~S5 증명·반례" 어느 쪽에도 직접 쓸 근거는 아니다.

## 아직 확인 안 된 것
- 정리 4·5 의 증명 세부와 정리 9 (near-spanning matching) 의 정량 버전 (부록).
- Lean 형식화의 실제 범위 (접속 불가).

## 문주님께 요청 해결 여부
- 이 논문은 문주님이 업로드하셨으므로 REQUESTS 에 새로 올릴 것은 없음. Lean 저장소는 접속이 막혀 있으므로, 필요하면 해당 저장소를 열어 달라고 요청할 수 있음 (`github.com` 허용 여부 확인 필요).
