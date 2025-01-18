/*
    Half Enumeration / Meet in the Middle
    分成兩半，用 bit mask 來枚舉所有可能的子集和，
    並用 dict 來記錄每個子集和出現的次數，最後再將兩邊的 dict 進行配對，計算答案。
    這樣的做法可以將時間複雜度降到 O(2^(n/2))，適用於 n <= 40 的情況。
    Python 會 TLE ，必需用 C++ 才能 AC 。
*/

#include <bits/stdc++.h>
using namespace std;
using LL = long long;
const int N = 45;
#define endl '\n'

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    int n, target, arr[N];
    while (cin >> n >> target) {
        for (int i = 0; i < n; i++) cin >> arr[i];
        if (n == 1) {
            cout << (arr[0] == target) << endl;
            continue;
        }
        int n1 = n / 2, n2 = n - n / 2;
        map<LL, int> cnt1, cnt2;
        for (int i = 1; i < (1 << n1); i++) {
            LL s = 0;
            for (int j = 0; j < n1; j++) {
                if (i & (1 << j)) {
                    s += arr[j];
                }
            }
            cnt1[s]++;
        }
        for (int i = 1; i < (1 << n2); i++) {
            LL s = 0;
            for (int j = 0; j < n2; j++) {
                if (i & (1 << j)) {
                    s += arr[n1 + j];
                }
            }
            cnt2[s]++;
        }
        LL ans = 0;
        for (auto k: cnt1) {
            if (cnt2.count(target - k.first)) {
                ans += (LL) k.second * cnt2[target - k.first];
            }
        }
        ans += cnt1[target] + cnt2[target]; // consider only one side
        cout << ans << endl;
    }
    return 0;
}