# STATUS — hadwiger-coindex (인계 메모)

갱신: 라운드 1 완료 (세 보고서 모두 제출, 오케스트레이터 재검증은 C5[K2] 한 건만 수행)
포메이션: T (연구원 · 반례꾼 · 망상꾼)

## 확정된 것
- 정의 정정: $\tau(G)=\operatorname{coind}(B_0(G))+1$ ($+2$ 는 오류. $K_1$ 반례, $B_0(K_n)\cong S^{n-1}$ 오케스트레이터 확인).
- 변형들의 올바른 오프셋 [기억-미검증, researcher1]: $\operatorname{coind}(B)+2$, $\operatorname{ind}(B_0)+1$, $\operatorname{ind}(B)+2$, $\operatorname{conn}(B_0)+2$, $\operatorname{conn}(B)+3$.
- $\tau(C_5[K_2])=4<\chi=5$: 세 방법(Radon 인증서, 오케스트레이터 재검증, SW 높이)이 일치.
- 정점 ≤7 그래프 1252개: $\tau=\chi$ 가 1247개, $\tau=3<\chi=4$ 가 5개. S1·홀수 마이너·S4·S5 위반 0건 (researcher1·2, 일부만 오케스트레이터 재검증).
- 망상꾼: $\tau(C_5[K_3])=6<\chi=8$, $\tau(C_7[K_2])=4<\chi=5$ (Radon 인증서, 오케스트레이터 미재검증). $\tau(G/e)\ge\tau(G-e)$ [증명]. $\tau\le d_R(G)+1$ 인증서 도구(그래프 Radon 정리, 증명 스케치).
- Hadwiger ⇒ S1 은 $\tau\le\chi$ 로 자명. S1 의 반례는 Hadwiger 의 반례.

## 열린 문제
- S1~S5 전체 (증명도 반례도 없음). 정점 ≥8 전수 미실시.
- $\tau(C_5[K_m])=2m$ 추측 ($m=2,3$ 만 확인). Dol'nikov–Kříž 하한과 $\tau$ 의 대소.
- 망상꾼 #7: 마이너-자유 그래프가 $\mathbb R^{t-2}$ 에서 Radon-free 배치를 갖는가 (미시험).
- 논문(Steiner, arXiv:2312.17130) 원문은 네트워크 제한으로 못 읽음. 논문의 coindex 진술 여부 미확인.

## 주의
- Catlin 계열은 $\tau=\omega$ 라 S4 시험대로 부적합. S4 반례 후보는 $\tau>\omega$ 이면서 Hajós 가 실패하는 그래프.
- 호몰로지 하한 $\tau_h$ 는 부분그래프에 단조가 아님 → 단조화(부분그래프 최댓값) 필수.

## 다음 임무 (제안)
1. 반례꾼에게 연구원 표와 망상꾼 아이디어를 중계해 본격 공격 (R2).
2. 정점 8개 이상 탐색, $C_5[K_m]$ 일반화, 망상꾼 #7 시험.
3. 오케스트레이터가 연구원 표의 핵심 값 몇 개를 독립 재검증.

## 파일
- `problem.md`(문제·정정 이력), `library/`(보고서), `rooms/`(연구원 코드·노트).
