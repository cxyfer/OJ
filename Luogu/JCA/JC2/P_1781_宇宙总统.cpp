#include <bits/stdc++.h>
using namespace std;
#define endl '\n'

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    int n;
    cin >> n;
    string mx, s;
    int idx = -1;
    for (int i = 1; i <= n; ++i) {
        cin >> s;
        if (s.size() > mx.size() || (s.size() == mx.size() && s > mx)) {
            mx = s;
            idx = i;
        }
    }
    cout << idx << endl << mx << endl;
    return 0;
}