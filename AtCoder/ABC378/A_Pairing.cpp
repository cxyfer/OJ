#include <bits/stdc++.h>
using namespace std;
const int N = 4;
#define endl '\n'

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    vector<int> A(N), cnt(N + 1);
    for (int i = 0; i < N; i++) {
        cin >> A[i];
        cnt[A[i]]++;
    }
    int ans = 0;
    for (auto &x : cnt) {
        ans += x / 2;
    }
    cout << ans << endl;
    return 0;
}