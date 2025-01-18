#include <bits/stdc++.h>
using namespace std;
#define endl '\n'

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    int x, y;
    while (cin >> x >> y) {
        vector<int> ans;
        while (y) {
            ans.push_back(x / y);
            x %= y;
            swap(x, y);
        }
        cout << "[" << ans[0];
        if (ans.size() > 1) {
            cout << ";";
            for (int i = 1; i < ans.size(); ++i) {
                cout << ans[i];
                if (i < ans.size() - 1) cout << ",";
            }
        }
        cout << "]" << endl;
    }
    return 0;
}