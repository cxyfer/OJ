/*
 * @lc app=leetcode.cn id=26 lang=cpp
 *
 * [26] 删除有序数组中的重复项
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution1 {
public:
    int removeDuplicates(vector<int>& nums) {
        int n = nums.size();
        int i = 0, k = 0;
        while (i < n) {
            int j = i;
            while (i < n && nums[i] == nums[j]) i++;
            nums[k++] = nums[j];
        }
        return k;
    }
};

class Solution2 {
public:
    int removeDuplicates(vector<int>& nums) {
        int n = nums.size();
        int k = 1;
        for (int i = 1; i < n; i++)
            if (nums[i] != nums[i - 1])
                nums[k++] = nums[i];
        return k;
    }
};

// using Solution = Solution1;
using Solution = Solution2;
// @lc code=end

