#include <bits/stdc++.h>
using namespace std;
#define endl '\n'

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    string s;
    cin >> s;
    int n = s.size();
    vector<int> ans;
    int i = 1, st;
    while (i < n) {
        st = i;
        while (i < n && s[i] != '|') i++;
        ans.push_back(i - st);
        i++;
    }
    for (auto &x : ans) cout << x << ' ';
    return 0;
}