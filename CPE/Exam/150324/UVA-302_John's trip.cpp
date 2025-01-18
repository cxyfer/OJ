#include<bits/stdc++.h>
#define PII pair<int,int>
#define fi first
#define se second
using namespace std;
const int N=2001;
int n,m,u,v,w,s,d[N],ans[N],l;
bool vis[N],e;
vector<PII>G[N];
void dfs(int u){
	for(int i=0;i<G[u].size();i++){
		int v=G[u][i].se,w=G[u][i].fi; 
		if(vis[w]) continue;
        vis[w]=1;
		dfs(v);
        ans[++l]=w;
	}
}
int main(){
    while(cin>>u>>v){
        if(!u&&!v){
            if(!e) break;
            for(int i=1;i<=2000;i++){
                sort(G[i].begin(),G[i].end());
                if(d[i]%2){
                    cout<<"Round trip does not exist.\n";
                    goto T2;
                }
            }
            dfs(s);
            while(l>1) cout<<ans[l--]<<" ";
            cout<<ans[l--]<<endl;
            T2:;
            memset(vis,0,sizeof vis);
            memset(d,0,sizeof d);
            for(int i=1;i<=2000;i++) G[i].clear();
            s=0;
            e=0;
            cout<<endl;
            continue;
        }
        e=1;
        cin>>w;
        if(!s) s=min(u,v);
        G[u].push_back({w,v});
        G[v].push_back({w,u});
        d[u]--;
        d[v]++;
    }
}