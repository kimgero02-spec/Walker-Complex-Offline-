# 보조명제 1.4 (사이클 $C_n$의 평면성) 엄밀 증명 — 연구원 작성

판정: **완결**. 아래 증명은 교재가 정의 없이 쓰는 "평면 그래프"의 표준 정의 (아래 (P1)–(P3))와 초등 해석기하 (행렬식, 삼각함수 항등식, 볼록성)만 쓴다. 이 책 밖의 정리는 인용하지 않는다.

---

## (1) 정의 명시

**그래프 규약** (교재 규약 2를 따른다). $G=(V,E)$, $V$는 유한 집합, $E\subseteq\binom V2$.

**평면 그래프 (교재의 표준 용어, 여기서 명시).** $G=(V,E)$가 평면 그래프라는 것은 다음 자료가 존재하는 것이다.

- 점 사상 $\varphi:V\to\mathbb R^2$,
- 각 변 $e=\{u,v\}\in E$에 대하여 연속 함수 $\gamma_e:[0,1]\to\mathbb R^2$ (단순 곡선: 단사이며 연속). 그 끝점은 $\{\gamma_e(0),\gamma_e(1)\}=\{\varphi(u),\varphi(v)\}$이다.

이 자료가 다음 세 조건을 만족해야 한다.

- **(P1)** $\varphi$는 단사이다. (서로 다른 점은 서로 다른 점으로 그린다.)
- **(P2)** 각 변 $e$에 대하여, $\varphi(w)\notin\gamma_e([0,1])$이 모든 $w\in V\setminus e$에 대해 성립한다. (변은 자기 끝점이 아닌 다른 점을 지나지 않는다.)
- **(P3)** 서로 다른 두 변 $e\ne f$에 대하여 $\gamma_e([0,1])\cap\gamma_f([0,1])\subseteq\varphi(e\cap f)$이다. (두 변의 곡선은 공통 끝점 외에서 만나지 않는다.)

이것이 교재의 "평면 그래프"와 같은 정의이다. 교재가 평면 그래프를 "평면 그림을 가지는 그래프"로 쓰는 용법 (정리 6.1, 예 1.2, 예 1.5의 검증 등) 과 같고, 이는 표준 정의 (그래프의 평면 임베딩 존재) 그 자체이다. 본 증명은 $\gamma_e$를 직선 선분으로 잡는다. 직선 선분은 단순 곡선이므로, 곡선 기반의 어떤 표준 정의에서도 위 조건을 만족하는 그림이 된다.

---

## (2) 기하 보조 사실과 증명

모든 점은 $\mathbb R^2$의 원소이다. $x\cdot y$는 내적, $\det(x,y)=x_1y_2-x_2y_1$은 행렬식(2차 외적)이다. 원 $S^1$은 단위원 $\{x:|x|=1\}$이다. 

$\theta\in\mathbb R$에 대하여 $p(\theta):=(\cos\theta,\sin\theta)\in S^1$이다. $n\ge3$에 대하여 $\delta:=2\pi/n$, $\theta_j:=j\delta$, $p_j:=p(\theta_j)$로 둔다. $\theta_{j+n}=\theta_j+2\pi$이므로 $p_j$는 $j$를 $\bmod\ n$으로 본 것이 잘 정의된다. 지표 $j,k$는 항상 $\bmod\ n$으로 읽는다.

### 보조사실 A (삼각함수의 기본 사실)

**A1.** $\cos x=\cos y \iff x\equiv\pm y \pmod{2\pi}$.

*증명.* $\cos x-\cos y=-2\sin\frac{x+y}2\sin\frac{x-y}2$이다. 따라서 $\cos x=\cos y$는 $\sin\frac{x+y}2=0$ 또는 $\sin\frac{x-y}2=0$과 동치이고, 이는 $x+y\in2\pi\mathbb Z$ 또는 $x-y\in2\pi\mathbb Z$와 동치이다. $\square$

**A2.** $\cos$는 $[0,\pi]$에서 엄격 감소한다. (미분 기초.)

