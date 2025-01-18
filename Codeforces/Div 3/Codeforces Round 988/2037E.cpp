#include <bits/stdc++.h>
using namespace std;
#define endl '\n'

int query(int l, int r) {
    cout << "? " << l << " " << r << endl;
    cout.flush();
    int res;
    cin >> res;
    return res;
}

void answer(const string& ans) {
    cout << "! " << ans << endl;
    cout.flush();
}

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    int t, n;
    cin >> t;
    while (t--) {
        cin >> n;

        vector<int> f(n + 2, 0), d(n + 1, 0);
        vector<char> s(n + 1);

        for (int i = 1; i < n; i++) {
            f[i] = query(i, n);
        }

        for (int i = 1; i <= n; i++) {
            d[i] = f[i] - f[i + 1];
        }

        bool ambiguous = false, found = false;
        string result;
        function<void(int, int)> dfs = [&](int i, int cnt) {
            if (found || ambiguous) return;
            if (i == 0) {
                found = true;
                result = string(s.begin() + 1, s.end());
                return;
            }
            if (d[i] < 0) return;
            if (d[i] > 0) {
                if (d[i] != cnt) return;
                s[i] = '0';
                dfs(i - 1, cnt);
            } else {
                int count = 0;
                s[i] = '0';
                dfs(i - 1, cnt);
                if (found) count++;
                found = false;

                s[i] = '1';
                dfs(i - 1, cnt + 1);
                if (found) count++;

                if (count == 0) return;
                if (count > 1) {
                    ambiguous = true;
                    return;
                }
            }
        };
        dfs(n, 0);

        if (!found || ambiguous) {
            answer("IMPOSSIBLE");
        } else {
            answer(result);
        }
    }
    return 0;
}
