/*
首先考慮有解的情況：
假設第 i 個位置的石頭來源是 from_i，則移動的距離為 i - from_i，
總距離為 sum(i - from_i) = sum(i) - sum(from_i)，
其中 sum(i) = n * (n + 1) // 2，
而 sum(from_i) 即原本石頭位置的和，為 sum(X_i * A_i for X_i, A_i in stones)。

接著考慮無解的情況：
- 由於最後石頭的數量必須為 n，因此只要 sum(A) != n 即無解。
- 由於石頭只能往後移動，因此我們可以模擬移動的過程，只要中途數量出現負數即無解。
    - 但如果枚舉每個位置顯然會超時，但我們其實只需要枚舉存在石頭的位置即可。
    - 在這個過程中維護多餘的石頭數量 cur、上一個石頭的位置 last。
*/
#include <bits/stdc++.h>
using namespace std;
using LL = long long;
#define endl '\n'

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    int n, m;
    cin >> n >> m;
    vector<int> X(m), A(m);
    for (int i = 0; i < m; ++i) {
        cin >> X[i];
    }
    for (int i = 0; i < m; ++i) {
        cin >> A[i];
    }
    vector<pair<int, int>> stones(m);
    for (int i = 0; i < m; ++i) {
        stones[i] = {X[i], A[i]};
    }
    sort(stones.begin(), stones.end(), [](const auto &a, const auto &b) {
        return a.first < b.first;
    });
    LL ans = (LL)n * (n + 1) / 2;
    for (auto [pos, val] : stones) {
        ans -= (LL)pos * val;
    }
    if (accumulate(A.begin(), A.end(), 0LL) != (LL) n) ans = -1;
    LL cur = 0, last = 0;
    for (auto [pos, val] : stones) {
        cur -= (pos - (last + 1));
        if (cur < 0) {
            ans = -1;
            break;
        }
        cur += val - 1;
        last = pos;
    }
    cur -= (n - last);
    if (cur != 0) ans = -1;
    cout << ans << endl;
    return 0;
}