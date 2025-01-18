/*
 * @lc app=leetcode.cn id=1649 lang=cpp
 *
 * [1649] 通过指令创建有序数组
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
const int MOD = 1e9 + 7;

class FenwickTree { // PURQ (Point Update Range Query), 0-based
private:
    int n;
    vector<int> tree;
public:
    FenwickTree(int n) {
        this->n = n;
        tree = vector<int>(n, 0);
    }
    void add(int k, int x) { // 令 nums[k] += x
        for (int i = k+1; i <= n; i += i & -i) {
            tree[i-1] += x;
        }
    }
    int preSum(int k) { // 求前綴和: 求 nums[0] 到 nums[k] 的區間和
        int res = 0;
        for (int i = k+1; i > 0; i -= i & -i) {
            res += tree[i-1];
        }
        return res;
    }
};

class Solution {
public:
    int createSortedArray(vector<int>& instructions) {
        int n = instructions.size();
        vector<int> sorted_nums = instructions; // 離散化
        sort(sorted_nums.begin(), sorted_nums.end());
        sorted_nums.erase(unique(sorted_nums.begin(), sorted_nums.end()), sorted_nums.end()); // 去重
        int m = sorted_nums.size();
        FenwickTree bit(m);
        int ans = 0, idx, l, r;
        for (int x : instructions) {
            idx = lower_bound(sorted_nums.begin(), sorted_nums.end(), x) - sorted_nums.begin();
            l = bit.preSum(idx - 1);
            r = bit.preSum(m - 1) - bit.preSum(idx);
            ans = (ans + min(l, r)) % MOD;
            bit.add(idx, 1);
        }
        return ans;
    }
};
// @lc code=end

