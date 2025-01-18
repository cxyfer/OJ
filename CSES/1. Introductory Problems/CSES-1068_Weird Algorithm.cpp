#include <bits/stdc++.h>
using namespace std;
using LL = long long;
#define endl '\n'

int main() {
    ios::sync_with_stdio(0); cin.tie(0); cout.tie(0);
    LL n;
    cin >> n;
    vector<LL> ans;
    ans.push_back(n);
    while (n != 1) {
        if (n % 2 == 0) n /= 2;
        else n = n * 3 + 1;
        ans.push_back(n);
    }
    for (int i = 0; i < ans.size(); i++) cout << ans[i] << (i == ans.size() - 1 ? "" : " ");
}