#include <bits/stdc++.h>
using namespace std;
#define endl '\n'

int n, kase = 1;

const int MAXN = 16 * 2;
vector<bool> is_prime(MAXN + 1, true);
void sieve() {
    is_prime[0] = is_prime[1] = false;
    for (int i = 2; i * i <= MAXN; i++) {
        if (is_prime[i]) {
            for (int j = i * i; j <= MAXN; j += i) 
                is_prime[j] = false;
        }
    }
}

vector<vector<int>> ans;
vector<int> path;
void dfs(int s) {
    if (s == (1 << n) - 1) {
        if (is_prime[path.back() + path[0]])
            ans.push_back(path);
        return;
    }
    for (int i = 0; i < n; i++) {
        if (s & (1 << i)) continue;
        int x = i + 1;
        if (path.size() && !is_prime[path.back() + x]) continue;
        path.push_back(x);
        dfs(s | (1 << i));
        path.pop_back();
    }
}

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    sieve();
    while (cin >> n) {
        if (kase > 1) cout << endl;
        ans.clear();
        path.clear();
        path.push_back(1);
        dfs(1 << 0);
        cout << "Case " << kase++ << ":" << endl;
        for (auto &p : ans) {
            for (int i = 0; i < n; i++) cout << p[i] << " \n"[i == n - 1];
        }
    }
    return 0;
}