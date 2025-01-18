#include <bits/stdc++.h>
using namespace std;
using LL = long long;
const int N = 1e5+10;
#define endl '\n'

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    int arr[N] = {0};
    for (int i = 1; i * i < N; i++) arr[i * i] = 1;
    int pre_sum[N] = {0};
    for (int i = 1; i < N; i++) pre_sum[i] = pre_sum[i - 1] + arr[i];
    int L, R;
    while (cin >> L >> R && (L || R)) {
        cout << pre_sum[R] - pre_sum[L - 1] << endl;
    }
    return 0;
}