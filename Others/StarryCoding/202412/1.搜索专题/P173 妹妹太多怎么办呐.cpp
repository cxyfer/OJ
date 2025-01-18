#include <bits/stdc++.h>
using namespace std;
using LL = long long;
const LL INF = 0x3f3f3f3f3f3f3f3f;
#define endl '\n'

struct Node {
    LL x, y, w;
};

LL dist(Node a, LL x, LL y) {
    return abs(a.x - x) + abs(a.y - y);
}

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    int t, n, k;
    cin >> t;
    while (t--) {
        cin >> n >> k;
        vector<Node> A(n);
        for (int i = 0; i < n; i++) cin >> A[i].x >> A[i].y >> A[i].w;
        auto dfs = [&](auto &&dfs, int i, LL x, LL y) -> LL {
            if (__builtin_popcount(i) == k) {
                return 0;
            }
            LL res = LLONG_MIN;
            for (int j = 0; j < n; j++) {
                if (i & (1 << j)) continue;
                res = max(res, A[j].w - dist(A[j], x, y) + dfs(dfs, i | (1 << j), A[j].x, A[j].y));
            }
            return res;
        };
        cout << dfs(dfs, 0, 0, 0) << endl;
    }
    return 0;
}