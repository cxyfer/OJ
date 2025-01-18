#include <bits/stdc++.h>
using namespace std;
#define endl '\n'

string s, path;
vector<int> cnt(26, 0);
vector<string> ans;

void dfs(int i){
    if (i == s.size()) {
        ans.push_back(path);
        return;
    }
    for (int j = 0; j < 26; j++) {
        if (cnt[j] > 0) {
            cnt[j]--;
            path.push_back(j + 'a');
            dfs(i + 1);
            path.pop_back();
            cnt[j]++;
        }
    }

}
int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    cin >> s;
    for (char ch : s) {
        cnt[ch - 'a']++;
    }
    dfs(0);
    cout << ans.size() << endl;
    for (string cur : ans) {
        cout << cur << endl;
    }

    return 0;
}