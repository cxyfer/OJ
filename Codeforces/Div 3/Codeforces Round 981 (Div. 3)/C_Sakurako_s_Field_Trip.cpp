/*
    DP
    注意到 disturbance 只會發生在相鄰的兩個位置，且只能對對稱的位置進行交換。
    因此可以令 f(i, flag) 表示考慮到第 i 個位置，且前一個位置是否發生過交換的最小 disturbance。
    轉移時分別考慮在第 i 個位置不交換，以及交換的情況。
    由於是對稱的，因此只需要考慮一半即可。
    邊界條件為 i > n / 2，此時若 n 為奇數，則還有兩條邊需要考慮；否則只剩一條邊需要考慮。
*/

#include <bits/stdc++.h>
const int INF = 0x3f3f3f3f;
using namespace std;
#define endl '\n'

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    int t, n;
    cin >> t;
    while (t--) {
        cin >> n;
        vector<int> A(n + 2);
        A[0] = A[n+1] = -INF; // 邊界
        for (int i = 1; i <= n; i++) {
            cin >> A[i];
        }
        vector<vector<int>> memo(2, vector<int>(n + 2, INF));
        auto f = [&](auto &&f, int i, bool flag) -> int {
            if (i > n / 2) {
                if (n & 1) { // 奇數，還有兩條邊需要考慮
                    return int(A[i-1] == A[i]) + int(A[i] == A[i+1]);
                } else { // 偶數，只剩一條邊需要考慮
                    return int(A[i-1] == A[i]);
                }
            }
            int &res = memo[flag][i];
            if (res != INF) return res;
            if (!flag) { // 前一個位置沒有發生過交換
                // 不交換 A[i] 和 A[n - i + 1]
                int res1 = int(A[i-1] == A[i]) + int(A[n-i+1] == A[n-i+2]) + f(f, i+1, false);
                // 交換 A[i] 和 A[n - i + 1]
                int res2 = int(A[i-1] == A[n-i+1]) + int(A[i] == A[n-i+2]) + f(f, i+1, true);
                return res = min(res1, res2);
            } else { // 前一個位置發生過交換
                // 不交換 A[i] 和 A[n - i + 1]
                int res1 = int(A[n-i+1] == A[i]) + int(A[i-1] == A[n-i+2]) + f(f, i+1, false);
                // 交換 A[i] 和 A[n - i + 1]
                int res2 = int(A[n-i+1] == A[n-i+2]) + int(A[i-1] == A[i]) + f(f, i+1, true);
                return res = min(res1, res2);
            }
        };
        cout << f(f, 1, false) << endl;
    }
    return 0;
}
