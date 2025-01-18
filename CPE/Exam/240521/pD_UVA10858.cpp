#include <bits/stdc++.h>
using namespace std;
#define endl '\n'

vector<vector<int>> ans;
vector<int> path;

void dfs(int x) {
    if (x == 1 && path.size() > 1) {
        ans.push_back(path);
        return;
    }
    int pre = path.empty() ? 2 : path.back();
    for (int y = pre; y <= x; y++) {
        if (x % y == 0) {
            path.push_back(y);
            dfs(x / y);
            path.pop_back();
        }
    }
}

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    int n;
    while (cin >> n && n) {
        ans.clear();
        dfs(n);
        cout << ans.size() << endl;
        for (auto a : ans)
            for (int i = 0; i < a.size(); i++)
                cout << a[i] << (i == a.size() - 1 ? endl : ' ');
    }
    return 0;
}