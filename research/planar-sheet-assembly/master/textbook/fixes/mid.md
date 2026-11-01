# 을 (제3장 중심) 수정 블록 - 대상: index.html (현재 버전)

### FIX 1 (R3 / 학생 Q1·Q18: (T1) 증명의 수축 단계를 변 수축으로 한정)
OLD:
<<<
$X_i=X_{i-1}/T$이면 $Z_i:=Z_{i-1}/\sigma_{i-1}(T)$
>>>
NEW:
<<<
$X_i=X_{i-1}/T$ ($T=\{a,b\}\in E(X_{i-1})$, 변 수축)이면 $Z_i:=Z_{i-1}/\sigma_{i-1}(T)$
>>>

### FIX 2 (학생 Q1·Q19 / 형식 R5: (T2) 에 변 수축 포함)
OLD:
<<<
$X$에서 점 삭제 또는 변 삭제 하나로 얻은 그래프 $H$는 $H\preceq X$이다 ($u=1$).
>>>
NEW:
<<<
$X$에서 점 삭제, 변 삭제, 또는 변 수축 가운데 하나로 얻은 그래프 $H$는 $H\preceq X$이다 ($u=1$). 변 수축의 경우 $X_1=X/\{a,b\}$ ($\{a,b\}\in E_X$)이다.
>>>

### FIX 3 (R3 / 학생 Q20: 정의 3.3 바로 뒤 설명을 정확히)
OLD:
<<<
정의 3.3은 한 번의 수축만 허용하므로, 임의의 $T$에 대해 $X/T\preceq X$라는 것은 자명하지 않다.
>>>
NEW:
<<<
정의 3.3의 마이너는 연산 열로 정의되며, 그 열에 쓰이는 수축은 변 수축 $X/\{a,b\}$뿐이다. 임의의 $T$에 대한 $X/T$는 점 개수가 $|V_X|-|T|+1$이므로, $|T|\ge3$이면 변 수축 한 번의 결과 (점 개수 $|V_X|-1$)가 아니다. (반면 $|T|=2$이고 $X[T]$가 연결이면 $T$는 변이므로 $X/T$는 변 수축 한 번이다.) 그래서 $|T|\ge3$인 $X/T\preceq X$는 자명하지 않다.
>>>

### FIX 4 (R5: 예 인용 정정 - 보조명제 3.4 증명 끝)
OLD:
<<<
$X'\preceq X$이다 ((T2)).
>>>
NEW:
<<<
$X'\preceq X$이다 ((T2)의 변 수축, $u=1$).
>>>

### FIX 5 (R2: 보조명제 3.5 증명의 지역 사상 $\rho$ 를 $\rho_{T_i}$ 로)
OLD:
<<<
이하 $\rho:=\rho_{T_i}:V(X_{i-1})\to V(X_i)$ (수축점 $z_i$)로 둔다.
>>>
NEW:
<<<
이하 $\rho_{T_i}:V(X_{i-1})\to V(X_i)$ (수축점 $z_i$)로 둔다.
>>>

### FIX 6 (R2: 보조명제 3.5 증명 (a$_i$)-앞 단락의 $\rho$ 를 $\rho_{T_i}$ 로)
OLD:
<<<
먼저 $\rho\circ\pi_{i-1}=\pi_i$이다 (두 사상 모두 $V_X$에서 $V(X_i)$로 가는 사상이다). $p\in T_k$, $k<i$이면 $\pi_{i-1}(p)=z_k$이고, $z_k\notin T_i$이므로 $\rho(z_k)=z_k=\pi_i(p)$이다. $p\in T_i$이면 $\pi_{i-1}(p)=p$이고 $\rho(p)=z_i=\pi_i(p)$이다. $p\notin T_1\cup\cdots\cup T_i$이면 $\pi_{i-1}(p)=p$이고 $\rho(p)=p=\pi_i(p)$이다.
>>>
NEW:
<<<
먼저 $\rho_{T_i}\circ\pi_{i-1}=\pi_i$이다 (두 사상 모두 $V_X$에서 $V(X_i)$로 가는 사상이다). $p\in T_k$, $k<i$이면 $\pi_{i-1}(p)=z_k$이고, $z_k\notin T_i$이므로 $\rho_{T_i}(z_k)=z_k=\pi_i(p)$이다. $p\in T_i$이면 $\pi_{i-1}(p)=p$이고 $\rho_{T_i}(p)=z_i=\pi_i(p)$이다. $p\notin T_1\cup\cdots\cup T_i$이면 $\pi_{i-1}(p)=p$이고 $\rho_{T_i}(p)=p=\pi_i(p)$이다.
>>>

