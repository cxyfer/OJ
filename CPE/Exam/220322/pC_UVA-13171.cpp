/* UVA-13171: Pixel Art
    模擬(Simulation)
    已於 UVA, CPE, ZeroJudge 測試通過
*/
#include <bits/stdc++.h>
using namespace std;
#define endl '\n'

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    int t;
    cin >> t;
    while (t--) {
        int m, y, c;
        string s;
        cin >> m >> y >> c >> s;
        bool flag = true;
        for (char ch : s) {
            if (ch == 'M') {
                m -= 1;
            } else if (ch == 'Y') {
                y -= 1;
            } else if (ch == 'C') {
                c -= 1;
            } else if (ch == 'R') {
                m -= 1;
                y -= 1;
            } else if (ch == 'V') {
                m -= 1;
                c -= 1;
            } else if (ch == 'G') {
                y -= 1;
                c -= 1;
            } else if (ch == 'B') {
                m -= 1;
                y -= 1;
                c -= 1;
            }
            if (m < 0 || y < 0 || c < 0) {
                flag = false;
                break;
            }
        }
        if (flag) {
            cout << "YES " << m << " " << y << " " << c << endl;
        } else {
            cout << "NO" << endl;
        }   
    }
    return 0;
}