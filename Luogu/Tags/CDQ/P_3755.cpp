/*
P3755 [CQOI2017] 老 C 的任务
https://www.luogu.com.cn/problem/P3755
二維數點問題

首先用二維前綴和的方式理解，令 f(i, j) 表示以 (i, j)
為右下角的矩形內的點的權重和， 則左上角為 (a, b)，右下角為 (c, d)
的矩形內的點的權重和為 f(c, d) - f(a - 1, d) - f(c, b - 1) + f(a - 1, b - 1)
自此可以把每條詢問拆解成四個問題。

而求 f(a, b)，相當於求 x[k] <= a, y[k] <= b 的點的個數，
將查詢的點視為虛擬點，那我們還需要確保所有實際點都先被處理過，但這可以透過對 (x,
-v) 排序就能解決。 因此這是二維偏序問題，可以考慮 CDQ 分治來求解。

Similar problems:
- P2163 [SHOI2007] 园丁的烦恼
*/

#include <bits/stdc++.h>
using namespace std;
using i64 = long long;
#define endl '\n'

struct Event {
    i64 x, y, v;
    int typ;   // 1 for real point, 2 for query event
    int qid;   // query id
    int coef;  // inclusion-exclusion coefficient
    Event() : x(0), y(0), v(0), typ(0), qid(-1), coef(0) {}
    Event(i64 x, i64 y, i64 v) : x(x), y(y), v(v), typ(1) {}
    Event(i64 x, i64 y, int qid, int coef)
        : x(x), y(y), typ(2), qid(qid), coef(coef) {}
};

void solve() {
    int n, m;
    cin >> n >> m;
    int N = n + (m << 2);

    vector<Event> events;
    events.reserve(N);

    for (int i = 0; i < n; ++i) {
        int x, y, v;
        cin >> x >> y >> v;
        events.emplace_back(x, y, v);
    }

    for (int i = 0; i < m; ++i) {
        i64 a, b, c, d;  // (a - 1) 可能低於 INT_MIN，所以需要用 i64
        cin >> a >> b >> c >> d;
        events.emplace_back(a - 1, b - 1, i, 1);
        events.emplace_back(a - 1, d, i, -1);
        events.emplace_back(c, b - 1, i, -1);
        events.emplace_back(c, d, i, 1);
    }

    // 按照 x 以及 typ 排序，這樣可以保證在處理詢問點時，左側的實際點都已經被處理過
    sort(events.begin(), events.end(), [](const Event& lhs, const Event& rhs) {
        if (lhs.x != rhs.x) return lhs.x < rhs.x;
        return lhs.typ < rhs.typ;
    });

    vector<long long> ans(m);
    vector<Event> tmp(N);  // 用於 Merge Sort

    auto cdq = [&](this auto&& cdq, int left, int right) -> void {
        if (left >= right) return;
        int mid = (left + right) >> 1;
        cdq(left, mid);
        cdq(mid + 1, right);

        long long cnt = 0;
        for (int i = left, j = mid + 1; j <= right; ++j) {
            while (i <= mid && events[i].y <= events[j].y) {
                // 左側是實際點，將實際點的權重累加到 cnt 中
                if (events[i].typ == 1) {
                    cnt += events[i].v;
                }
                i++;
            }
            // 右側是詢問點，將 cnt 乘以係數後累加到答案中
            if (events[j].typ == 2) {
                ans[events[j].qid] += cnt * events[j].coef;
            }
        }

        // 用內建的排序會有額外 log n 的複雜度，用 Merge Sort 可以避免
        // sort(events.begin() + left, events.begin() + right + 1, [](const Event& lhs, const Event& rhs) {
        //     return lhs.y < rhs.y;
        // });
        int i = left, j = mid + 1, k = left;
        while (i <= mid && j <= right) {
            if (events[i].y <= events[j].y)
                tmp[k++] = events[i++];
            else
                tmp[k++] = events[j++];
        }
        while (i <= mid) tmp[k++] = events[i++];
        while (j <= right) tmp[k++] = events[j++];
        for (int p = left; p <= right; ++p) {
            events[p] = tmp[p];
        }
    };

    cdq(0, N - 1);

    for (auto& x : ans) {
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