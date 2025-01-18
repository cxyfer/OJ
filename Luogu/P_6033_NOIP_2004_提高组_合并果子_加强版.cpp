#include <bits/stdc++.h>
using namespace std;
using LL = long long;
const int MX = 1e5 + 5;

/*
注意到本題中 n 的範圍是 1e7，因此用 Heap 的 O(n log n) 的時間複雜度會超時。

不過不難發現，每次合併後的值，一定比先前合併的值大，因此可以改成用兩個 Queue 來維護。
第一個 Queue 維護尚未合併的值，為此我們需要對 A_i 排序，
注意到本題中 A_i 的範圍是 1e5，因此可以用計數排序，時間複雜度為 O(D)，其中 D 是 A_i 的範圍。
第二個 Queue 維護已經合併的值，每次合併後的值一定比先前合併的值大，因此可以將合併後的值插入到第二個 Queue 中。

取出時，比較兩個 Queue 的頭部，選擇較小的值。
*/

inline LL read() {
    LL x = 0, f = 1;
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

int main() {
    LL n, x;
    n = read();
    vector<LL> cnt(MX);
    for (int i = 0; i < n; i++) {
        x = read();
        cnt[x]++;
    }
    queue<LL> q1, q2;
    for (int i = 0; i < MX; i++) {
        for (int j = 0; j < cnt[i]; j++) {
            q1.push(i);
        }
    }

    auto pop = [&]() {
        LL res = 0;
        if (q2.empty() || (!q1.empty() && q1.front() < q2.front())) {
            res = q1.front(); q1.pop();
        } else {
            res = q2.front(); q2.pop();
        }
        return res;
    };

    LL ans = 0;
    while (q1.size() + q2.size() > 1) {
        LL x = pop(), y = pop();
        ans += x + y;
        q2.push(x + y);
    }
    write(ans);
    return 0;
}