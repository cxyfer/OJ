#include <bits/stdc++.h>
using namespace std;
#define endl '\n'

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    int n, k;
    cin >> n >> k;
    string s;
    cin >> s;
    vector<pair<int, int>> blocks;
    for (int i = 0, st; i < n; i++) {
        if (s[i] == '1') {
            st = i;
            while (i < n && s[i] == '1') i++;
            blocks.push_back({st, i - 1});
        }
    }
    int r_prev = blocks[k - 2].second;
    int l = blocks[k - 1].first, r = blocks[k - 1].second;
    string ans = "";
    ans += s.substr(0, r_prev + 1);
    ans += s.substr(l, r + 1 - l);
    ans += s.substr(r_prev + 1, l - r_prev - 1);
    ans += s.substr(r + 1);
    cout << ans << endl;
    return 0;
}