### FIX 7 (R2: 보조명제 3.5 (b$_i$) 증명의 $\rho$ 를 $\rho_{T_i}$ 로)
OLD:
<<<
(b$_i$) $\subseteq$: $\{\rho s,\rho t\}\in E(X_i)$ ($\{s,t\}\in E(X_{i-1})$, $\rho s\ne\rho t$)라 하자. (b$_{i-1}$)에 의해 $\{s,t\}=\{\pi_{i-1}p,\pi_{i-1}q\}$ ($\{p,q\}\in E_X$, $\pi_{i-1}p\ne\pi_{i-1}q$)로 쓸 수 있다. $\rho\pi_{i-1}=\pi_i$에 의해 $\{\rho s,\rho t\}=\{\pi_ip,\pi_iq\}$이고 $\pi_ip\ne\pi_iq$이다. $\supseteq$: $\{p,q\}\in E_X$이고 $\pi_ip\ne\pi_iq$라 하자. 먼저 $\pi_{i-1}p\ne\pi_{i-1}q$이다. 실제로 같다면 $\pi_ip=\rho\pi_{i-1}p=\rho\pi_{i-1}q=\pi_iq$가 되어 모순이다. 따라서 (b$_{i-1}$)에 의해 $\{\pi_{i-1}p,\pi_{i-1}q\}\in E(X_{i-1})$이고, $\rho$를 적용하면 $\{\pi_ip,\pi_iq\}\in E(X_i)$이다.
>>>
NEW:
<<<
(b$_i$) $\subseteq$: $\{\rho_{T_i}s,\rho_{T_i}t\}\in E(X_i)$ ($\{s,t\}\in E(X_{i-1})$, $\rho_{T_i}s\ne\rho_{T_i}t$)라 하자. (b$_{i-1}$)에 의해 $\{s,t\}=\{\pi_{i-1}p,\pi_{i-1}q\}$ ($\{p,q\}\in E_X$, $\pi_{i-1}p\ne\pi_{i-1}q$)로 쓸 수 있다. $\rho_{T_i}\pi_{i-1}=\pi_i$에 의해 $\{\rho_{T_i}s,\rho_{T_i}t\}=\{\pi_ip,\pi_iq\}$이고 $\pi_ip\ne\pi_iq$이다. $\supseteq$: $\{p,q\}\in E_X$이고 $\pi_ip\ne\pi_iq$라 하자. 먼저 $\pi_{i-1}p\ne\pi_{i-1}q$이다. 실제로 같다면 $\pi_ip=\rho_{T_i}\pi_{i-1}p=\rho_{T_i}\pi_{i-1}q=\pi_iq$가 되어 모순이다. 따라서 (b$_{i-1}$)에 의해 $\{\pi_{i-1}p,\pi_{i-1}q\}\in E(X_{i-1})$이고, $\rho_{T_i}$를 적용하면 $\{\pi_ip,\pi_iq\}\in E(X_i)$이다.
>>>

### FIX 8 (형식 R5: 정리 3.6 증명의 인용 정정)
OLD:
<<<
(3.2와 정의 2.3의 그래프임)
>>>
NEW:
<<<
(보조명제 2.2 (1)과 정의 2.3에 의해 $E_{00}$의 원소는 $\binom{V_0}2$의 원소이고, $E_{01}$의 원소는 $V_0$의 점과 $V_1$의 점의 쌍이므로 $\binom{V(\mathfrak M)}2$의 원소이다)
>>>

### FIX 9 (형식 R5: 정리 3.6 (a)의 인용 정정)
OLD:
<<<
같은 $v$의 두 복사점 $(v,k)$, $(v,l)$은 보조명제 2.2 (1)에 의해 $E_{00}$의 변으로 이어지지 않는다.
>>>
NEW:
<<<
같은 $v$의 두 복사점 $(v,k)$, $(v,l)$ ($k\ne l$)은 $E_{00}$의 변으로 직접 이어지지 않는다 (정의 2.1: $E_{00}$의 변의 두 끝점은 두 번째 성분이 같다).
>>>

### FIX 10 (형식 R7 / R5: 예 7.2 의 수축 인용 정정)
OLD:
<<<
(T2)와 (T3)에 의해 $C_3\preceq C_4$이다.
>>>
NEW:
<<<
$\{1,4\}$는 $C_4$의 변이므로 $C_4/\{1,4\}$는 변 수축 한 번의 결과이고 ((T2)의 변 수축, $u=1$), 이것은 $C_3$와 동형이므로 (T3)에 의해 $C_3\preceq C_4$이다.
>>>
