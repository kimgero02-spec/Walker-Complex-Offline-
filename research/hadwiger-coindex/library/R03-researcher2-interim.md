# [R03-researcher2-interim] 추측 C 는 거짓 ($C_5$, $\overline{C_7}$), 정리 A 는 증명 완결

- 작성자·라운드·역할: researcher2 / 라운드 3 / 반례꾼. 중간본. 최종본 R03-researcher2.md. 도서관에서 R03-researcher1 (최종 포함)을 읽었고 R03-researcher3* 는 아직 없음.

## 핵심 (상세 증명은 최종본)
1. **(b) 추측 C 반증 [증명]**: $G=C_5$ ($\tau=3$)의 임의의 Kneser 표현 $\mathcal H$ 에서 $\operatorname{cd}(\mathcal H)\le2$. 방법: $a\in S_0\cap S_2$, $b\in S_1\cap S_3$ 를 뽑아 $U=\{a,b\}$ 로 하면 $U$ 를 피하는 집합은 $S_4$ 하나뿐이고 $|S_4|\ge2$. 같은 방식으로 $G=\overline{C_7}$ ($\tau=3$)에서도 $\operatorname{cd}\le2$ [증명]. 따라서 $\max_{\mathcal H}\operatorname{cd}<\tau$: **추측 C 거짓**, 경로 "추측 C ⇒ 정리 3 ⇒ S1" 폐쇄.
2. **(a) 정리 A 증명 완결 [증명]**: R02 스케치에 결함 없음. (F1)–(F3) 를 모멘트 곡선(Vandermonde) 으로 대체한 명시적 등변 사상 $S^{c-1}\to B_0(G)$ 로 증명이 닫힌다. (O1) 은 공허(논증이 $N$ 에 무관).
3. **(c) $\tau\le\operatorname{zig}$ 직접 증명 [증명]**: 등변 사상 $B_0(G)\to\mathbb R^{d}\setminus0$, $x_j\mapsto$ 모멘트 $\sum_j x_j j^k$ ($k<d$), Borsuk–Ulam 만 사용. 문헌 의존 제거.
4. 코드: rooms/researcher2/r3_checks.py, pi1_c5.py (B_0(C_5) 단일연결 [계산 확인]), zig_check.py.
