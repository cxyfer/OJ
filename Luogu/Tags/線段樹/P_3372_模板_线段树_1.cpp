#include <bits/stdc++.h>
using namespace std;
using i64 = long long;
#define endl '\n'

/*
Lazy Segment Tree (array-based, recursive)
- Use o, 2*o, 2*o+1 as node indices
- customizable:
    S: segment value type
    F: lazy tag type
    op(S, S) -> S
    e() -> S
    mapping(F, S, seglen) -> S
    composition(F, F) -> F
    id() -> F
*/

template <class S, S (*op)(S, S), S (*e)(), class F, S (*mapping)(F, S, int),
          F (*composition)(F, F), F (*id)()>
class LazySegmentTree {
public:
    int n = 0;
    int root = 1;
    vector<S> val;
    vector<F> lazy;

    LazySegmentTree() : LazySegmentTree(0) {}

    // LazySegmentTree(n)
    explicit LazySegmentTree(int n_) {
        init_n(n_);
    }

    // LazySegmentTree(nums)
    explicit LazySegmentTree(const vector<S>& nums) {
        init_n((int)nums.size());
        if (n > 0) build(root, 1, n, nums);
    }

    void build(int o, int left, int right, const vector<S>& nums) {
        if (left == right) {
            val[o] = nums[left - 1];
            return;
        }
        int mid = (left + right) >> 1;
        build(o * 2, left, mid, nums);
        build(o * 2 + 1, mid + 1, right, nums);
        pushup(o);
    }

    void _update(int o, int left, int right, F f) {
        int seglen = right - left + 1;
        val[o] = mapping(f, val[o], seglen);
        lazy[o] = composition(f, lazy[o]);
    }

    void pushdown(int o, int left, int right) {
        if (left == right) return;
        if (lazy[o] == id_) return;
        int mid = (left + right) >> 1;
        F f = lazy[o];
        _update(o * 2, left, mid, f);
        _update(o * 2 + 1, mid + 1, right, f);
        lazy[o] = id_;
    }

    void pushup(int o) {
        val[o] = op(val[o * 2], val[o * 2 + 1]);
    }

    void update(int o, int left, int right, int l, int r, F f) {
        if (l <= left && right <= r) {
            _update(o, left, right, f);
            return;
        }
        pushdown(o, left, right);
        int mid = (left + right) >> 1;
        if (l <= mid) update(o * 2, left, mid, l, r, f);
        if (r > mid) update(o * 2 + 1, mid + 1, right, l, r, f);
        pushup(o);
    }

    S query(int o, int left, int right, int l, int r) {
        if (l <= left && right <= r) return val[o];
        pushdown(o, left, right);
        int mid = (left + right) >> 1;
        S ans = e_;
        if (l <= mid) ans = op(ans, query(o * 2, left, mid, l, r));
        if (r > mid) ans = op(ans, query(o * 2 + 1, mid + 1, right, l, r));
        return ans;
    }

    // ---------------- external aliases (public API) ----------------
    void apply(int l, int r, F f) {
        if (n <= 0 || l > r) return;
        update(root, 1, n, l, r, f);
    }

    S prod(int l, int r) {
        if (n <= 0 || l > r) return e_;
        return query(root, 1, n, l, r);
    }

    S all_prod() const {
        if (n <= 0) return e_;
        return val[root];
    }

private:
    S e_ = e();
    F id_ = id();

    void init_n(int n_) {
        n = n_;
        e_ = e();
        id_ = id();
        int size = 1 << (bit_width(static_cast<unsigned>(n)) + 1);
        val.assign(size, e_);
        lazy.assign(size, id_);
    }
};

void solve() {
    int n, q;
    cin >> n >> q;
    vector<i64> nums(n);
    for (auto& x : nums) cin >> x;

    auto op = [](i64 a, i64 b) -> i64 { return a + b; };
    auto e = []() -> i64 { return 0; };
    auto mapping = [](i64 f, i64 x, int seglen) -> i64 {
        return x + f * seglen;
    };
    auto composition = [](i64 f, i64 g) -> i64 { return f + g; };
    auto id = []() -> i64 { return 0; };

    LazySegmentTree<i64, op, e, i64, mapping, composition, id> seg(nums);
    while (q--) {
        int op, l, r;
        i64 k;
        cin >> op;
        if (op == 1) {
            cin >> l >> r >> k;
            seg.apply(l, r, k);
        } else {
            cin >> l >> r;
            cout << seg.prod(l, r) << endl;
        }
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    solve();
    return 0;
}