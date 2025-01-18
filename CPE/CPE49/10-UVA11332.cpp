#include <bits/stdc++.h>
using namespace std;
using LL = long long;
#define endl '\n'

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    LL n;
    while (cin >> n && n) {
        while (n >= 10) {
            LL tmp = 0;
            while (n) {
                tmp += n % 10;
                n /= 10;
            }
            n = tmp;
        }
        cout << n << endl;
    }
    return 0;
}