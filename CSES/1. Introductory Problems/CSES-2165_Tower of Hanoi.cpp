#include <bits/stdc++.h>
using namespace std;
#define endl '\n'

void f(int n, int a, int b, int c) { 
    if (n == 1) {
        cout << a << ' ' << c << endl;
    } else {
        f(n - 1, a, c, b);
        cout << a << ' ' << c << endl;
        f(n - 1, b, a, c);
    }
}

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    int n; cin >> n;
    cout << (1 << n) - 1 << endl;
    f(n, 1, 2, 3);
    return 0;
}