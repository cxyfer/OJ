#include <bits/stdc++.h>
using namespace std;
#define endl '\n'

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    int t;
    string s;
    cin >> t;
    while (t--) {
        cin >> s;
        int n = s.size();
        queue<pair<int, int>> q;
        for (int i = 0; i < n - 1; i++) {
            q.emplace(i, i + 1);
        }
        while (!q.empty()) {
            auto [i, j] = q.front();
            q.pop();
            if (j >= n || s[j] == '0') continue;
            int t = s[j] - '1';
            if (t <= s[i] - '0') continue;
            s[j] = t + '0';
            swap(s[i], s[j]);
            if (i - 1 >= 0) q.emplace(i - 1, i);
            if (j + 1 < n) q.emplace(j, j + 1);
        }
        cout << s << endl;
    }
    return 0;
}