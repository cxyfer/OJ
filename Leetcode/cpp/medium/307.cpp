/*
 * @lc app=leetcode.cn id=307 lang=cpp
 *
 * [307] 区域和检索 - 数组可修改
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start

/*
    Binary Indexed Tree (Fenwick Tree, BIT) 模板題
    Reference:
     - https://iyukiyama.github.io/binary-indexed-tree/
     - https://leetcode.cn/problems/range-sum-query-mutable/solutions/2524481/dai-ni-fa-ming-shu-zhuang-shu-zu-fu-shu-lyfll/
*/
class FenwickTree { // PURQ (Point Update Range Query), 1-based, initialization: O(n)
private:
    int n = 0;
    vector<int> tree;
    vector<int> nums;
public:
    FenwickTree(vector<int>& nums) {
        n = nums.size();
        this->nums = nums;
        tree = vector<int>(n + 1); // 1-based
        for (int i = 1; i <= n; i++) { // initialization: O(n)
            tree[i] += nums[i-1];
            int nxt = i + (i & -i); // 下一個關鍵區間的右端點
            if (nxt <= n) {
                tree[nxt] += tree[i];
            }
        }
    }

    void add(int k, int x) { // 令 nums[k] += x
        for (int i = k+1; i < tree.size(); i += i & -i) {
            tree[i] += x;
        }
    }

    void update(int k, int x) { // 令 nums[k] = x
        add(k, x - nums[k]);
        nums[k] = x;
    }

    int sum(int l, int r) { // 區間查詢 (區間求和): 求 nums[l] 到 nums[r] 之和
        return preSum(r+1) - preSum(l);
    }

    int preSum(int k) { // 求前綴和: 求 nums[0] 到 nums[k] 的區間和
        int s = 0;
        for (int i = k; i > 0; i -= i & -i) {
            s += tree[i];
        }
        return s;
    }
};

class NumArray {
public:
    FenwickTree* bit;
    NumArray(vector<int>& nums) {
        bit = new FenwickTree(nums);
    }
    
    void update(int index, int val) {
        bit->update(index, val);
    }
    
    int sumRange(int left, int right) {
        return bit->sum(left, right);
    }
};
// @lc code=end

