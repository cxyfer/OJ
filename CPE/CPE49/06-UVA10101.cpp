#include <bits/stdc++.h>
using namespace std;
using LL = long long;
const int kuti = 1e7;
const int lakh = 1e5;
const int hajar = 1e3;
const int shata = 1e2;
#define endl '\n'

void bangla(LL n){
    if (n >= kuti) {
        bangla(n / kuti); // recursive
        cout << " kuti";
        n %= kuti;
    }
    if (n >= lakh) {
        cout << " " << n / lakh;
        cout << " lakh";
        n %= lakh;
    }
    if (n >= hajar) {
        cout << " " << n / hajar;
        cout << " hajar";
        n %= hajar;
    }
    if (n >= shata) {
        cout << " " << n / shata;
        cout << " shata";
        n %= shata;
    }
    if (n) cout << " " << n;
    return;
}

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    int tc = 1;
    LL n;
    while (cin >> n) {
        cout << setw(4) << tc++ << ".";
        if (n) bangla(n);
        else cout << " 0";
        cout << endl;
    }
    return 0;
}