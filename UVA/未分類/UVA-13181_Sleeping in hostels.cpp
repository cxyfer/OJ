#include <bits/stdc++.h>
using namespace std;
#define endl '\n'

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    string s;
    while (cin >> s) {
        int n = s.size();
        vector<int> groups;
        int i = 0;
        while (i < n) {
            while (i < n && s[i] == 'X') i++;
            int st = i;
            while (i < n && s[i] == '.') i++;
            groups.push_back(i - st);
            i++;
        }
        int ans = 0;
        for (int g : groups) ans = max(ans, (g - 1) / 2);
        if (s[0] == '.') ans = max(ans, groups[0] - 1);
        if (s[n - 1] == '.') ans = max(ans, groups[groups.size() - 1] - 1);
        cout << ans << endl;
    }
    return 0;
}