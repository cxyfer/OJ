#include <bits/stdc++.h>
using namespace std;

int main(){
    int a,b,c,x1,x2;
    cin >> a >> b >> c;
    if (b*b<4*a*c) cout << "No real root" << endl;
    else if (b*b==4*a*c) cout << "Two same roots x=" << b/(-2*a) << endl;
    else{
        x1 = (b-sqrt(b*b-4*a*c))/(-2*a);
        x2 = (b+sqrt(b*b-4*a*c))/(-2*a);
        cout << "Two different roots x1=" << x1 << " , x2=" << x2 << endl;
    }
	return 0;
}
