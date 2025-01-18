#include <bits/stdc++.h>
using namespace std;
using LL = long long;
const int INF = 0x3f3f3f3f;

/*
    Static/Dynamic Range Minimum Queries

    - CSES-1647 Static Range Minimum Queries
    - CSES-1649 Dynamic Range Minimum Queries
*/

class SegmentTree {
private:
    vector<int> nums;
    vector<int> tree;
public:
    SegmentTree(vector<int>& nums) {
        int n = nums.size();
        this->nums = vector<int>(n + 1, 0);
        for (int i = 1; i <= n; i++) this->nums[i] = nums[i - 1]; // 1-indexed
        this->tree = vector<int>(4 * n, 0);
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

    int merge(int left_child, int right_child) {
        return min(tree[left_child], tree[right_child]);
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

    int query(int o, int left, int right, int l, int r) {
        if (l <= left && right <= r) return tree[o];
        int mid = (left + right) / 2;
        int ans = INF;
        if (l <= mid) ans = min(ans, query(2 * o, left, mid, l, r));
        if (r > mid) ans = min(ans, query(2 * o + 1, mid + 1, right, l, r));
        return ans;
    }
};
