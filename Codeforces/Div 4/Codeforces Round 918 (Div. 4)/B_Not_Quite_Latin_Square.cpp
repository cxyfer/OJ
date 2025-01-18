#include <bits/stdc++.h>
using namespace std;
using LL = long long;
#define endl '\n'
const int INF = 0x3f3f3f3f;
const int MOD = 1e9 + 7;
const int N = 100005;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);
    int t;
    cin >> t;
    while (t--) {
        bool flag;
        char ch;
        int cnt_row[3];
        char ans;
        for (int i = 0; i < 3; ++i) {
            flag = false;
            for (int j = 0; j < 3; ++j) cnt_row[j] = 0;

            for (int j = 0; j < 3; ++j) {
                cin >> ch;
                if (ch == 'A') {
                    cnt_row[0]++;
                }
                else if (ch == 'B') {
                    cnt_row[1]++;
                }
                else if (ch == 'C') {
                    cnt_row[2]++;
                }
                else {
                    flag = true;
                }
            }
            if (flag){
                if (cnt_row[0] == 0) {
                    ans = 'A';
                }
                else if (cnt_row[1] == 0) {
                    ans = 'B';
                }
                else if (cnt_row[2] == 0) {
                    ans = 'C';
                }
            }
        }
        cout << ans << endl;
    }
    return 0;
}