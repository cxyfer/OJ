/*
 * P2098 [USACO16DEC] Team Building P
 * https://www.luogu.com.cn/problem/P2098
 */
#include <bits/stdc++.h>
using namespace std;
using i64 = int64_t;
const int MOD = 1e9 + 9;
#define endl '\n'

void solve1() {
    int N, M, K;
    cin >> N >> M >> K;
    vector<int> A(N), B(M);
    for (int i = 0; i < N; i++) cin >> A[i];
    for (int i = 0; i < M; i++) cin >> B[i];
    sort(A.begin(), A.end());
    sort(B.begin(), B.end());

    vector<vector<vector<i64>>> memo(N + 1, vector<vector<i64>>(M + 1, vector<i64>(K + 1, -1)));
    auto dfs = [&](this auto&& dfs, int i, int j, int k) -> i64 {
        if (k == 0) return 1;
        if (i < 0 || j < 0) return 0;
        i64& res = memo[i][j][k];
        if (res != -1) return res;
        res = (dfs(i - 1, j, k) + dfs(i, j - 1, k) - dfs(i - 1, j - 1, k) + MOD) % MOD;
        if (A[i] > B[j]) res = (res + dfs(i - 1, j - 1, k - 1)) % MOD;
        return res;
    };
    cout << dfs(N - 1, M - 1, K) << endl;
    return;
}

void solve2() {
    int N, M, K;
    cin >> N >> M >> K;
    vector<int> A(N), B(M);
    for (int i = 0; i < N; i++) cin >> A[i];
    for (int i = 0; i < M; i++) cin >> B[i];
    sort(A.begin(), A.end());
    sort(B.begin(), B.end());

    vector<vector<vector<i64>>> f(N + 1, vector<vector<i64>>(M + 1, vector<i64>(K + 1, 0)));
    for (int i = 0; i <= N; i++)
        for (int j = 0; j <= M; j++)
            f[i][j][0] = 1;
    for (int i = 1; i <= N; i++) {
        for (int j = 1; j <= M; j++) {
            for (int k = 1; k <= K; k++) {
                f[i][j][k] = (f[i - 1][j][k] + f[i][j - 1][k] - f[i - 1][j - 1][k] + MOD) % MOD;
                if (A[i - 1] > B[j - 1]) f[i][j][k] = (f[i][j][k] + f[i - 1][j - 1][k - 1]) % MOD;
            }
        }
    }
    cout << f[N][M][K] << endl;
    return;
}

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    solve1();
    // solve2();
    return 0;
}