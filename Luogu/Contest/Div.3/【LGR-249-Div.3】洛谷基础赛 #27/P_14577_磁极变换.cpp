/*
P14577 磁极变换
https://www.luogu.com.cn/problem/P14577

很卡常的題目，要用快讀快寫，另外為了避免 cache miss，也需要考慮二維陣列的維度安排。

對於每種字母 c 來說，顯然只有區間內有奇數個該字母，才有可能剩下。
並且這個最後一個該字母的位置 lst，不能被其他字母 c2 橫跨，
具體來說，當左側 [l, lst - 1] 有奇數個其他字母 c2，且右側 [lst, r] 有該字母 c2 時，不合法。
注意上述判斷條件對 c2 == c 也成立。

為了找到區間內最後一個 c 的位置，可以預處理出每個位置前一個 c 的位置。
為了計算區間內有多少個 c，可以對每個字母預處理出前綴和。
上述做法是 O(26n + 26^2 * q) 的，可以接受。

但我們只關心左側區間的奇偶性，以及右側區間是否存在該字母。
可以狀態壓縮成一個整數，分別用前綴異或和以及和 ST 表維護。
可以省去枚舉 c2 的過程，時間複雜度為 O(26n + 26q)。

~~然而並沒有快多少~~
*/
#include <bits/stdc++.h>
using namespace std;
using LL = long long;
#define endl '\n'

/* START of FAST IO */
inline int read() {
    int x = 0, f = 1;
    char c = getchar();
    while (c < '0' || c > '9') {
        if (c == '-') f = -1;
        c = getchar();
    }
    while (c >= '0' && c <= '9') {
        x = (x << 3) + (x << 1) + (c ^ 48);
        c = getchar();
    }
    return x * f;
}

inline void write(LL x) {
    if (x < 0) {
        putchar('-');
        x = -x;
    }
    if (x > 9) write(x / 10);
    putchar(x % 10 + '0');
}
/* END of FAST IO */

void solve1() {
    int n = read(); getchar();
    string s; getline(cin, s);
    vector<int> A(n);
    for (auto &x : A) x = read();

    // 為了避免 cache miss，這裡需要使用 N * 26 的二維陣列
    vector<array<int, 26>> ss(n + 1);
    vector<array<int, 26>> pre(n + 1);
    for (int i = 1; i <= n; i++) {
        int c = s[i - 1] - 'a';
        for (int j = 0; j < 26; j++) {
            ss[i][j] = ss[i - 1][j] + (c == j);
            pre[i][j] = (c == j ? i : pre[i - 1][j]);
        }
    }

    int q, op, x, y, l, r;
    q = read();
    while (q--) {
        op = read();
        if (op == 1) {
            x = read(); y = read();
            A[x - 1] = y;
        } else {
            l = read(); r = read();
            LL res = 0;
            for (int c = 0; c < 26; c++) {
                // 在 [l, r] 之間有偶數個 c，不會剩下
                if (((ss[r][c] - ss[l - 1][c]) & 1) == 0) continue;
                // 最後一個 c 的位置
                int p = pre[r][c]; 
                // 檢查是否有其他字母 c2 會橫跨最後一個 c
                bool flag = true;
                for (int c2 = 0; c2 < 26; c2++) {
                    int L = ss[p - 1][c2] - ss[l - 1][c2];
                    int R = ss[r][c2] - ss[p][c2];
                    // 左側有奇數個 c2 且右側有 c2，則會包含 p，不合法
                    if (L & 1 && R > 0) {
                        flag = false;
                        break;
                    }
                }
                if (flag) res += A[p - 1];
            }
            write(res); putchar('\n');
        }
    }
    return;
}

template<typename T, typename Op = function<T(T, T)>>
class SparseTable {
private:
    vector<vector<T>> st;
    Op merge;
    int n;
public:
    SparseTable(const vector<T>& data, Op op) : merge(op), n(data.size()) {
        if (n == 0) return;
        int max_log = __lg(n); 
        st.assign(n, vector<T>(max_log + 1));

        for (int i = 0; i < n; ++i)
            st[i][0] = data[i];

        for (int j = 1; j <= max_log; ++j)
            for (int i = 0; i + (1 << j) <= n; ++i)
                st[i][j] = merge(st[i][j - 1], st[i + (1 << (j - 1))][j - 1]);
    }

    T query(int L, int R) {  // 0-indexed
        int k = __lg(R - L + 1);
        return merge(st[L][k], st[R - (1 << k) + 1][k]);
    }
};

void solve2() {
    int n = read(); getchar();
    string s; getline(cin, s);
    vector<int> A(n);
    for (auto &x : A) x = read();

    vector<int> vis(n + 1), sxor(n + 1);
    // 為了避免 cache miss，這裡需要使用 N * 26 的二維陣列
    vector<array<int, 26>> pre(n + 1);
    for (int i = 1; i <= n; i++) {
        int c = s[i - 1] - 'a';
        vis[i] = (1 << c);
        sxor[i] = sxor[i - 1] ^ (1 << c);
        for (int j = 0; j < 26; j++)
            pre[i][j] = (c == j ? i : pre[i - 1][j]);
    }

    auto func = [](int a, int b) { return a | b; };
    SparseTable<int, decltype(func)> st(vis, func);
    
    int q, op, x, y, l, r;
    q = read();
    while (q--) {
        op = read();
        if (op == 1) {
            x = read(); y = read();
            A[x - 1] = y;
        } else {
            l = read(); r = read();
            LL res = 0;
            for (int c = 0; c < 26; c++) {
                int p = pre[r][c];
                if (p < l) continue;
                int msk1 = sxor[p - 1] ^ sxor[l - 1];  // [l, p - 1] 的奇偶性
                int msk2 = st.query(p, r);  // [p, r] 的字母出現情況
                if ((msk1 & msk2) == 0) res += A[p - 1];
            }
            write(res); putchar('\n');
        }
    }
    return;
}

int main() {
    // solve1();
    solve2();
    return 0;
}