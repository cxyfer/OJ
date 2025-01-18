#include <bits/stdc++.h>
using namespace std;
const int N = 1e6 + 5;
#define endl '\n'

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    int t, n;

    vector<int> cnt(N), ans(N);
    for (int i = 1; i < N; i++)
        for (int j = i; j < N; j += i)
            cnt[j]++;

    for (int i = 1; i < N; i++)
        ans[i] = (cnt[ans[i - 1]] <= cnt[i]) ? i : ans[i - 1];

    cin >> t;
    while (t--) {
        cin >> n;
        cout << ans[n] << endl;
    }
    return 0;
}