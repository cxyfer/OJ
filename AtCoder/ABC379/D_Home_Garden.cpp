/*
維護一個變數 tot 表示總經過時間，
則操作 2 中只需將 tot 加上 T 即可，不用真的改變每棵植物的生長時間：
而在操作 1 中，則是紀錄植物的種植時間到 plants 中。

在操作 3 中，我們需要找到有多少還沒被收割的植物高度 >= H。
因此可以維護一個變數 idx 表示第一個還沒被收割的植物下標，
每次操作 3 時，不斷檢查 plants[idx] + tot - H 是否 >= 0，
如果 >= 0 則將 idx 右移，直到不滿足條件為止，則移動的次數即為答案。

也可以用 queue 來維護 plants，思路相同。
此外，由於 plants 是單調遞增的，因此也可以用二分搜尋來找到第一個滿足條件的植物下標。
*/
#include <bits/stdc++.h>
using namespace std;
using LL = long long;
#define endl '\n'

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    int Q, T, H; cin >> Q;
    char op;
    vector<LL> plants; // 紀錄植物的種植時間
    LL tot = 0; // 總經過時間
    int idx = 0; // 第一個還沒被收割的植物下標
    while (Q--) {
        cin >> op;
        if (op == '1') {
            plants.push_back(tot);
        } else if (op == '2') {
            cin >> T;
            tot += T;
        } else {
            cin >> H;
            int st = idx;
            while (idx < plants.size() && tot - plants[idx] >= H) {
                idx++;
            }
            cout << idx - st << endl;
        }
    }
    return 0;
}