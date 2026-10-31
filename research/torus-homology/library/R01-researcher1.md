# [R01-researcher1] 토러스 및 비교 공간의 호몰로지: CW / Δ / 단체 모델 직접 계산

- 작성자: researcher1 (예제 계산 담당) / 라운드: 1 / 임무: $T^2$ 의 $H_n(\,\cdot\,;\mathbb{Z})$ 를 여러 모델로 직접 계산하고, $S^1, T^3$, 클라인 병 $K$ 와 비교
- 코드: `rooms/researcher1/homology.py` (자체 구현 정수 스미스 표준형), 결과 원자료 `rooms/researcher1/results.json`

## 요약
1. **[증명 + 계산]** $H_0(T^2)=\mathbb{Z},\ H_1(T^2)=\mathbb{Z}^2,\ H_2(T^2)=\mathbb{Z}$ — CW(1/2/1), Δ(1/3/2), 단체(9꼭짓점 3×3 격자, 16꼭짓점 4×4 격자, 7꼭짓점 최소 삼각분할) 모든 모델에서 일치. 모든 경우 $\partial\circ\partial=0$ 확인, $\chi=0$.
2. **[계산]** $T^3$: $\mathbb{Z},\mathbb{Z}^3,\mathbb{Z}^3,\mathbb{Z}$ (큐브 CW 1/3/3/1, Δ 1/7/12/6, 단체 27/189/324/162). $S^1$: $\mathbb{Z},\mathbb{Z}$. 패턴 $H_k(T^n)\cong\mathbb{Z}^{\binom{n}{k}}$ 와 부합 (일반 $n$ 은 **추측**/쿼넷·퀸네스 정리로 증명될 것).
3. **[계산]** 대조군 클라인 병: $H_1(K)=\mathbb{Z}\oplus\mathbb{Z}/2,\ H_2(K)=0$ (CW, Δ, 3×3·4×4 단체 모두 일치). $\chi(K)=\chi(T^2)=0$ 이므로 **오일러 지표만으로는 $T^2$ 와 $K$ 를 구별 못 하며, 꼬임 $\mathbb{Z}/2$ 와 $H_2$ 가 구별**한다.
4. **구조적 관찰**: 토러스류의 최소 CW 구조에서는 모든 셀룰러 경계사상이 $0$ (접착 단어의 각 문자가 지수합 $0$). 클라인 병은 $aba b^{-1}$ 의 $a$ 지수합 $2$ 가 그대로 $\partial_2 = (2,0)^T$ 가 되어 $\mathbb{Z}/2$ 를 만든다.
5. 단체 모델 SNF: $T^2$ 의 $\partial_2$ 는 비영 불변인자가 전부 $1$, $K$ 는 $1,\dots,1,2$. sympy SNF 와 교차검증 일치.

## 본문

### 0. 방법
- 사슬군 $C_k=\mathbb{Z}^{c_k}$, 경계행렬 $\partial_k$ 의 스미스 표준형 대각 $d_1|d_2|\cdots|d_r$ ($r=\operatorname{rank}\partial_k$) 로부터
  $$H_k \cong \mathbb{Z}^{\,c_k-\operatorname{rank}\partial_k-\operatorname{rank}\partial_{k+1}} \oplus \bigoplus_{d_i(\partial_{k+1})>1}\mathbb{Z}/d_i .$$
- 단체 복합체는 꼭짓점 번호 정렬 순서로 방향을 주고 $\partial[v_0\cdots v_k]=\sum_i(-1)^i[v_0\cdots\hat v_i\cdots v_k]$.
- 유효성 검사(단체 모델): 각 삼각형 꼭짓점 3개 서로 다름, 같은 꼭짓점 집합의 중복 단체 없음, 변이 정확히 2개 삼각형에 속함(의사다양체), 각 꼭짓점 링크가 하나의 원.

### 1. CW 구조 (0-셀 $v$, 1-셀 $a,b$, 2-셀 $e$, 접착 단어 $aba^{-1}b^{-1}$) — **증명(손계산)**
- $\partial_1 a = v-v=0,\ \partial_1 b=0$ (1-셀이 모두 루프).
- 셀룰러 경계 공식: $\partial_2 e=\sum_{\text{1-셀 }x}(\text{단어에서 }x\text{ 의 지수합})\,x = (1-1)a+(1-1)b=0$.
- 사슬 복합체 $0\to\mathbb{Z}\xrightarrow{0}\mathbb{Z}^2\xrightarrow{0}\mathbb{Z}\to0$ 이므로
  $H_0=\mathbb{Z},\ H_1=\mathbb{Z}^2=\langle a,b\rangle,\ H_2=\mathbb{Z}=\langle e\rangle$.

