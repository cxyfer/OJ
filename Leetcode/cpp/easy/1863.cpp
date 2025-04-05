/*
 * @lc app=leetcode.cn id=1863 lang=cpp
 *
 * [1863] 找出所有子集的异或总和再求和
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution1 {
public:
    int subsetXORSum(vector<int>& nums) {
        int n = nums.size(), ans = 0;
        for (int i = 0; i < (1 << n); i++) {  // 枚舉所有子集，狀態壓縮
            int cur = 0;                      // 當前子集的 XOR 和
            for (int j = 0; j < n; j++)       // 當前元素是否在子集中
                if (i & (1 << j)) cur ^= nums[j];
            ans += cur;
        }
        return ans;
    }
};

class Solution2 {
public:
    int subsetXORSum(vector<int>& nums) {
        return reduce(nums.begin(), nums.end(), 0, bit_or<int>())
               << (nums.size() - 1);
    }
};

using Solution = Solution1;
// using Solution = Solution2;
// @lc code=end

