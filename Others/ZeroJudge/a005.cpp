#include <bits/stdc++.h>
using namespace std;

int main(){
    int n, num[5];
    cin >> n;
    while(n--){
        for(int i=0;i<4;i++) cin >> num[i];
        if ((num[2]-num[1])==(num[1]-num[0])) num[4]=num[3]+(num[3]-num[2]);
        else num[4] = num[3]*(num[3]/num[2]);
        for(int i=0;i<5;i++) i==4? cout<<num[i]<<endl : cout<<num[i]<<" ";
    }
    return 0;
}
