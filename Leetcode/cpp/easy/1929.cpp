/*
 * @lc app=leetcode id=1929 lang=cpp
 *
 * [1929] Concatenation of Array
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end 
// @lc code=start
class Solution {
public:
    vector<int> getConcatenation(vector<int>& nums) {
        nums.insert(nums.end(), nums.begin(), nums.end());
        return nums;
    }
};
// @lc code=end

int main() {
    Solution sol = Solution();
    vector<int> nums = {1, 2, 3};
    for (auto &x : sol.getConcatenation(nums)) {
        cout << x << " ";
    }
    cout << endl;
    return 0;
}