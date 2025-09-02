#include <bits/stdc++.h>
using namespace std;
#define endl '\n'

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    int n, m, l;
    cin >> n >> m >> l;
    vector<int> cards(n + m + l);
    for (int i = 0; i < n + m + l; i++) cin >> cards[i];
    int mask = (1 << (n + m + l)) - 1;
    int a = 0, b = 0;
    for (int i = 0; i < n; i++) a |= (1 << i);
    for (int i = n; i < n + m; i++) b |= (1 << i);

    unordered_map<int, int> memo; // Memoization
    auto f = [&](auto &&f, int a, int b, bool flag) -> bool {
        int key = a << (n + m + l + 1) | b << 1 | flag;
        if (memo.count(key)) return memo[key];

        int cur = flag ? a : b; // 當前輪到某玩家出牌
        if (cur == 0) return false; // 當前玩家沒有牌可打就輸了
        int table = ~(a | b) & mask; // 桌面上的牌是兩個玩家手牌以外的牌
        
        int n_a, n_b, n_table;
        for (int i = 0; i < n + m + l; i++) { // 枚舉要打出的牌
            if (!((cur >> i) & 1)) continue; // 如果當前玩家沒有這張牌則跳過

            if (flag) {
                n_a = a & ~(1 << i);
                n_b = b;
            } else {
                n_a = a;
                n_b = b & ~(1 << i);
            }

            n_table = table | (1 << i); // 桌面上的牌加上剛剛打出的牌
            if (!f(f, n_a, n_b, flag ^ 1)) return memo[key] = true; // 不回收牌
            for (int j = 0; j < n + m + l; j++) {
                if (((n_table >> j) & 1) && (cards[j] < cards[i])) { // 這張牌在桌面上，且比剛剛打出的牌小，可以回收
                    if (flag) {
                        if (!f(f, n_a | (1 << j), n_b, flag ^ 1)) return memo[key] = true;
                    } else {
                        if (!f(f, n_a, n_b | (1 << j), flag ^ 1)) return memo[key] = true;
                    }
                }
            }
        }
        return memo[key] = false;
    };
    cout << (f(f, a, b, 1) ? "Takahashi" : "Aoki") << endl;

    return 0;
}