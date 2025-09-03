/*
 * @lc app=leetcode.cn id=315 lang=cpp
 * @lcpr version=30204
 *
 * [315] 计算右侧小于当前元素的个数
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
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

class Solution {
public:
    vector<int> countSmaller(vector<int>& nums) {
        int n = nums.size();
        // 離散化
        auto B = nums;
        sort(B.begin(), B.end());
        B.erase(unique(B.begin(), B.end()), B.end());
        int m = B.size();
        for (auto &x : nums) x = lower_bound(B.begin(), B.end(), x) - B.begin() + 1;

        // BIT
        BIT bit(m);
        vector<int> ans(n);
        for (int i = n - 1; i >= 0; i--) {
            ans[i] = bit.query(1, nums[i] - 1);
            bit.add(nums[i], 1);
        }
        return ans;
    }
};
// @lc code=end



/*
// @lcpr case=start
// [5,2,6,1]\n
// @lcpr case=end

// @lcpr case=start
// [-1]\n
// @lcpr case=end

// @lcpr case=start
// [-1,-1]\n
// @lcpr case=end

 */

