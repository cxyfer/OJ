/*
    Meet in the Middle
*/
// from collections import defaultdict

// n, x = map(int, input().split())
// A = list(map(int, input().split()))

// A.sort()

// n1, n2 = n // 2, n - n // 2
// cnt1 = defaultdict(int)
// for i in range(1, 1 << n1):
//     s = 0
//     for j in range(n1):
//         if i & (1 << j):
//             s += A[j]
//     cnt1[s] += 1

// cnt2 = defaultdict(int)
// for i in range(1, 1 << n2):
//     s = 0
//     for j in range(n2):
//         if i & (1 << j):
//             s += A[n1 + j]
//     cnt2[s] += 1

// # 計算兩邊的組合數
// ans = 0
// for k, v in cnt1.items():
//     ans += v * cnt2[x - k]
// ans += cnt1[x] + cnt2[x] # 只選一邊的組合數
// print(ans)

#include <bits/stdc++.h>
using namespace std;
using LL = long long;
#define endl '\n'

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    int n, x;
    cin >> n >> x;
    vector<int> A(n);
    for (int i = 0; i < n; i++) cin >> A[i];
    sort(A.begin(), A.end());
    // 分成兩半，統計兩邊的子集和
    int n1 = n / 2, n2 = n - n / 2;
    unordered_map<LL, int> cnt;
    for (int i = 1; i < (1 << n1); i++) {
        LL s = 0;
        for (int j = 0; j < n1; j++) {
            if (i & (1 << j)) s += A[j];
        }
        cnt[s]++;
    }
    LL ans = 0;
    for (int i = 1; i < (1 << n2); i++) {
        LL s = 0;
        for (int j = 0; j < n2; j++) {
            if (i & (1 << j)) s += A[n1 + j];
        }
        if (cnt.find(x - s) != cnt.end()) ans += cnt[x - s];
    }
    cout << ans << endl;
    return 0;
}