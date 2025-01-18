#include <bits/stdc++.h>
using namespace std;
using LL = long long;
const int INF = 0x3f3f3f3f;
const int MOD = 1e9 + 7;
const int N = 100005;
#define endl '\n'

int n, L, cnt;
string C, ans, path;

bool check(const string& path) {
    for (int k = 1; k <= path.size() / 2; ++k) {
        if (path.substr(path.size() - k) == path.substr(path.size() - 2 * k, k)) return false;
    }
    return true;
}

void dfs(int i) {
    if (cnt == n) {
        ans = path;
        return;
    }
    for (char ch : C) {
        path += ch;
        if (check(path)) {
            ++cnt;
            dfs(i + 1);
            if (cnt == n) return;
        }
        path.pop_back();
    }
}

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    while (cin >> n >> L && (n || L)) {
        C.clear();
        for (int i = 0; i < L; ++i) C += 'A' + i;
        cnt = 0;
        path.clear(), ans.clear();
        dfs(0);
        for (int i = 0; i < ans.size(); ++i) {
            cout << ans[i];
            if (ans.size() > 64 && (i + 1) % 64 == 0) cout << endl;
            else if (i + 1 < ans.size() && (i + 1) % 4 == 0) cout << " ";
        }
        cout << endl << ans.size() << endl;
    }
    return 0;
}