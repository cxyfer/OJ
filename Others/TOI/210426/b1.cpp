#include <bits/stdc++.h>
using namespace std;

int main(){
    int n,hmin=1000,wmin=1000;
    cin >> n;
    int h[n]={0},w[n]={0};

    for(int i=0;i<n;i++) cin >> h[i];
    for(int i=0;i<n;i++) cin >> w[i];
    while(n--){
        if (h[n]*w[n] < hmin*wmin){
            hmin = h[n];
            wmin = w[n];
        }
    }
    cout << hmin << " " << wmin << endl;
	return 0;
}
