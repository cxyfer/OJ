#include <bits/stdc++.h>
using uint = unsigned int;
using namespace std;
#define endl '\n'

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    uint n;
    while (cin >> n && n) {
        uint sqrt_n = sqrt(n);
        cout << (sqrt_n * sqrt_n == n ? "yes" : "no") << endl;
    }
    return 0;
}