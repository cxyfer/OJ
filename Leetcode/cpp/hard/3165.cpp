/*
 * @lc app=leetcode.cn id=3165 lang=cpp
 * @lcpr version=30204
 *
 * [3165] 不包含相邻元素的子序列的最大和
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
const int MOD = 1e9 + 7;

struct SegNode {
    vector<long long> f;
    SegNode() : f(4, 0) {}
    
    SegNode operator+(SegNode const& other) const {
        // f00: 不選 left, 不選 right
        // f01: 不選 left, 可選可不選 right
        // f10: 可選可不選 left, 不選 right
        // f11: 可選可不選 left, 可選可不選 right
        SegNode res;
        res.f[0] = max(f[0] + other.f[2], f[1] + other.f[0]);
        res.f[1] = max(f[0] + other.f[3], f[1] + other.f[1]);
        res.f[2] = max(f[2] + other.f[2], f[3] + other.f[0]);
        res.f[3] = max(f[2] + other.f[3], f[3] + other.f[1]);
        return res;
    }
};

class SegmentTree {
public:
    SegmentTree(vector<int>& nums) {
        this->n = nums.size();
        this->tree = vector<SegNode>(4 * n, SegNode());
        build(1, 1, n, nums);
    }

    void update(int idx, int val) {
        _update(1, 1, n, idx, val);
    }

    SegNode query(int l, int r) {
        return _query(1, 1, n, l, r);
    }

    long long query() {
        return tree[1].f[3];
    }

private:
    int n;
    vector<SegNode> tree;

    void build(int o, int left, int right, vector<int>& nums) {
        if (left == right) {
            tree[o].f[3] = max(nums[left - 1], 0);
            return;
        }
        int mid = left + ((right - left) >> 1);
        build(o << 1, left, mid, nums);
        build(o << 1 | 1, mid + 1, right, nums);
        pushup(o);
    }

    // Push up node value
    void pushup(int o) {
        // tree[o] = tree[o << 1] + tree[o << 1 | 1];  // 這樣寫需要重新建構 SegNode，會 TLE
        int l00 = tree[o << 1].f[0], l01 = tree[o << 1].f[1], l10 = tree[o << 1].f[2], l11 = tree[o << 1].f[3];
        int r00 = tree[o << 1 | 1].f[0], r01 = tree[o << 1 | 1].f[1], r10 = tree[o << 1 | 1].f[2], r11 = tree[o << 1 | 1].f[3];
        tree[o].f[0] = max(l00 + r10, l01 + r00) % MOD;
        tree[o].f[1] = max(l00 + r11, l01 + r01) % MOD;
        tree[o].f[2] = max(l10 + r10, l11 + r00) % MOD;
        tree[o].f[3] = max(l10 + r11, l11 + r01) % MOD;
    }

    void _update(int o, int left, int right, int idx, int val) {
        if (left == right) {
            tree[o].f[3] = max(val, 0);
            return;
        }
        int mid = left + ((right - left) >> 1);
        if (idx <= mid)
            _update(o << 1, left, mid, idx, val);
        else
            _update(o << 1 | 1, mid + 1, right, idx, val);
        pushup(o);
    }

    SegNode _query(int o, int left, int right, int l, int r) {
        if (left == l && r == right) return tree[o];
        int mid = left + ((right - left) >> 1);
        if (r <= mid) return _query(o << 1, left, mid, l, r);
        if (mid < l) return _query(o << 1 | 1, mid + 1, right, l, r);
        return _query(o << 1, left, mid, l, mid) +
               _query(o << 1 | 1, mid + 1, right, mid + 1, r);
    }
};

class Solution {
public:
    int maximumSumSubsequence(vector<int>& nums, vector<vector<int>>& queries) {
        int n = nums.size();
        SegmentTree seg(nums);
        int ans = 0;
        for (auto& q : queries) {
            seg.update(q[0] + 1, q[1]);
            ans = (ans + seg.query()) % MOD;
        }
        return ans;
    }
};
// @lc code=end



/*
// @lcpr case=start
// [3,5,9]\n[[1,-2],[0,-3]]\n
// @lcpr case=end

// @lcpr case=start
// [0,-1]\n[[0,-5]]\n
// @lcpr case=end

 */

