#include <bits/stdc++.h>
using namespace std;
using LL = long long;
#define endl '\n'

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    int N; cin >> N;
    string S; cin >> S;

    vector<LL> ans(2 * N + 1);
    for (int i = 0; i < N; ++i) {
        int d = S[i] - '0';
        ans[0] += d * (i + 1);
        ans[N - i] -= d * (i + 1);
    }

    for (int i = 1; i <= 2 * N; ++i) {
        ans[i] += ans[i - 1];
    }

    for (int i = 0; i <= 2 * N; ++i) {
        if (ans[i] >= 10) {
            ans[i + 1] += ans[i] / 10;
            ans[i] %= 10;
        }
    }
    bool flag = false;
    for (int i = 2 * N; i >= 0; --i) {
        if (ans[i] != 0) {
            flag = true;
        }
        if (flag) {
            cout << ans[i];
        }
    }
    return 0;
}