#include <bits/stdc++.h>
using namespace std;
#define endl '\n'

int gcd(int a, int b) {
    return b == 0 ? a : gcd(b, a % b);
}

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    int n, ans;
    while (cin >> n && n) {
        ans = 0;
        for (int i=1; i<n; i++){
            for (int j=i+1; j<=n; j++){
                ans += gcd(i, j); // or use __gcd(i, j) in <algorithm>
            }
        }
        cout << ans << endl;
    }
    return 0;
}