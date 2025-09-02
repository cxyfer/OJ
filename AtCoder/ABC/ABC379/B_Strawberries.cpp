#include <bits/stdc++.h>
using namespace std;
#define endl '\n'

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    int n, k;
    cin >> n >> k;
    string s;
    cin >> s;
    int ans = 0, i = 0, j = 0;
    while (i < n) {
        j = i;
        while (j < n && s[j] == 'O') {
            j++;
        }
        ans += (j - i) / k;
        i = j + 1;
    }
    cout << ans << endl;
    return 0;
}