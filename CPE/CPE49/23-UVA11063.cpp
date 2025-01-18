#include <bits/stdc++.h>
using namespace std;
const int N = 105;
const int M = 2e4 + 5;
#define endl '\n'

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    bool flag;
    int n, kase = 1, arr[N], cnt[M];
    while (cin >> n) {
        for (int i = 0; i < n; i++) cin >> arr[i];
        flag = arr[0] >= 1;
        for (int i = 0; i < n-1; i++) {
            if (arr[i] >= arr[i+1]) {
                flag = false;
                break;
            }
        }
        memset(cnt, 0, sizeof(cnt));
        for (int i = 0; i < n; i++) {
            for (int j = i; j < n; j++) {
                if (cnt[arr[i] + arr[j]] > 0) {
                    flag = false;
                    break;
                }
                cnt[arr[i] + arr[j]]++;
            }
        }
        cout << "Case #" << kase++ << ": It is " << (flag ? "a B2-Sequence." : "not a B2-Sequence.") << endl << endl;
    }
    return 0;
}