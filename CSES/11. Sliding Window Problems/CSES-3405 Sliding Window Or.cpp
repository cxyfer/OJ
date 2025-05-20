#include <bits/stdc++.h>
using namespace std;
using LL = long long;
#define endl '\n'

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    int n, k; cin >> n >> k;
    LL x, a, b, c; cin >> x >> a >> b >> c;

    // 生成完整的數列
    vector<int> A(n);
    A[0] = x;
    for(int i = 1; i < n; i++)
        A[i] = (a * A[i - 1] + b) % c;

    // 分段計算 Suffix OR
    vector<int> suf(n);
    for(int i = n - 1; i >= 0; i--){
        if (i == n - 1 || (i + 1) % k == 0)
            suf[i] = A[i];
        else
            suf[i] = A[i] | suf[i + 1];
    }

    // 分段計算 Prefix OR 並用 pre 和 suf 計算出答案
    int ans = 0, pre = 0;
    for(int i = 0; i < n; i++){
        // 分段計算 Prefix OR
        if (i % k == 0) pre = A[i];
        else pre |= A[i];
        // 更新答案
        if (i >= k - 1)
            ans ^= (pre | suf[i - k + 1]);
    }
    cout << ans << "\n";
    return 0;
}