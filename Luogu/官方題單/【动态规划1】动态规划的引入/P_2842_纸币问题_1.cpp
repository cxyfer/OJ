#include <bits/stdc++.h>
using namespace std;
const int INF = 0x3f3f3f3f;
#define endl '\n'

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    int n, w;
    cin >> n >> w;
    vector<int> A(n);
    for (int i = 0; i < n; i++) cin >> A[i];
    sort(A.begin(), A.end());

    vector<int> f(w + 1, INF);
    f[0] = 0;
    for (int i = 1; i <= w; i++) {
        for (int a : A) {
            if (i - a < 0) break;
            f[i] = min(f[i], f[i - a] + 1);
        }
    }
    cout << f[w] << endl;

    return 0;
}