### 2. Δ-복합체 (꼭짓점 1, 변 $a,b,c$, 삼각형 $U,L$; Hatcher 식 대각선 $c$) — **증명(손계산) + 자동생성 재확인**
- $\partial_1=0$ (꼭짓점 1개). $\partial_2 U = a+b-c,\ \partial_2 L = a+b-c$:
  $$\partial_2=\begin{pmatrix}1&1\\1&1\\-1&-1\end{pmatrix}\quad(\text{행 }a,b,c;\ \text{열 }U,L).$$
- SNF 대각 $=(1)$, rank 1. $H_2=\ker\partial_2=\langle U-L\rangle\cong\mathbb{Z}$,
  $H_1=\mathbb{Z}^3/\langle a+b-c\rangle\cong\mathbb{Z}^2$ (기저 $a,b$), $H_0=\mathbb{Z}$.
- Kuhn 삼각분할을 $\mathbb{Z}^2$ 로 나눈 몫($N=1$)을 코드로 자동 생성하면 정확히 같은 행렬이 나옴.

### 3. 단체 복합체 (Python, SNF) — **계산으로 확인**
| 모델 | $(c_0,c_1,c_2)$ | 유효성 | $\partial_2$ 비영 SNF | $H_0,H_1,H_2$ |
|---|---|---|---|---|
| 3×3 격자 (9꼭짓점) | (9,27,18) | 단체 ✓, 의사다양체 ✓, 링크=원 ✓ | 전부 1 (rank 17) | $\mathbb{Z},\mathbb{Z}^2,\mathbb{Z}$ |
| 4×4 격자 (16꼭짓점) | (16,48,32) | 단체 ✓ | 전부 1 | $\mathbb{Z},\mathbb{Z}^2,\mathbb{Z}$ |
| 7꼭짓점 (Möbius–Császár): $\{i,i+1,i+3\},\{i,i+2,i+3\}\bmod 7$ | (7,21,14) | 변 = $K_7$ 전체, 의사다양체 ✓, 링크=6-순환 ✓ | 전부 1 | $\mathbb{Z},\mathbb{Z}^2,\mathbb{Z}$ |
- 모든 경우 $\partial_1\partial_2=0$ 확인.
- 7꼭짓점 모델에서 $\ker\partial_2$ 의 생성원은 14개 삼각형 계수가 전부 $\pm1$ → 기본류(가향성)를 직접 확인.
- 참고: 2×2 격자(Kuhn $N=2$, 4꼭짓점)는 **단체 복합체가 아님**(서로 다른 변이 같은 꼭짓점쌍을 가짐). 그러나 Δ-복합체로 계산하면 호몰로지는 여전히 $\mathbb{Z},\mathbb{Z}^2,\mathbb{Z}$. 9꼭짓점이 "정사각 격자형" 단체 삼각분할의 최소, 7꼭짓점이 전체 최소(Heawood 경계 $\chi=0\Rightarrow n\ge7$).

### 4. 비교 공간
- $S^1$: CW (1,1), $\partial_1=0$; Δ (1,1); 단체 (삼각형 경계 3,3). 모두 $H_0=H_1=\mathbb{Z}$.
- $T^3$:
  - 큐브 CW: 셀 $1,3,3,1$. 각 셀 경계는 마주보는 면이 반대 방향으로 상쇄되어 모든 $\partial_k=0$ (**증명 수준의 손계산**, 코드도 동일 입력).
  - Δ: 단위 큐브의 Kuhn 6사면체를 $\mathbb{Z}^3$ 로 몫 → $(1,7,12,6)$. 
  - 단체: Kuhn 삼각분할 $\bmod 3$ → $(27,189,324,162)$, 단체 복합체임 확인.
  - 결과 모두 $\mathbb{Z},\mathbb{Z}^3,\mathbb{Z}^3,\mathbb{Z}$.
- 클라인 병 $K$ (대조군):
  - CW 단어 $aba b^{-1}$: $\partial_2 e = 2a+0b$, $\partial_2=\binom{2}{0}$ → $H_1=\mathbb{Z}^2/\langle 2a\rangle=\mathbb{Z}\oplus\mathbb{Z}/2$, $H_2=\ker\partial_2=0$.
  - Δ (Hatcher): $\partial U=a+b-c,\ \partial L=a-b+c$, $\partial_2=\begin{pmatrix}1&1\\1&-1\\-1&1\end{pmatrix}$, SNF $(1,2)$ → 같은 결과.
  - 단체: 격자 $(i,0)\sim(i,n),\ (0,j)\sim(m,n-j)$, 3×3 및 4×4 모두 유효한 단체 복합체, SNF 비영 성분 $1,\dots,1,2$ → $\mathbb{Z},\ \mathbb{Z}\oplus\mathbb{Z}/2,\ 0$.

