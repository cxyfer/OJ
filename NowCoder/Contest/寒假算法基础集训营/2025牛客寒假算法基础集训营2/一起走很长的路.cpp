#include <bits/stdc++.h>
using namespace std;
using LL = long long;
const LL INF = 0x3f3f3f3f3f3f3f3f;

class SegmentTree {
private:
    vector<LL> nums;
    vector<LL> tree;
public:
    SegmentTree(vector<LL>& nums) {
        int n = nums.size();
        this->nums = vector<LL>(n + 1, 0);
        for (int i = 1; i <= n; i++) this->nums[i] = nums[i - 1]; // 1-indexed
        this->tree = vector<LL>(4 * n, 0);
        build(1, 1, n);
    }

    void build(int o, int left, int right) {
        if (left == right) {
            tree[o] = nums[left];
            return;
        }
        int mid = (left + right) / 2;
        build(2 * o, left, mid);
        build(2 * o + 1, mid + 1, right);
        tree[o] = merge(tree[2 * o], tree[2 * o + 1]);
    }

    LL merge(LL left_child, LL right_child) {
        return max(left_child, right_child);
    }

    LL query(int o, int left, int right, int l, int r) {
        if (l <= left && right <= r) return tree[o];
        int mid = (left + right) / 2;
        LL ans = -INF;
        if (l <= mid) ans = max(ans, query(2 * o, left, mid, l, r));
        if (r > mid) ans = max(ans, query(2 * o + 1, mid + 1, right, l, r));
        return ans;
    }
};

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    
    int n, q;
    cin >> n >> q;
    vector<LL> A(n);
    for (int i = 0; i < n; i++) cin >> A[i];

    vector<LL> s(n + 1, 0);
    for (int i = 0; i < n; i++) {
        s[i + 1] = s[i] + A[i];
    }

    vector<LL> d(n);
    for (int i = 1; i < n; i++) {
        d[i] = A[i] - s[i];
    }

    SegmentTree st(d);
    while (q--) {
        int l, r;
        cin >> l >> r;
        
        if (l == r) {
            cout << 0 << '\n';
            continue;
        }

        LL mx = st.query(1, 1, n, l + 1, r);
        LL ans = abs(max(0LL, s[l - 1] + mx));
        cout << ans << '\n';
    }
    
    return 0;
}