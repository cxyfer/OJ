#include <bits/stdc++.h>
using namespace std;
const int N = 5005;
#define endl '\n'

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    int t, n, arr[N], ans, tmp;
    cin >> t;
    while (t--){
        cin >> n;
        for (int i = 0; i < n; i++) cin >> arr[i];
        ans = 0;
        for (int i = 1; i < n; i++){
            tmp = 0;
            for (int j = 0; j < i; j++){
                if (arr[j] <= arr[i]) tmp++;
            }
            ans += tmp;
        }
        cout << ans << endl;
    }

    return 0;
}