/*
    AC: UVA, CPE, ZeroJudge
*/
#include <bits/stdc++.h>
using namespace std;
using LL = long long;
const int N = 20;
#define endl '\n'

LL fact[N]; // 預處理 N! 的值

void init() {
    fact[0] = 1;
    for (int i=1; i<N; i++) {
        fact[i] = fact[i-1] * i;
    }
}

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    LL t, n, x, i;
    cin >> t;
    init();
    string s, ans;
    while (t--) {
        cin >> s >> n;
        ans = "";
        sort(s.begin(), s.end());
        while (s.size() > 0) {
            x = fact[s.size()-1];
            i = n / x;
            ans += s[i];
            s.erase(i, 1);
            n %= x;
        }
        cout << ans << endl;
    }
    return 0;
}