#include <bits/stdc++.h>
using namespace std;
const int N = 128;
#define endl '\n'

bool cmp(pair<int, int> a, pair<int, int> b) {
    if (a.second != b.second) return a.second < b.second;
    return a.first > b.first;
}
int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    int tc=0;
    int cnt[N];
    string s;
    while (getline(cin, s)) {
        if (tc++> 0) cout << endl;
        memset(cnt, 0, sizeof(cnt));
        for (auto &ch: s) cnt[ch]++;
        vector<pair<int, int>> v;
        for (int i = 0; i < N; i++) if (cnt[i]) v.emplace_back(i, cnt[i]);
        sort(v.begin(), v.end(), cmp);
        for (auto &p: v) cout << p.first << ' ' << p.second << endl;
    }
    return 0;
}