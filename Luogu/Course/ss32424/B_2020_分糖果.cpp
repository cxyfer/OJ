#include <bits/stdc++.h>
using namespace std;
const int N = 5;
#define endl '\n'

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    vector<int> A(N);
    for (auto & x : A) cin >> x;
    int ans = 0;
    for (int i = 0; i < N; ++i) {
        int x = A[i] / 3;
        ans += A[i] % 3;
        A[(i + 1) % N] += x;
        A[(i - 1 + N) % N] += x;
        A[i] = x;
    }
    for (int i = 0; i < N; ++i) cout << A[i] << " \n"[i == N - 1];
    cout << ans << endl;
    return 0;
}