#include <bits/stdc++.h>
using namespace std;
#define endl '\n'

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    int k;
    while (cin >> k) {
        vector<pair<int, int>> ans;
        for (int y = k + 1; y <= 2 * k; y++) {
            int num = y * k;
            int den = y - k;
            if (num % den != 0) continue;
            int x = num / den;
            if (x >= y) ans.push_back({x, y});
        }
        cout << ans.size() << endl;
        for (auto &p : ans) {
            cout << "1/" << k << " = 1/" << p.first << " + 1/" << p.second << endl;
        }
    }
    return 0;
}