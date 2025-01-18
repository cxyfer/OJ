#include <bits/stdc++.h>
using namespace std;
#define endl '\n'

bool is_prime(int n) {
    if (n < 2) return false;
    for (int i = 2; i <= sqrt(n); i++) {
        if (n % i == 0) return false;
    }
    return true;
}
int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    int n, m, tmp;
    bool ck1, ck2;
    while (cin >> n) {
        m = 0; tmp = n;
        while (tmp) {
            m = m * 10 + tmp % 10;
            tmp /= 10;
        }
        ck1 = is_prime(n);
        ck2 = is_prime(m);
        if (ck1 && ck2 && n != m) {
            cout << n << " is emirp." << endl;
        } else if (ck1) {
            cout << n << " is prime." << endl;
        } else {
            cout << n << " is not prime." << endl;
        }
    }
    return 0;
}