**A3.** $p(\theta)=p(\theta')\iff\theta-\theta'\in2\pi\mathbb Z$.

*증명.* $p(\theta)=p(\theta')$이면 $\cos(\theta-\theta')=\cos\theta\cos\theta'+\sin\theta\sin\theta'=|p(\theta)|^2=1$이므로 $\theta-\theta'\in2\pi\mathbb Z$. 역은 주기성. $\square$

### 보조사실 B (점들의 서로 다름)

**B1.** 정수 $i,j$에 대하여 $p_i=p_j\iff i\equiv j\pmod n$. 특히 $p_1,\dots,p_n$은 서로 다른 $n$개의 점이다.

*증명.* A3에 의해 $p_i=p_j\iff\theta_i-\theta_j=2\pi(i-j)/n\in2\pi\mathbb Z\iff n\mid(i-j)$. $\square$

### 보조사실 C (원 위의 세 점은 한 직선 위에 있지 않다; 직선과 원의 교점은 많아야 두 개)

**C1.** $x,y,z\in S^1$이 서로 다르면 $x,y,z$는 한 직선 위에 있지 않다. 따라서 임의의 직선과 $S^1$의 교점은 최대 두 개이다.

*증명.* $x\ne y$라 하고 $z$가 직선 $xy$ 위에 있다고 하자. 그러면 $z=x+t(y-x)$인 $t\in\mathbb R$가 있다. $|x|=|y|=1$이므로 $|y-x|^2=2-2x\cdot y$이고 $x\cdot(y-x)=x\cdot y-1=-\tfrac12|y-x|^2$이다. 따라서

$$|z|^2=1+2t\,x\cdot(y-x)+t^2|y-x|^2=1-t|y-x|^2+t^2|y-x|^2=1+t(t-1)|y-x|^2.$$

$|z|=1$이고 $y\ne x$이므로 $t(t-1)=0$, 즉 $t\in\{0,1\}$이다. 그러면 $z\in\{x,y\}$이어서 $z$가 $x,y$와 서로 다르다는 가정에 모순이다. 직선과 $S^1$의 교점이 세 개 이상이면 그중 서로 다른 세 점이 같은 직선 위에 있으므로 이것도 모순이다. $\square$

### 보조사실 D (열린 반평면과 볼록성)

$a\ne b$인 $a,b\in\mathbb R^2$에 대하여

$$\ell_{ab}(x):=\det(b-a,\;x-a)$$

로 둔다. $\ell_{ab}$는 $x$의 아핀 함수이고 $\ell_{ab}(a)=\ell_{ab}(b)=0$이며 상수가 아니다. 그러므로 그 영점집합 $L_{ab}:=\{x:\ell_{ab}(x)=0\}$은 직선이고, $a,b$를 지나므로 직선 $ab$와 일치한다. 열린 반평면은 $H^+_{ab}:=\{\ell_{ab}>0\}$, $H^-_{ab}:=\{\ell_{ab}<0\}$이다.

**D1 (볼록성).** $x,y\in H^+_{ab}$이고 $t\in[0,1]$이면 $(1-t)x+ty\in H^+_{ab}$이다. 따라서 선분 $[x,y]\subseteq H^+_{ab}$이고 $[x,y]\cap L_{ab}=\varnothing$이다.

*증명.* $\ell_{ab}$가 아핀이므로 $\ell_{ab}((1-t)x+ty)=(1-t)\ell_{ab}(x)+t\,\ell_{ab}(y)$이다. 이것은 두 양수의 볼록결합이므로 양수이다. $\square$

**D2 (행렬식 표현).** $\ell_{ab}(x)=\det(b-a,x)+\det(a,b)$이다.

*증명.* $\det(b-a,x-a)=\det(b-a,x)-\det(b-a,a)$이고 $\det(b-a,a)=\det(b,a)=-\det(a,b)$이다. $\square$

### 보조사실 E (핵심 기하 사실: 다른 점들은 한쪽 반평면에 있다)

**E1.** 정수 $j$와 $a=p_j$, $b=p_{j+1}$에 대하여, $k\not\equiv j,\ j+1\pmod n$인 모든 정수 $k$에 대해

$$\ell_{ab}(p_k)>0,$$

즉 $p_k\in H^+_{ab}$이다. 특히 $p_k\notin L_{ab}$이다.

*증명.* $\alpha:=\theta_j=j\delta$, $\beta:=\alpha+\delta$, $m:=\frac{\alpha+\beta}2$로 둔다. $\delta/2=\pi/n\in(0,\pi/3]$이므로 $s:=2\sin\frac\delta2>0$이다. 차의 합-곱 공식에 의해

$$\cos\beta-\cos\alpha=-2\sin m\sin\tfrac\delta2=-s\sin m,\qquad \sin\beta-\sin\alpha=2\cos m\sin\tfrac\delta2=s\cos m$$

이므로 $b-a=s(-\sin m,\ \cos m)$이다. 따라서 $x=p(\theta)$에 대하여

$$\det(b-a,x)=s(-\sin m\sin\theta-\cos m\cos\theta)=-s\cos(\theta-m).$$

또 $\det(a,b)=\cos\alpha\sin\beta-\sin\alpha\cos\beta=\sin\delta=s\cos\frac\delta2$이다 ($\sin\delta=2\sin\frac\delta2\cos\frac\delta2$). D2에 의해

$$\ell_{ab}(p(\theta))=s\Bigl(\cos\tfrac\delta2-\cos(\theta-m)\Bigr).$$

이제 $\theta=\theta_k=k\delta$를 넣는다. $\theta_k-m=(k-j)\delta-\frac\delta2=\frac{(2q-1)\pi}n$이고 $q:=k-j$이다. $\frac\delta2=\frac\pi n$이므로

$$\ell_{ab}(p_k)=s\Bigl(\cos\tfrac\pi n-\cos\tfrac{o\pi}n\Bigr),\qquad o:=2q-1\ (\text{홀수}).$$

**(i) $\cos\frac{o\pi}n\le\cos\frac\pi n$.** $o$를 $2n$으로 나눈 나머지 쪽으로 옮긴다: $r:=\operatorname{round}(o/2n)$로 두고 $o':=o-2nr$로 하면 $|o'|\le n$이고 $o'$는 홀수이므로 $1\le|o'|\le n$이다. $\cos$의 $2\pi$ 주기성과 우함수성에 의해 $\cos\frac{o\pi}n=\cos\frac{o'\pi}n=\cos\frac{|o'|\pi}n$이다. $\frac{|o'|\pi}n\in[\frac\pi n,\pi]$이므로 A2에 의해 $\cos\frac{|o'|\pi}n\le\cos\frac\pi n$이다.

**(ii) 등호 조건.** A1에 의해 $\cos\frac{o\pi}n=\cos\frac\pi n\iff\frac{o\pi}n\equiv\pm\frac\pi n\pmod{2\pi}\iff o\equiv\pm1\pmod{2n}$이다.

$o=2q-1$에 대하여 $o\equiv1\pmod{2n}\iff q\equiv1\pmod n$이고, $o\equiv-1\pmod{2n}\iff q\equiv0\pmod n$이다. 따라서 $k\not\equiv j,j+1\pmod n$ (즉 $q\not\equiv0,1$)이면 (ii)에 의해 (i)의 부등식이 엄격하다. 그러면 $\ell_{ab}(p_k)=s(\cos\frac\pi n-\cos\frac{o\pi}n)>0$이다. $\square$

**E2 (보조).** $n\ge3$이면 $k\equiv j$ 또는 $j+1$이 아닌 $k$에 대해서만 E1을 쓴다. E1의 조건이 바로 그 조건이므로 추가 가정은 없다.

---

## (3) 보조명제 1.4 증명

**설정.** $n\ge3$, $V=\{c_1,\dots,c_n\}$, $E=\{e_1,\dots,e_n\}$, $e_j:=\{c_j,c_{j+1}\}$ (지표는 $\bmod\ n$). $n\ge3$이므로 $e_1,\dots,e_n$은 서로 다른 $n$개의 변이다. 실제로 $e_j=e_k$이면 $\{j,j+1\}=\{k,k+1\}$ (mod $n$)이고, $j=k+1$, $j+1=k$이면 $2\equiv0\pmod n$이므로 $n\le2$이다. 따라서 $j\equiv k$이다.

$\varphi(c_j):=p_j$ $(j=1,\dots,n)$, $\gamma_{e_j}(t):=(1-t)p_j+t\,p_{j+1}$ $(t\in[0,1])$로 둔다. $a_j:=p_j$, $b_j:=p_{j+1}$로 쓴다.

**(P1)** B1에 의해 $p_1,\dots,p_n$은 서로 다르므로 $\varphi$는 단사이다.

**단순 곡선.** $\gamma_{e_j}$는 연속이고, $a_j\ne b_j$ (B1, $n\ge2$)이므로 $\gamma_{e_j}(t)=\gamma_{e_j}(t')$이면 $(t-t')(b_j-a_j)=0$, 즉 $t=t'$이다. 따라서 단사이다. 끝점은 $\gamma_{e_j}(0)=p_j=\varphi(c_j)$, $\gamma_{e_j}(1)=p_{j+1}=\varphi(c_{j+1})$이다.

**(P2) 다른 점을 지나지 않음.** $w=c_k$, $k\not\equiv j,j+1$이라 하자. $\gamma_{e_j}([0,1])=[a_j,b_j]\subseteq L_{a_jb_j}$이다 (아핀 함수 $\ell$의 영점집합은 $a_j,b_j$를 포함하는 볼록 집합). E1에 의해 $p_k\notin L_{a_jb_j}$이므로 $p_k\notin[a_j,b_j]$이다. 즉 $\varphi(w)\notin\gamma_{e_j}([0,1])$이다.

**(P3) 서로 다른 두 변.** $j\not\equiv k$라 하자. 두 경우가 전부이다.

*경우 A: $\{j,j+1\}\cap\{k,k+1\}=\varnothing$ (mod $n$)* (끝점을 공유하지 않는 경우). 그러면 $k,k+1\not\equiv j,j+1$이다. E1을 지표 $k$와 $k+1$에 적용하면 $p_k,p_{k+1}\in H^+_{a_jb_j}$이다. D1에 의해 $[p_k,p_{k+1}]\subseteq H^+_{a_jb_j}$이고 $[p_k,p_{k+1}]\cap L_{a_jb_j}=\varnothing$이다. 그런데 $\gamma_{e_j}([0,1])\subseteq L_{a_jb_j}$이므로 두 곡선 상은 서로소이다. 특히 교집합은 $\varnothing=\varphi(e_j\cap e_k)$에 포함된다.

*경우 B: 끝점을 정확히 하나 공유.* 두 변은 서로 다르므로 $\{j,j+1\}\cap\{k,k+1\}$의 원소는 한 개를 넘지 않는다 (두 개면 두 변이 같아진다). 공유점을 $P=p_m$ ($\varphi$로 옮긴 점)이라 하고, 두 변의 다른 끝점을 $A\ne B$로 두자. $A,B$는 $P$와 다르다. 따라서 $P,A,B$는 $S^1$ 위의 서로 다른 세 점이다. 이 두 변의 상은 $[P,A]$, $[P,B]$이다.

$x\in[P,A]\cap[P,B]$이고 $x\ne P$라 하자. $x=P+t(A-P)$, $t\in(0,1]$, 그리고 $x=P+t'(B-P)$, $t'\in(0,1]$이다. 그러면 $A-P=(x-P)/t$, $B-P=(x-P)/t'$이므로 $A,B,P$는 모두 직선 $P+\mathbb R(x-P)$ 위에 있다. 이것은 C1에 모순이다. 따라서 $[P,A]\cap[P,B]\subseteq\{P\}=\varphi(e\cap f)$이다. (P3)이 성립한다.

두 경우 A, B가 모든 경우를 덮는다. 따라서 (P1)–(P3)이 모두 성립하고, $C_n$은 평면 그래프이다. $\blacksquare$

---

## (4) 직접 확인 예

**$n=3$.** $\theta_1=120^\circ$, $\theta_2=240^\circ$, $\theta_3=0^\circ$이므로
$p_1=(-\tfrac12,\tfrac{\sqrt3}2)$, $p_2=(-\tfrac12,-\tfrac{\sqrt3}2)$, $p_3=(1,0)$이다.
세 변은 모두 서로 끝점을 공유하므로 경우 B만 나타난다.

- $e_1=[p_1,p_2]$는 직선 $x=-\tfrac12$ 위의 선분이다.
- $e_2=[p_2,p_3]=\{(-\tfrac12+\tfrac32t,\ -\tfrac{\sqrt3}2+\tfrac{\sqrt3}2t)\}$. 여기서 $x=-\tfrac12$이면 $t=0$이므로 $e_1\cap e_2=\{p_2\}$이다.
- $e_3=[p_3,p_1]=\{(1-\tfrac32s,\ \tfrac{\sqrt3}2s)\}$. $e_2\cap e_3$에서 $x$ 좌표가 같으면 $t+s=1$, $y$ 좌표가 같으면 $t-s=1$이므로 $t=1$, $s=0$, 즉 $e_2\cap e_3=\{p_3\}$이다.
- $e_1\cap e_3$: $x=-\tfrac12$에서 $e_3$은 $s=1$, 즉 $p_1$뿐이므로 $\{p_1\}$이다.

E1 검사: $j=1$일 때 $p_3$에 대하여 $q=2$, $o=3$이므로 $\ell_{p_1p_2}(p_3)=\sqrt3\,(\cos\frac\pi3-\cos\pi)=\frac{3\sqrt3}{2}>0$이다. 이것은 $p_3$의 $x$좌표 $1$이 $L$ ($x=-\frac12$)의 같은 쪽에 있다는 것과 일치한다.

**$n=4$.** $p_1=(0,1)$, $p_2=(-1,0)$, $p_3=(0,-1)$, $p_4=(1,0)$. 변은 $e_1=[p_1,p_2]$, $e_2=[p_2,p_3]$, $e_3=[p_3,p_4]$, $e_4=[p_4,p_1]$이다.

- 경우 A: $\{e_1,e_3\}$, $\{e_2,e_4\}$. $e_1=\{(x,x+1):x\in[-1,0]\}$, $e_3=\{(x,x-1):x\in[0,1]\}$이다. 두 선분의 $x$ 좌표 범위는 $[-1,0]\cap[0,1]=\{0\}$이고, $x=0$에서 $e_1$은 $y=1$, $e_3$은 $y=-1$이므로 교점이 없다. $\{e_2,e_4\}$도 같은 방식으로 $x=0$에서 $e_2$는 $y=-1$, $e_4$는 $y=1$이므로 서로소이다.
- E1 검사: $j=1$, $L$은 $y=x+1$. $p_3=(0,-1)$, $p_4=(1,0)$은 모두 $y-x-1<0$에 있다 (부호는 $\ell$과 반대이지만 같은 쪽이다). 공식으로 $q=2$일 때 $\ell(p_3)=\sqrt2(\cos\frac\pi4-\cos\frac{3\pi}4)=2$, $q=3$일 때 $\ell(p_4)=\sqrt2(\cos\frac\pi4-\cos\frac{5\pi}4)=2$이다. 두 값 모두 양수로 일치한다.
- 경우 B: 예를 들어 $e_1,e_2$는 공유점 $p_2$를 가지며 다른 끝점은 $p_1=(0,1)$, $p_3=(0,-1)$이다. 이 두 선분은 $x=0$ 위에서 각각 $p_1$, $p_3$만 가지므로 $\{p_2\}$에서만 만난다.

---

## 주석: 교재 본문과의 차이

교재의 현행 증명 (b)는 "원의 두 열린 호 $A_1,A_2$ 위의 점들이 $L$의 서로 다른 열린 반평면에 들어간다"와 "짧은 호에는 $p$가 없다"를 증명 없이 쓴다. 본 증명의 E1이 이 부분 (그리고 반평면 쪽 판정)을 계산으로 대체한다. 교재 (a)의 "단위원 위의 세 서로 다른 점은 한 직선 위에 있지 않다"는 본 증명의 C1이다.

교재 본문을 고칠 때는 증명 (b)를 "E1 (다른 점 $p_k$, $p_{k+1}$은 $\ell_{p_jp_{j+1}}$의 같은 양의 쪽에 있다)"로 교체하는 것을 권한다. 이 편집은 실행하지 않았다 (교재 수정 금지).

---

## (5) 남은 가정

1. **평면 그래프의 정의.** 교재는 "평면 그래프"를 정의 없이 쓴다. 본 증명은 (P1)–(P3)을 그 정의로 쓴다. 이것은 표준 정의이다. 다른 표준 정의 (곡선이 다각선인 경우, 위상적 임베딩 등)를 쓰면, 본 증명의 직선 선분 그림은 여전히 그 정의의 조건을 만족한다 (선분은 단순 곡선이고 다각선이다). 이 정도의 가정 외에는 남은 가정이 없다.
2. 사용한 초등 사실: 행렬식과 삼각함수 항등식 (덧셈 공식, 합차곱 공식), $\cos$의 $[0,\pi]$에서의 엄격 감소, $\cos$의 주기성과 우함수성. 모두 미적분 기초이며 이 책 밖의 정리가 아니다.

**판정: 완결.**
