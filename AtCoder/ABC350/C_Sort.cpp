#include <bits/stdc++.h>
using namespace std;
#define endl '\n'

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    int n; cin >> n;
    vector<int> A(n);
    map<int, int> mp;
    for (int i = 0; i < n; i++) {
        cin >> A[i];
        mp[A[i]] = i;
    }

    int cnt = 0;
    vector<pair<int, int>> ans;
    for (int i = 0; i < n; i++) {
        if (A[i] == i+1) {
            continue;
        }
        cnt++;
        int idx = mp[i+1];
        swap(A[i], A[idx]);
        mp[A[idx]] = idx;
        ans.push_back({i+1, idx+1});
    }
    cout << cnt << endl;
    for (auto &x: ans){
        cout << x.first << " " << x.second << endl;
    }
    return 0;
}