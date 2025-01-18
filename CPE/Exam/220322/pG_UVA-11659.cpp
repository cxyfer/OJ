/*
    集合枚舉 + 位運算(Bit Manipulation)
    看到 1 ≤ N ≤ 20，就知道這題是要用集合枚舉 + 位運算

    https://leetcode.cn/circle/discuss/CaOJ45/
*/

#include <bits/stdc++.h>
using namespace std;
const int N = 20;
#define endl '\n'

int bit_count(int x){ // or __builtin_popcount(x)
    int res = 0;
    while (x){
        x &= x - 1; // 清除最低位的 1
        res++;
    }
    return res;
}

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    int n, m, x, y, saya[N], sayb[N];
    while (cin >> n >> m && (n || m)){
        memset(saya, 0, sizeof(saya));
        memset(sayb, 0, sizeof(sayb));
        for (int i = 0; i < m; i++){
            cin >> x >> y;
            if (y > 0) saya[x-1] |= 1 << (y-1);
            else sayb[x-1] |= 1 << (-y-1);
        }
        int ans = 0;
        for (int x = 1; x < (1 << n); x++){
            if (bit_count(x) <= ans) continue; // pruning
            bool flag = true;
            for (int i = 0; i < n; i++){
                if (x & (1 << i)){
                    if ((x & saya[i]) != saya[i] || (x & sayb[i]) != 0){
                        flag = false;
                        break;
                    }
                }
            }
            if (flag) ans = max(ans, bit_count(x)); // update ans
        }
        cout << ans << endl;
    }
    return 0;
}