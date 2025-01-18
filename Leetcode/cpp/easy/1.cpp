/*
 * @lc app=leetcode id=1 lang=cpp
 * @lcpr version=30112
 *
 * [1] Two Sum
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        int n = nums.size();
        map<int, int> tbl;
        for (int i=0; i<n; ++i){
            int x = nums[i];
            if (tbl.find(target-x) != tbl.end()){
                return {tbl[target-x], i};
            }
            tbl[x] = i;
        }
        return {};
    }
};
// @lc code=end
int main() {
    Solution sol = Solution();
    vector<int> nums1 = {2,7,11,15};
    int target1 = 9;
    vector<int> nums2 = {3,2,4};
    int target2 = 6;
    vector<int> nums3 = {3,3};
    int target3 = 6;
    vector<int> ans1 = sol.twoSum(nums1, target1);
    vector<int> ans2 = sol.twoSum(nums2, target2);
    vector<int> ans3 = sol.twoSum(nums3, target3);
    cout << ans1[0] << " " << ans1[1] << endl;
    cout << ans2[0] << " " << ans2[1] << endl;
    cout << ans3[0] << " " << ans3[1] << endl;
    return 0;
}


/*
// @lcpr case=start
// [2,7,11,15]\n9\n
// @lcpr case=end

// @lcpr case=start
// [3,2,4]\n6\n
// @lcpr case=end

// @lcpr case=start
// [3,3]\n6\n
// @lcpr case=end

 */

