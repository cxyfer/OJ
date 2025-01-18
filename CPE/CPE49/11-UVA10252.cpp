#include <bits/stdc++.h>
using namespace std;
const int N = 26;
#define endl '\n'

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    string a, b;
    int tc = 1;
    int cnt_a[N], cnt_b[N];
    while (getline(cin, a) && getline(cin, b)) {
        string ans = "";
        memset(cnt_a, 0, sizeof(cnt_a));
        memset(cnt_b, 0, sizeof(cnt_b));
        for (char ch: a) cnt_a[ch - 'a']++;
        for (char ch: b) cnt_b[ch - 'a']++;
        for (int i = 0; i < N; i++) {
            int mn = min(cnt_a[i], cnt_b[i]);
            while (mn--) ans += (char)(i + 'a'); // 字串相加要一個一個加
        }
        cout << ans << endl;  
    }
    return 0;
}