### 5. 종합표
| 공간 | 모델 | 셀/단체 수 $(c_0,c_1,\dots)$ | $H_0$ | $H_1$ | $H_2$ | $H_3$ | $\chi$ |
|---|---|---|---|---|---|---|---|
| $S^1$ | CW | (1,1) | $\mathbb{Z}$ | $\mathbb{Z}$ | – | – | 0 |
| $S^1$ | Δ | (1,1) | $\mathbb{Z}$ | $\mathbb{Z}$ | – | – | 0 |
| $S^1$ | 단체 | (3,3) | $\mathbb{Z}$ | $\mathbb{Z}$ | – | – | 0 |
| $T^2$ | CW $aba^{-1}b^{-1}$ | (1,2,1) | $\mathbb{Z}$ | $\mathbb{Z}^2$ | $\mathbb{Z}$ | – | 0 |
| $T^2$ | Δ | (1,3,2) | $\mathbb{Z}$ | $\mathbb{Z}^2$ | $\mathbb{Z}$ | – | 0 |
| $T^2$ | Δ (2×2 격자, 비단체) | (4,12,8) | $\mathbb{Z}$ | $\mathbb{Z}^2$ | $\mathbb{Z}$ | – | 0 |
| $T^2$ | 단체 3×3 | (9,27,18) | $\mathbb{Z}$ | $\mathbb{Z}^2$ | $\mathbb{Z}$ | – | 0 |
| $T^2$ | 단체 4×4 | (16,48,32) | $\mathbb{Z}$ | $\mathbb{Z}^2$ | $\mathbb{Z}$ | – | 0 |
| $T^2$ | 단체 7꼭짓점 | (7,21,14) | $\mathbb{Z}$ | $\mathbb{Z}^2$ | $\mathbb{Z}$ | – | 0 |
| $T^3$ | 큐브 CW | (1,3,3,1) | $\mathbb{Z}$ | $\mathbb{Z}^3$ | $\mathbb{Z}^3$ | $\mathbb{Z}$ | 0 |
| $T^3$ | Δ (Kuhn) | (1,7,12,6) | $\mathbb{Z}$ | $\mathbb{Z}^3$ | $\mathbb{Z}^3$ | $\mathbb{Z}$ | 0 |
| $T^3$ | 단체 (Kuhn mod 3) | (27,189,324,162) | $\mathbb{Z}$ | $\mathbb{Z}^3$ | $\mathbb{Z}^3$ | $\mathbb{Z}$ | 0 |
| $K$ | CW $abab^{-1}$ | (1,2,1) | $\mathbb{Z}$ | $\mathbb{Z}\oplus\mathbb{Z}/2$ | $0$ | – | 0 |
| $K$ | Δ | (1,3,2) | $\mathbb{Z}$ | $\mathbb{Z}\oplus\mathbb{Z}/2$ | $0$ | – | 0 |
| $K$ | 단체 3×3 | (9,27,18) | $\mathbb{Z}$ | $\mathbb{Z}\oplus\mathbb{Z}/2$ | $0$ | – | 0 |
| $K$ | 단체 4×4 | (16,48,32) | $\mathbb{Z}$ | $\mathbb{Z}\oplus\mathbb{Z}/2$ | $0$ | – | 0 |

모든 행에서 $\sum(-1)^k c_k=\sum(-1)^k \operatorname{rank}H_k$ 확인, $\partial\circ\partial=0$ 확인.

### 6. 증명/계산/추측 구분
- **증명됨(손계산)**: CW·Δ 모델의 $T^2$, $K$, $S^1$ 결과; 큐브 CW $T^3$ (모든 경계 0).
- **계산으로만 확인**: 모든 단체 모델(9·16·7꼭짓점 $T^2$, 27꼭짓점 $T^3$, 9·16꼭짓점 $K$), Kuhn Δ-모델 $T^3$.
- **추측**: $H_k(T^n;\mathbb{Z})\cong\mathbb{Z}^{\binom nk}$, 꼬임 없음 (곱 CW 구조에서 모든 경계 0 → 증명 경로 명확; 퀴네스 정리로도 귀결). 

### 7. 남은 질문 (다음 라운드 제안)
- 일반 $T^n$ 의 곱 CW 구조에서 "모든 셀룰러 경계 = 0" 을 정식으로 증명 (셀룰러 경계의 곱 공식 $\partial(e\times f)=\partial e\times f\pm e\times\partial f$).
- 단체 모델 SNF 가 모두 1 인 이유(꼬임 없음)를 가향성/기본류와 연결: 닫힌 곡면에서 $H_2\neq0 \iff$ 가향, 그리고 $\operatorname{Tors}H_1 \neq 0 \iff$ 비가향.
- 단체 모델 사이 사슬 사상(세분 사상)을 명시적으로 구성해 동형이 실제로 유도됨을 보이는 것.
- 같은 코드로 $\mathbb{Z}/2$ 계수 계산 시 $T^2$ 와 $K$ 의 베티수가 같아짐($1,2,1$)을 보이는 대조 실험.
