#include <bits/stdc++.h>
#define ll long long
#define INF 0x3f3f3f3f
using namespace std;

int N = 10000;

int rotate(int A[]) {
    int res = INF;
    for (int k = 0; k < N; ++k) {
        bool flag = true;
        for (int i = 0; i < N - 1; ++i) {
            if (A[(i - k + N) % N] > A[(i - k + 1 + N) % N]) {
                flag = false;
                break;
            }
        }
        if (flag) {
            res = min(res, k);
            break;
        }
    }
    for (int k = 0; k < N; ++k) {
        bool flag = true;
        for (int i = 0; i < N - 1; ++i) {
            if (A[(i - k + N) % N] < A[(i - k + 1 + N) % N]) {
                flag = false;
                break;
            }
        }
        if (flag) {
            res = min(res, k + 1);
            break;
        }
    }
    return res;
}

int main() {
    int T;
    cin >> T;
    for (int tc = 1; tc <= T; ++tc) {
        cin >> N;
        int A[N];
        for (int i = 0; i < N; ++i) {
            cin >> A[i];
        }
        if (N == 1) {
            cout << 0 << endl;
            continue;
        }
        int ans = INF;
        int res1 = rotate(A);
        ans = min(ans, res1);

        reverse(A, A + N);
        int res2 = rotate(A) + 1;
        ans = min(ans, res2);
        if (ans == INF) {
            cout << -1 << endl;
        } else {
            cout << ans << endl;
        }
    }
    return 0;
}