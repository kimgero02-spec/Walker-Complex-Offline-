### FIX 1 (보조명제 3.5 변집합 증명)
OLD:
<<<
점집합은 정의 3.3에서 바로 나온다. 수축 $X_i=X_{i-1}/T_i$에서 $V(X_{i-1})\setminus T_i$는 $V_X\setminus(T_1\cup\cdots\cup T_i)$와 $z_1,\dots,z_{i-1}$의 서로소 합집합이고, 여기에 수축점 $z_i$가 더해진다. 변집합은 귀납으로 다음과 같이 얻어진다. $\pi_i=\rho_{T_i}\circ\pi_{i-1}$이고, 정의 3.3의 변 집합 공식을 $X_{i-1}$에서 $X_i$로 적용하면 $E(X_i)=\{\{\pi_i p,\pi_i q\}:\{p,q\}\in E_X,\ \pi_i p\ne\pi_i q\}$를 얻는다. 여기서 $\pi_i p\ne\pi_i q$이면 $\pi_{i-1}p\ne\pi_{i-1}q$이므로 귀납 가정을 쓸 수 있다. $\square$
>>>
NEW:
<<<
점집합은 정의 3.3에서 바로 나온다. 수축 $X_i=X_{i-1}/T_i$에서 $V(X_{i-1})\setminus T_i$는 $V_X\setminus(T_1\cup\cdots\cup T_i)$와 $z_1,\dots,z_{i-1}$의 서로소 합집합이고, 여기에 수축점 $z_i$가 더해진다. 변집합은 다음과 같이 귀납으로 얻는다. 먼저 $\rho:=\rho_{T_i}$ (정의역은 $V(X_{i-1})$)라 하면 $\pi_i=\rho\circ\pi_{i-1}$이다. 실제로 $p\in V_X$에 대해 세 경우를 본다. (가) $p\in T_k$ ($k\le i-1$)이면 $\pi_{i-1}p=z_k$이고, $z_k\notin V_X$이고 $T_i\subseteq V_X$이므로 $z_k\notin T_i$이다. 따라서 $\rho z_k=z_k$, 즉 $\rho\pi_{i-1}p=z_k=\pi_ip$이다. (나) $p\in T_i$이면 $p\notin T_1\cup\cdots\cup T_{i-1}$이므로 $\pi_{i-1}p=p$이고 $\rho p=z_i=\pi_ip$이다. (다) $p\notin T_1\cup\cdots\cup T_i$이면 $\pi_{i-1}p=p$, $\rho p=p=\pi_ip$이다.

이제 $0\le i\le r$에 대해 다음을 귀납으로 보인다.
$$(\ast_i)\qquad E(X_i)=\{\{\pi_i p,\pi_i q\}:\ \{p,q\}\in E_X,\ \pi_i p\ne\pi_i q\}.$$

기저 $i=0$: $\pi_0=\mathrm{id}$, $X_0=X$이므로 $(\ast_0)$의 우변은 $E_X$ 자체이다 (변은 두 점의 집합이므로 $p\ne q$는 자동이다). 따라서 $(\ast_0)$이 성립한다.

귀납 단계: $1\le i\le r$이고 $(\ast_{i-1})$이 성립한다고 하자. 정의 3.3에 의해 $E(X_i)=\{\{\rho s,\rho t\}:\ \{s,t\}\in E(X_{i-1}),\ \rho s\ne\rho t\}$이다.

($\subseteq$) $e\in E(X_i)$라 하자. 위 식에 의해 $\{s,t\}\in E(X_{i-1})$, $\rho s\ne\rho t$, $e=\{\rho s,\rho t\}$가 있다. $(\ast_{i-1})$에 의해 $\{p,q\}\in E_X$, $\pi_{i-1}p\ne\pi_{i-1}q$, $\{s,t\}=\{\pi_{i-1}p,\pi_{i-1}q\}$가 있다. 여기서 $\pi_{i-1}p\ne\pi_{i-1}q$여야 하는 이유는 다음과 같다. 만약 $\pi_{i-1}p=\pi_{i-1}q$이면 $\{s,t\}$가 한 원소짜리 집합이 되어, $s\ne t$인 변 $\{s,t\}$와 모순된다 (또는 $\rho s=\rho\pi_{i-1}p=\rho\pi_{i-1}q=\rho t$가 되어 $\rho s\ne\rho t$와 모순된다). 따라서 $\pi_{i-1}p\ne\pi_{i-1}q$이다. 이제 $\pi_i=\rho\circ\pi_{i-1}$을 쓰면 $\{\rho s,\rho t\}=\{\rho\pi_{i-1}p,\rho\pi_{i-1}q\}=\{\pi_ip,\pi_iq\}$이고, $\rho s\ne\rho t$이므로 $\pi_ip\ne\pi_iq$이다. 따라서 $e=\{\pi_ip,\pi_iq\}$이고 $\{p,q\}\in E_X$, $\pi_ip\ne\pi_iq$이므로 $e$는 $(\ast_i)$의 우변에 속한다.

($\supseteq$) $\{p,q\}\in E_X$, $\pi_ip\ne\pi_iq$라 하자. 먼저 $\pi_{i-1}p\ne\pi_{i-1}q$이다. 실제로 $\pi_{i-1}p=\pi_{i-1}q$이면 $\pi_ip=\rho\pi_{i-1}p=\rho\pi_{i-1}q=\pi_iq$가 되어 가정에 모순된다. 그러므로 $(\ast_{i-1})$의 우변 조건이 성립하고, $(\ast_{i-1})$에 의해 $\{\pi_{i-1}p,\pi_{i-1}q\}\in E(X_{i-1})$이다. 이제 $s:=\pi_{i-1}p$, $t:=\pi_{i-1}q$로 두면 $\{s,t\}\in E(X_{i-1})$이고 $\rho s=\pi_ip\ne\pi_iq=\rho t$이다. 정의 3.3에 의해 $\{\rho s,\rho t\}=\{\pi_ip,\pi_iq\}\in E(X_i)$이다.

두 포함이 모두 성립하므로 $(\ast_i)$가 성립한다. 귀납이 끝나고 $i=r$의 경우가 (b) $E(X_r)=\{\{\pi_rp,\pi_rq\}:\{p,q\}\in E_X,\ \pi_rp\ne\pi_rq\}$이다. $\square$
>>>
