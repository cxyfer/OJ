#include <bits/stdc++.h>
using namespace std;

int main(){
    int n,t,dir;
    cin >> n;
    int x[n]={0};
    for (int i=0;i<n;i++) cin >> x[i];
    cin >> t;
    dir = (x[t-1]-x[t]>x[t-1]-x[t-2]||t==1)?1:-1; //consider t=1(dir=+1)
    while((x[t-1]-x[t-1+dir])>=0) t=t+dir;
    cout << t << endl;
	return 0;
}
