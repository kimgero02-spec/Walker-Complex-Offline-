# [R11-researcher2-recheck] S^2 덮개 반례 재검토: 반례는 성립하지 않는다 (철회)

- 작성자: researcher2. 대상: `R11-researcher2.md` §4 의 "반례 [증명] (덮개 논법은 coind 에 대해 불충분)". 지적: 망상꾼 `R41-researcher3.md` §정정. R11 파일은 수정하지 않았다.
- 판정: **망상꾼의 지적이 맞다. 반례를 철회한다.**

## 1. 원래 구성과 오류 [증명]
- 원래: $U$ = 경도 $(-10^\circ,100^\circ)$ 의 띠 (모든 위도) $\cup$ 북극 근방, $V$ = 경도 $(80^\circ,190^\circ)$ 의 띠, $A=U\cup(-U)$, $B=V\cup(-V)$.
- 오류: 띠가 모든 위도를 포함하므로 남극 근방의 점 (경도 $(-10^\circ,100^\circ)$) 이 $U$ 에 있다. $-U$ 는 남극 근방 전체를 포함하므로 $U\cap(-U)\ne\emptyset$. 따라서 $A$ 는 "두 서로소 열린 집합의 합" 이 아니고, $\operatorname{coind}A=0$ 이라는 논증 (연결 사상이 한 성분에 들어감) 이 적용되지 않는다.

## 2. 어떤 수정도 불가능하다 [증명, Borsuk–Ulam 만 사용]
**주장.** $S^2=A\cup B$ 이고 $A=U\sqcup(-U)$, $B=V\sqcup(-V)$ ($U,V$ 열린 집합, $U\cap(-U)=V\cap(-V)=\emptyset$) 인 덮개는 존재하지 않는다.
**증명.** 그런 덮개가 있다고 하자. $f_A:A\to S^0$ 를 $U\mapsto+1$, $-U\mapsto-1$ 로 두면 연속 (서로소 열린 집합) 이고 동변이다. $f_B$ 도 같다. 불변 단위분해 $\varphi_A(x)=d(x,S^2\setminus A)$, $\varphi_B(x)=d(x,S^2\setminus B)$ (대척 사상은 등거리이고 $A,B$ 가 불변이므로 $\varphi(-x)=\varphi(x)$) 를 합이 1 이 되도록 정규화한다. 그러면
$$x\mapsto\big(\varphi_A(x)f_A(x),\ \varphi_B(x)f_B(x)\big)\in\mathbb R^2\setminus\{0\}$$
는 동변 연속 사상 $S^2\to S^1$ (정규화 후) 을 준다 (둘 다 0 인 점은 없다: $\varphi_A+\varphi_B=1$ 이고 $f=\pm1$). Borsuk–Ulam 에 의해 동변 사상 $S^2\to S^1$ 은 없다. 모순. ∎
- 이 논증은 Schwarz/Krasnosel'skii 종수 $\gamma(S^2)=3$ 과 같은 내용이다 ($S^2$ 는 $W\sqcup(-W)$ 꼴 열린 집합 2 개로 덮이지 않는다).

## 3. 철회 범위와 영향
- **철회:** R11 §4 의 "덮개 논법은 coind 판에서 거짓 ($S^2$ 반례)" 은 철회한다. 올바른 상태: coind 판 덮개 부등식 $\operatorname{coind}(A\cup B)\le\operatorname{coind}A+\operatorname{coind}B+1$ 은 **증명되지도 반증되지도 않았다** [추측 상태로 되돌림].
- **영향 받는 서술 (수정 권고, 원본 파일은 건드리지 않음):**
  - `R12-researcher3.md` (§3 정정 사항 — 이 반례를 받아들여 자기 덮개 보조정리를 정정함).
  - `ADVICE-3-to-1.md` §1 표 ("open-cover 논법이 R11 반례로 coind 판에서 깨졌으므로").
  - `master/final_report.md` §3 ("덮개 논법은 coind 판에서 거짓 (R11-r2 의 $S^2$ 반례)").
  - 내 `READ-researcher2.md`, `R12-researcher2.md` 의 같은 인용.
- **영향 받지 않는 결론:** J (τ 조인 상계) 가 열린 문제라는 판정은 그대로다. 그 판정의 근거는 "R08-r3·R09-r3 의 덮개 논법이 ind 판만 준다" (R09 부록) 이며, $S^2$ 반례가 아니다. R09 부록의 "레트랙션은 coind 쪽 단조성을 주지 않는다" 판정도 유지된다.
- 덧붙임: 위 §2 의 논법 (단위분해 + 조인 사상) 은 **ind 판** 덮개 부등식 $\operatorname{ind}(A\cup B)\le\operatorname{ind}A+\operatorname{ind}B+1$ 의 표준 증명과 같다. coind 판은 이 논법으로 다뤄지지 않으므로, coind 판의 참·거짓은 여전히 열려 있다.

## 4. 교훈 (자기 점검)
- R11 에서 반례를 [증명] 으로 표기했지만, 집합의 서로소성 (가장 중요한 조건) 을 극 근방에서 확인하지 않았다. 반례 표기는 핵심 조건을 모든 영역에서 확인한 뒤에만 쓴다.
