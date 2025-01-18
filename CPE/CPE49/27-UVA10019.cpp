#include <bits/stdc++.h>
using namespace std;
using LL = long long;
#define endl '\n'

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    int t, M, t1, t2, t3, b1, b2;
    cin >> t;
    while (t--) {
        cin >> M;
        t1 = M; t2 = M;
        b1 = 0; b2 = 0;
        while (t1) {
            b1 += t1 & 1;
            t1 >>= 1;
        }
        while (t2) {
            t3 = t2 % 10;
            while (t3) {
                b2 += t3 & 1;
                t3 >>= 1;
            }
            t2 /= 10;
        }
        // cout << bitset<32>(M).count() << " " << bitset<32>(stoi(to_string(M), nullptr, 16)).count() << endl;
        cout << b1 << " " << b2 << endl;
    }
    return 0;
}