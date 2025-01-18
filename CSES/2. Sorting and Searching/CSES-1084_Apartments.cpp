#include <bits/stdc++.h>
using namespace std;
using LL = long long;
const int INF = 0x3f3f3f3f;
const int MOD = 1e9 + 7;
const int N = 100005;
#define endl '\n'

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    int n, m, k;
    cin >> n >> m >> k;
    vector<int> arr(n), brr(m);
    for (int i = 0; i < n; i++) cin >> arr[i];
    for (int i = 0; i < m; i++) cin >> brr[i];
    sort(arr.begin(), arr.end());
    sort(brr.begin(), brr.end());
    int ans = 0;
    int i = 0, j = 0;
    while (i < n && j < m) {
        if (arr[i] + k < brr[j]) i++;
        else if (arr[i] - k > brr[j]) j++;
        else i++, j++, ans++;
    }
    cout << ans << endl;
    return 0;
}