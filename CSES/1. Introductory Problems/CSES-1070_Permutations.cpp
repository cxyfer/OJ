#include <bits/stdc++.h>
using namespace std;
#define endl '\n'

int main(){
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    int n; cin >> n;
    vector<int> ans;
    if (n == 2 or n == 3) {
        cout << "NO SOLUTION" << endl;
    }
    else {
        for (int i = 2; i <= n; i += 2) {
            ans.push_back(i);
        }
        for (int i = 1; i <= n; i += 2) {
            ans.push_back(i);
        }
        for (int i = 0; i < n; i++) {
            cout << ans[i] << (i == n - 1 ? endl : ' ');
        }
    }
    return 0;
}