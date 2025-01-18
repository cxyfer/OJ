#include <bits/stdc++.h>
using namespace std;
#define endl '\n'

int n;
vector<int> ans;

void dfs(int s, int cur) {
    if (cur * n > 98765) return; // 剪枝
    if (__builtin_popcount(s) == 5) {
        int x = n * cur;
        for (int j = 0; j < 5; j++) {
            int k = x % 10;
            if (s & (1 << k)) return;
            x /= 10;
            s |= 1 << k;
        }
        ans.push_back(cur);
        return;
    }
    for (int j = 0; j < 10; j++) {
        if (s & (1 << j)) continue;
        dfs(s | (1 << j), cur * 10 + j);
    }
}

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    int kase = 0;
    while (cin >> n && n) {
        if (kase++ > 0) cout << endl;
        ans.clear();
        dfs(0, 0);
        if (ans.empty()) {
            cout << "There are no solutions for " << n << "." << endl;
        }
        else {
            for (int x : ans) {
                cout << x * n << " / " << setw(5) << setfill('0') << x << " = " << n << endl;
            }
        }
    }
    return 0;
}