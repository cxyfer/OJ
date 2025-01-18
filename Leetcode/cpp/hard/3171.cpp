/*
 * @lc app=leetcode.cn id=3171 lang=cpp
 *
 * [3171] 找到按位与最接近 K 的子数组
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution1 {
public:
    int minimumDifference(vector<int>& nums, int k) {
        int n = nums.size();
        int ans = INT_MAX;
        vector<int> st;
        for (int x : nums) {
            vector<int> st2 = {x};
            for (int y : st) {
                if ((y | x) != st2.back()) {
                    st2.push_back(y | x);
                }
            }
            st = st2;
            for (int y : st) {
                ans = min(ans, abs(y - k));
            }
        }
        return ans;
    }
};

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
        return tree[left_child] | tree[right_child];
    }

    int query(int o, int left, int right, int l, int r) {
        if (l <= left && right <= r) return tree[o];
        int mid = (left + right) / 2;
        int ans = 0;
        if (l <= mid) ans |= query(2 * o, left, mid, l, r);
        if (r > mid) ans |= query(2 * o + 1, mid + 1, right, l, r);
        return ans;
    }
};

class Solution2 {
public:
    int minimumDifference(vector<int>& nums, int k) {
        int n = nums.size();
        SegmentTree seg(nums);
        int ans = INT_MAX;
        for (int i = 1; i <= n; i++) {
            int left = i, right = n;
            while (left <= right) {
                int mid = left + (right - left) / 2;
                if (seg.query(1, 1, n, i, mid) >= k) right = mid - 1;
                else left = mid + 1;
            }
            ans = min(ans, abs(seg.query(1, 1, n, i, left) - k));
            if (right >= i) ans = min(ans, abs(k - seg.query(1, 1, n, i, right)));
        }
        return ans;
    }
};

class Solution : public Solution1 {};
// class Solution : public Solution2 {};
// @lc code=end

int main() {
    Solution sol = Solution();
    vector<int> nums = {1,8,9};
    int k = 7;
    cout << sol.minimumDifference(nums, k) << endl; // 1
    return 0;
}