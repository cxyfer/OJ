#include <bits/stdc++.h>
using namespace std;
using i64 = long long;
#define endl '\n'

class BIT {  // PURQ, 1-based
private:
    vector<int> tree;

public:
    BIT(int n) {
        tree = vector<int>(n + 1, 0);
    }

    void add(int k, int x) {  // 令 nums[k] += x
        for (; k < tree.size(); k += k & -k) tree[k] += x;
    }

    int preSum(int k) {  // 求 nums[:k+1] 之和
        int res = 0;
        for (; k > 0; k -= k & -k) res += tree[k];
        return res;
    }

    int query(int l, int r) {  // 求 nums[l:r+1] 之和
        if (l > r) return 0;
        return preSum(r) - preSum(l - 1);
    }
};

struct Event {
    int x, y, typ;
    i64 v;
    int qid, coef;

    Event() : x(0), y(0), typ(0), v(0), qid(-1), coef(0) {}
    Event(int x, int y, i64 v) : x(x), y(y), typ(1), v(v), qid(-1), coef(0) {}
    Event(int x, int y, int qid, int coef)
        : x(x), y(y), typ(2), v(0), qid(qid), coef(coef) {}
};

void solve() {
    int _;
    int w;
    cin >> _ >> w;

    vector<Event> events;
    vector<i64> ans;

    while (true) {
        int op;
        cin >> op;
        if (op == 3) break;

        if (op == 1) {
            int x, y, v;
            cin >> x >> y >> v;
            events.emplace_back(x, y, v);
        } else {
            int x1, y1, x2, y2;
            cin >> x1 >> y1 >> x2 >> y2;
            int qid = ans.size();
            ans.push_back(0);
            events.emplace_back(x1 - 1, y1 - 1, qid, 1);
            events.emplace_back(x1 - 1, y2, qid, -1);
            events.emplace_back(x2, y1 - 1, qid, -1);
            events.emplace_back(x2, y2, qid, 1);
        }
    }

    BIT bit(w);
    vector<Event> tmp(events.size());

    auto cdq = [&](this auto&& cdq, int left, int right) -> void {
        if (left >= right) return;
        int mid = (left + right) >> 1;
        cdq(left, mid);
        cdq(mid + 1, right);

        int i = left;
        for (int j = mid + 1; j <= right; ++j) {
            while (i <= mid && events[i].x <= events[j].x) {
                if (events[i].typ == 1) {
                    bit.add(events[i].y, events[i].v);
                }
                ++i;
            }
            if (events[j].typ == 2) {
                ans[events[j].qid] +=
                    bit.query(1, events[j].y) * events[j].coef;
            }
        }

        for (int j = left; j < i; ++j) {
            if (events[j].typ == 1) {
                bit.add(events[j].y, -events[j].v);
            }
        }

        int p = left, q = mid + 1, k = left;
        while (p <= mid && q <= right) {
            if (events[p].x < events[q].x || (events[p].x == events[q].x &&
                                              events[p].typ <= events[q].typ)) {
                tmp[k++] = events[p++];
            } else {
                tmp[k++] = events[q++];
            }
        }
        while (p <= mid) tmp[k++] = events[p++];
        while (q <= right) tmp[k++] = events[q++];
        for (int j = left; j <= right; ++j) {
            events[j] = tmp[j];
        }
    };

    cdq(0, events.size() - 1);

    for (auto x : ans) cout << x << endl;

    return;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    solve();
    return 0;
}