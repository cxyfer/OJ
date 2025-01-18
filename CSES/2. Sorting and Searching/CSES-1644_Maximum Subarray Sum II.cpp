#include <bits/stdc++.h>
using namespace std;
using LL = long long;
#define endl '\n'

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    int n, a, b;
    cin >> n >> a >> b;
    vector<int> X(n);
    for (int i = 0; i < n; i++) cin >> X[i];
    vector<LL> s(n + 1);
    for (int i = 0; i < n; i++) s[i + 1] = s[i] + X[i];
    priority_queue<pair<LL, int>, vector<pair<LL, int>>, greater<pair<LL, int>>> hp;
    LL ans = LLONG_MIN;
    for (int i = 0; i <= n; i++) {
        while (!hp.empty() && hp.top().second < i - b) hp.pop();
        if (i >= a) hp.push({s[i - a], i - a});
        if (!hp.empty()) ans = max(ans, s[i] - hp.top().first);
    }
    cout << ans << endl;
    return 0;
}