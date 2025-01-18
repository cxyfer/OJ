#include <bits/stdc++.h>
using namespace std;
#define endl '\n'

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    int t, n;
    cin >> t;
    while (t--) {
        cin >> n;
        vector<int> p(n);
        for (int i = 0; i < n; i++) {
            cin >> p[i];
            p[i]--;
        }
        vector<bool> visited(n, false);
        int ans = 0;
        for (int i = 0; i < n; i++) {
            if (visited[i]) continue;
            int cur = i;
            int length = 0;
            while (!visited[cur]) {
                visited[cur] = true;
                cur = p[cur];
                length++;
            }
            if (length >= 3) {
                ans += (length - 1) / 2;
            }
        }
        cout << ans << endl;
    }
    return 0;
}