/*
 * @lc app=leetcode.cn id=33 lang=cpp
 * @lcpr version=30204
 *
 * [33] 搜索旋转排序数组
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution1 {
public:
    int findMin(vector<int>& nums) {
        int n = nums.size();

        auto check = [&](int mid) { return nums[mid] <= nums[n - 1]; };

        int left = 0, right = n - 1;  // [left, right]
        while (left <= right) {
            int mid = left + (right - left) / 2;
            if (check(mid))
                right = mid - 1;
            else
                left = mid + 1;
        }
        return left;
    }

    int search(vector<int>& nums, int target) {
        int n = nums.size();
        int left, right;

        int idx = findMin(nums);
        if (target > nums[n - 1])
            left = 0, right = idx - 1;
        else
            left = idx, right = n - 1;

        auto it =
            lower_bound(nums.begin() + left, nums.begin() + right + 1, target);
        return it == nums.end() || *it != target ? -1 : it - nums.begin();
    }
};

class Solution2 {
public:
    int search(vector<int>& nums, int target) {
        int n = nums.size();

        auto check = [&](int mid) {
            if (nums[mid] <= nums[n - 1])
                return target > nums[n - 1] || target < nums[mid];
            else
                return target > nums[n - 1] && target < nums[mid];
        };

        int left = 0, right = n - 1;  // [left, right]
        while (left <= right) {
            int mid = left + (right - left) / 2;
            if (check(mid))
                right = mid - 1;
            else
                left = mid + 1;
        }
        return right >= 0 && nums[right] == target ? right : -1;
    }
};

// using Solution = Solution1;
using Solution = Solution2;
// @lc code=end



/*
// @lcpr case=start
// [4,5,6,7,0,1,2]\n0\n
// @lcpr case=end

// @lcpr case=start
// [4,5,6,7,0,1,2]\n3\n
// @lcpr case=end

// @lcpr case=start
// [1]\n0\n
// @lcpr case=end

 */

