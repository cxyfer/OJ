#include <bits/stdc++.h>
using namespace std;

int main(){
    int n, a, b, c;
    while (cin >> n){
        a = n / 100;
        b = n / 10 % 10;
        c = n % 10;
        if (n == pow(a, 3) + pow(b, 3) + pow(c, 3)) {
            cout << "Yes" << endl;
        } else {
            cout << "No" << endl;
        }
    }
    return 0;
}