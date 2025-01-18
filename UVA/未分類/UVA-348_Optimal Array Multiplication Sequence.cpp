#include <bits/stdc++.h>
using namespace std;
const int INF = 0x3f3f3f3f;
#define endl '\n'

string build(const vector<vector<int>> &s, int i, int j) {
    if (i == j) return "A" + to_string(i);
    int k = s[i][j];
    string left = build(s, i, k);
    string right = build(s, k + 1, j);
    return "(" + left + " x " + right + ")";
}

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    int n, kase = 1, a, b;
    while (cin >> n && n != 0) {
        vector<int> P(n + 1);
        for (int i = 1; i <= n; i++) {
            cin >> a >> b;
            if (i == 1) P[0] = a;
            P[i] = b;
        }
        vector<vector<int>> f(n + 1, vector<int>(n + 1, INF));
        vector<vector<int>> s(n + 1, vector<int>(n + 1, 0));
        for (int i = 1; i <= n; i++) f[i][i] = 0;
        for (int ln = 2; ln <= n; ln++) {
            for (int i = 1; i <= n - ln + 1; i++) {
                int j = i + ln - 1;
                for (int k = i; k < j; k++) {
                    int t = f[i][k] + f[k + 1][j] + P[i - 1] * P[k] * P[j];
                    if (t < f[i][j]) {
                        f[i][j] = t;
                        s[i][j] = k;
                    }
                }
            }
        }
        string ans = build(s, 1, n);
        cout << "Case " << kase++ << ": " << ans << endl;
    }
    return 0;
}