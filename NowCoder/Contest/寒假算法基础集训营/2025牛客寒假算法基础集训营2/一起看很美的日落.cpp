#include <bits/stdc++.h>
using namespace std;
using LL = long long;
const int MOD = 1e9 + 7;
#define endl '\n'

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    int n, u, v;
    cin >> n;
    vector<int> A(n);
    for (int i = 0; i < n; i++) {
        cin >> A[i];
    }
    vector<vector<int>> g(n);
    for (int i = 0; i < n - 1; i++) {
        cin >> u >> v;
        u--; v--;
        g[u].push_back(v);
        g[v].push_back(u);
    }
    
    LL ans = 0;
    for (int b = 0; b < 31; b++) {
        vector<int> arr(n);
        for (int i = 0; i < n; i++) {
            arr[i] = (A[i] >> b) & 1;
        }

        // f[u][0/1] 表示以節點 u 為根的子樹中，
        // 所有「包含根節點 u」的連通分量中，第 b 位為 0/1 的節點個數總和（不同連通分量各計算一次）
        vector<array<LL, 2>> f(n);
        // s[u] 表示以節點 u 為根的子樹中，所有「包含根節點 u」的連通分量在第 b 位上的權值總和
        vector<LL> s(n);
        // cnt[u] 表示以節點 u 為根的子樹中，包含節點 u 的連通分量數量
        vector<LL> cnt(n);
        auto dfs = [&](auto &&dfs, int u, int fa) -> void {
            f[u][arr[u]] = 1;
            cnt[u] = 1;
            for (int v : g[u]) {
                if (v == fa) continue;
                dfs(dfs, v, u);
                
                // Calculate f0 and f1 (count of 0's and 1's in all paths)
                LL f0 = (f[u][0] + f[u][0] * cnt[v] % MOD + cnt[u] * f[v][0] % MOD) % MOD;
                LL f1 = (f[u][1] + f[u][1] * cnt[v] % MOD + cnt[u] * f[v][1] % MOD) % MOD;
                
                // Update s[u] (count of pairs)
                s[u] = (s[u] * (cnt[v] + 1) % MOD
                        + f[u][0] * f[v][1] % MOD
                        + f[u][1] * f[v][0] % MOD
                        + s[v] * cnt[u] % MOD) % MOD;
                
                // Update cnt[u] (number of solutions with u as LCA)
                cnt[u] = (cnt[u] * (1 + cnt[v])) % MOD;
                
                f[u][0] = f0;
                f[u][1] = f1;
            }
        };
        dfs(dfs, 0, -1);
        
        // Sum up the contribution of this bit
        for (int i = 0; i < n; i++) {
            ans = (ans + s[i] * (1LL << b)) % MOD;
        }
    }
    cout << (ans * 2) % MOD << endl;
    return 0;
}