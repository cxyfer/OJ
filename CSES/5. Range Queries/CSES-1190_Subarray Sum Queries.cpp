#include <bits/stdc++.h>
using namespace std;
using LL = long long;
#define endl '\n'

struct Info {
    LL sum, lSum, rSum, mSum;
    Info(LL sum = 0, LL lSum = 0, LL rSum = 0, LL mSum = 0) : sum(sum), lSum(lSum), rSum(rSum), mSum(mSum) {}
};

class SegmentTree {
private:
    vector<LL> nums;
    vector<Info> tree;
public:
    SegmentTree(vector<LL>& nums) {
        int n = nums.size();
        this->nums = vector<LL>(n + 1, 0);
        for (int i = 1; i <= n; i++) this->nums[i] = nums[i - 1]; // 1-indexed
        this->tree = vector<Info>(4 * n, Info());
        build(1, 1, n);
    }

    void build(int o, int left, int right) {
        if (left == right) {
            tree[o] = Info(nums[left], nums[left], nums[left], nums[left]);
            return;
        }
        int mid = (left + right) / 2;
        build(2 * o, left, mid);
        build(2 * o + 1, mid + 1, right);
        tree[o] = merge(tree[2 * o], tree[2 * o + 1]);
    }

    void update(int o, int left, int right, int idx, int val) {
        if (left == right) {
            tree[o] = Info(val, val, val, val);
            return;
        }
        int mid = (left + right) / 2;
        if (idx <= mid) update(2 * o, left, mid, idx, val);
        else update(2 * o + 1, mid + 1, right, idx, val);
        tree[o] = merge(tree[2 * o], tree[2 * o + 1]);
    }

    Info query(int o, int left, int right, int l, int r) {
        if (l <= left && right <= r) return tree[o];
        int mid = (left + right) / 2;
        Info ans = Info();
        if (l <= mid) ans = merge(ans, query(2 * o, left, mid, l, r));
        if (r > mid) ans = merge(ans, query(2 * o + 1, mid + 1, right, l, r));
        return ans;
    }

    Info merge(Info a, Info b) {
        Info res;
        res.sum = a.sum + b.sum;
        res.lSum = max(a.lSum, a.sum + b.lSum);
        res.rSum = max(b.rSum, b.sum + a.rSum);
        res.mSum = max(max(a.mSum, b.mSum), a.rSum + b.lSum);
        return res;
    }
};

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    int n, q; cin >> n >> q;
    vector<LL> nums(n);
    for (int i = 0; i < n; ++i) cin >> nums[i];
    SegmentTree seg(nums);
    int idx, val;
    while (q--) {
        cin >> idx >> val;
        seg.update(1, 1, n, idx, val);
        cout << max(0LL, seg.query(1, 1, n, 1, n).mSum) << endl;  // 考慮不選的情況
    }
    return 0;
}