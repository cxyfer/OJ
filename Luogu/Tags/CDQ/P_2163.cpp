/*
P2163 [SHOI2007] 园丁的烦恼
https://www.luogu.com.cn/problem/P2163
二維數點問題

首先用二維前綴和的方式理解，令 f(i, j) 表示以 (i, j) 為右下角的矩形內的點的個數，
則左上角為 (a, b)，右下角為 (c, d) 的矩形內的點的個數為 f(c, d) - f(a - 1, d) - f(c, b - 1) + f(a - 1, b - 1)
自此可以把每條詢問拆解成四個問題。

而求 f(a, b)，相當於求 x[k] <= a, y[k] <= b 的點的個數，
將查詢的點視為虛擬點，那我們還需要確保所有實際點都先被處理過，但這可以透過對 (x, type) 排序就能解決。
因此這是二維偏序問題，可以考慮 CDQ 分治來求解。

Python / JAVA 注定會 MLE，只能用 C++。
*/

#include <bits/stdc++.h>
using namespace std;
#define endl '\n'

struct Event {
    int x, y;
    int type;  // 1 for real point, 0 for query event
    int qid;    // query id
    int coef;  // inclusion-exclusion coefficient
    Event() : x(0), y(0), type(0), qid(-1), coef(0) {}
    Event(int x, int y, int type) : x(x), y(y), type(type), qid(-1), coef(0) {}
    Event(int x, int y, int type, int qid, int coef)
        : x(x), y(y), type(type), qid(qid), coef(coef) {}

    
};

void solve() {
    int n, m;
    cin >> n >> m;
    int N = n + (m << 2);

    vector<Event> events;
    events.reserve(N);

    for (int i = 0; i < n; ++i) {
        int x, y;
        cin >> x >> y;
        events.emplace_back(x, y, 1);
    }

    for (int i = 0; i < m; ++i) {
        int a, b, c, d;
        cin >> a >> b >> c >> d;
        events.emplace_back(a - 1, b - 1, 0, i, 1);
        events.emplace_back(a - 1, d, 0, i, -1);
        events.emplace_back(c, b - 1, 0, i, -1);
        events.emplace_back(c, d, 0, i, 1);
    }

    sort(events.begin(), events.end(), [](const Event& lhs, const Event& rhs) {
        if (lhs.x != rhs.x) return lhs.x < rhs.x;
        return lhs.type > rhs.type;
    });

    vector<int> ans(m);
    vector<Event> tmp(N);

    auto cmp_y = [](const Event& lhs, const Event& rhs) {
        if (lhs.y != rhs.y) return lhs.y < rhs.y;
        return lhs.type > rhs.type;
    };

    auto cdq = [&](this auto&& cdq, int left, int right) -> void {
        if (left >= right) return;
        int mid = (left + right) >> 1;
        cdq(left, mid);
        cdq(mid + 1, right);

        int cnt = 0;
        for (int i = left, j = mid + 1; j <= right; ++j) {
            while (i <= mid && events[i].y <= events[j].y) {
                cnt += events[i].type;
                i++;
            }
            if (events[j].type == 0) {
                ans[events[j].qid] += cnt * events[j].coef;
            }
        }

        // sort(events.begin() + left, events.begin() + right + 1, cmp_y);
        int i = left, j = mid + 1, k = left;
        while (i <= mid && j <= right) {
            if (cmp_y(events[i], events[j])) {
                tmp[k++] = events[i++];
            } else {
                tmp[k++] = events[j++];
            }
        }
        while (i <= mid) tmp[k++] = events[i++];
        while (j <= right) tmp[k++] = events[j++];
        for (int p = left; p <= right; ++p) {
            events[p] = tmp[p];
        }
    };

    cdq(0, N - 1);

    for (int x : ans) {
        cout << x << endl;
    }

    return;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    solve();
    return 0;
}