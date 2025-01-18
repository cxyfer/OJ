#include <bits/stdc++.h>
using namespace std;
#define endl '\n'

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    string s;
    cin >> s;
    vector<int> cnt(10, 0);
    for (auto &ch : s) cnt[ch - '0']++;
    cout << ((cnt[1] == 1 && cnt[2] == 2 && cnt[3] == 3) ? "Yes" : "No") << endl; 
    return 0;
}