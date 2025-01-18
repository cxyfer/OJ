#include <bits/stdc++.h>
using namespace std;
using LL = long long;
#define endl '\n'

class SegmentTree {
private:
    vector<int> nums;
    vector<LL> tree;
public:
    SegmentTree(vector<int>& nums) {
        int n = nums.size();
        this->nums = vector<int>(n + 1, 0);
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
        tree[o] = merge(2 * o, 2 * o + 1);
    }

    LL merge(int left_child, int right_child) {
        return tree[left_child] + tree[right_child];
    }

    void update(int o, int left, int right, int idx, int val) {
        if (left == right) {
            tree[o] = val;
            return;
        }
        int mid = (left + right) / 2;
        if (idx <= mid) update(2 * o, left, mid, idx, val);
        else update(2 * o + 1, mid + 1, right, idx, val);
        tree[o] = merge(2 * o, 2 * o + 1);
    }

    LL query(int o, int left, int right, int l, int r) {
        if (l <= left && right <= r) return tree[o];
        int mid = (left + right) / 2;
        LL ans = 0;
        if (l <= mid) ans += query(2 * o, left, mid, l, r);
        if (r > mid) ans += query(2 * o + 1, mid + 1, right, l, r);
        return ans;
    }
};

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    int n, q, op, a, b;
    cin >> n >> q;
    vector<int> nums(n);
    for (int i = 0; i < n; i++) cin >> nums[i];
    SegmentTree st(nums);
    while (q--) {
        cin >> op >> a >> b;
        if (op == 1) st.update(1, 1, n, a, b);
        else cout << st.query(1, 1, n, a, b) << endl;
    }
    return 0;
}