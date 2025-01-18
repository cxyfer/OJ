#include <bits/stdc++.h>
using namespace std;
#define endl '\n'

int gcd(int a, int b) {
    return b == 0 ? a : gcd(b, a % b);
}

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    int t, tc=1, a, b;
    string s1, s2;
    cin >> t;
    while (t--) {
        cin >> s1 >> s2;
        a = stoi(s1, 0, 2);
        b = stoi(s2, 0, 2);
        if (__gcd(a, b) == 1) { // std::gcd(a, b) in C++17, or __gcd(a, b) in <algorithm>
            cout << "Pair #" << tc++ << ": Love is not all you need!" << endl;
        } else {
            cout << "Pair #" << tc++ << ": All you need is love!" << endl;
        }
    }
    return 0;
}