#include <bits/stdc++.h>
using namespace std;
using LL = long long;
#define endl '\n'

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    LL x, y;
    while (cin >> x >> y) {
        cout << abs(x - y) << endl;
    }
    return 0;
}