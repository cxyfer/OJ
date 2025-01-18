/*
    預處理出每個數字的Digit Generator
    tags: 預處理, 紫書-Ch3, CPE-190326
*/
#include <bits/stdc++.h>
using namespace std;
using LL = long long;
const int N = 1e5 + 5;
#define endl '\n'

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    int t, n;
    cin >> t;
    int ans[N] = {0};
    for (int x = 1; x < N; x++) {
        int tmp = x, y = x;
        while (tmp) {
            y += tmp % 10;
            tmp /= 10;
        }
        if (y < N && ans[y] == 0) {
            ans[y] = x;
        }
    }
    while (t--) {
        cin >> n;
        cout << ans[n] << endl;
    }
    return 0;
}