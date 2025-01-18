#include <bits/stdc++.h>
using namespace std;

int main(){
    int n, s, d, num=0, fee=0;
    cin >> n;
    int books[n] = {0};

    while(n--){
        cin >> s >> d;
        if (d>100){
            fee  += (d-100)*5;
            books[num] = s;
            num++;
        }
    }
    sort(books, books + num);
    if(num==0) cout << 0 << endl;
    else{
        for (int i=0;i<num;i++){
            cout << books[i] ;
            i+1==num? cout<<endl : cout<<" ";
        }
        cout << fee ;
    }
	return 0;
}
