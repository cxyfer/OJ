#include <bits/stdc++.h>
using namespace std;
using LL = long long;
#define endl '\n'
#define all(x) x.begin(), x.end()

struct User {
    int l, r, id;
};

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    int t, n;
    cin >> t;
    while (t--) {
        cin >> n;
        vector<User> users(n);
        for (int i = 0; i < n; i++) {
            cin >> users[i].l >> users[i].r;
            users[i].id = i;
        }

        // L[i] 和 R[i] 分別表示能涵蓋用戶 i 的左邊界和右邊界
        vector<int> L(n, -1), R(n, -1);

        // 按照 L 升序，R 降序排序，計算 R
        sort(all(users), [](const User& a, const User& b) {
            return a.l < b.l || (a.l == b.l && a.r > b.r);
        });
        set<int> rs;
        for (int i = 0; i < n; i++) {
            int id = users[i].id;
            // 二分找到第一個大於等於 users[i].r 的值，表示能涵蓋用戶 i 的右邊界
            auto it = rs.lower_bound(users[i].r);
            if (it != rs.end()) {
                R[id] = *it;
            }
            rs.insert(users[i].r);
            // 特判，若下一個用戶和當前用戶的 L 和 R 相同，則當前用戶的 R 只能是 users[i].r
            if (i + 1 < n && users[i].l == users[i + 1].l && users[i].r == users[i + 1].r) {
                R[id] = users[i].r;
            }
        }

        // 按照 R 降序，L 升序排序，計算 L
        sort(all(users), [](const User& a, const User& b) {
            return a.r > b.r || (a.r == b.r && a.l < b.l);
        });
        set<int> ls;
        for (int i = 0; i < n; i++) {
            int id = users[i].id;
            // 二分找到第一個大於 users[i].l 的值，其前一個值就是能涵蓋用戶 i 的左邊界
            auto it = ls.upper_bound(users[i].l);
            if (it != ls.begin()) {
                L[id] = *prev(it);
            }
            ls.insert(users[i].l); // 插入用戶 i 的左邊界
            // 特判，若下一個用戶和當前用戶的 L 和 R 相同，則當前用戶的 L 只能是 users[i].l
            if (i + 1 < n && users[i].r == users[i + 1].r && users[i].l == users[i + 1].l) {
                L[id] = users[i].l;
            }
        }

        // 計算答案，先用 id 還原 users 的順序
        sort(all(users), [](const User& a, const User& b) {
            return a.id < b.id;
        });
        int ans = 0;
        for (int i = 0; i < n; i++) {
            if (L[i] == -1) {
                ans = 0;
            } else {
                ans = R[i] - L[i] - (users[i].r - users[i].l);
            }
            cout << ans << endl;
        }
    }
    return 0;
}