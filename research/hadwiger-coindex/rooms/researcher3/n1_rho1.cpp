// rho(G) = min over orders of max over maximal bicliques of label-runs. input: lines "n m u v u v ..."
#include <bits/stdc++.h>
using namespace std;
int rho(int n, vector<int>&nb){
  int full=(1<<n)-1;
  vector<pair<int,int>> P;
  for(int A=1;A<=full;A++){
    int B=full; for(int i=0;i<n;i++) if(A>>i&1) B&=nb[i];
    if(!B) continue;
    int A2=full; for(int i=0;i<n;i++) if(B>>i&1) A2&=nb[i];
    if(A2!=A) continue;
    if(A<B) P.push_back({A,B}); // unordered pair once (A,B)&(B,A): dedupe by A<B
  }
  if(P.empty()) return 1;
  vector<int> perm(n); iota(perm.begin(),perm.end(),0);
  int best=n+1;
  do{
    int mx=0; bool abort_=false;
    for(auto&pr:P){
      int r=0,last=-1;
      for(int i=0;i<n;i++){int v=perm[i]; int l=(pr.first>>v&1)?0:((pr.second>>v&1)?1:-1); if(l<0)continue; if(l!=last){r++;last=l;}}
      if(r>mx){mx=r; if(mx>=best){abort_=true;break;}}
    }
    if(!abort_) best=mx;
  }while(next_permutation(perm.begin(),perm.end()));
  return best;
}
int main(int argc,char**argv){
  int n,m;
  while(scanf("%d %d",&n,&m)==2){
    vector<int> nb(n,0), nb2(n+1,0);
    vector<pair<int,int>> E;
    for(int i=0;i<m;i++){int u,v;scanf("%d %d",&u,&v);nb[u]|=1<<v;nb[v]|=1<<u;}
    int r1=rho(n,nb);
    for(int i=0;i<n;i++) nb2[i]=nb[i]|(1<<n);
    nb2[n]=(1<<n)-1;
    int r2=(argc>1)?0:rho(n+1,nb2);
    printf("%d %d\n",r1,r2); fflush(stdout);
  }
}
