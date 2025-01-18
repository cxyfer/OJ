#include<bits/stdc++.h>
using namespace std;
 
#define endl '\n'
#define ll long long
#define int long long
 
signed main(){
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    int t;
    cin>>t;
    while(t--){
    	int n;
    	cin>>n;
    	vector<int>arr(n+1);
    	for(int i=1;i<=n;i++){
    		cin>>arr[i];
    	}
    	vector<int>brr(n+2);
    	brr[n+1]=0;
    	brr[n]=arr[n];
    	for(int i=n-1;i>=1;i--){
    		brr[i]=brr[i+1]+arr[i];
    	}
    	int ans=0;
    	for(int i=1;i<=n;i++){
            ans+=arr[i];
            if(brr[i+1]>=0){
            	ans+=brr[i+1];
            }
    	}
    	cout<<ans<<endl;
    }
    return 0;
}