/* UVA 11175 - From D to E and Back
    Python 會 TLE

    對圖E中的點對 (i, j)
    若存在一個點 k1，使得 i 和 j 都能到達 k1，
    但是又同時存在一個點 k2，使得 i 和 j 只有其中一個能到達 k2，
    則 (i, j) 是一個不可逆的點對。
     
    https://blog.csdn.net/Inuyasha__/article/details/103384599
    https://home.gamer.com.tw/creationDetail.php?sn=3800895
    https://web.ntnu.edu.tw/~algo/Graph2.html
*/
#include <bits/stdc++.h>
using namespace std;
const int N = 350;
#define endl '\n'

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    int t, kase=1, m, k, g[N][N], u, v;
    cin >> t;
    while (t--) {
        cin >> m >> k;
        memset(g, 0, sizeof(g));
        for (int i = 0; i < k; ++i) {
            cin >> u >> v;
            g[u][v] = 1;
        }
        bool flag = false;
        for (int i = 0; i < m && !flag; ++i) {
            for (int j = 0; j < m && !flag; ++j) {
                bool ck1 = false, ck2 = false;
                for (int k = 0; k < m && !flag; ++k) {
                    if (g[i][k] && g[j][k]) ck1 = true; // i 和 j 都能到達 k
                    if (g[i][k] != g[j][k]) ck2 = true; // i 和 j 只有其中一個能到達 k
                }
                if (ck1 && ck2) flag = true;
            }
        }
        cout << "Case #" << kase++ << ": " << (flag ? "No" : "Yes") << endl;
    }
    return 0;
}