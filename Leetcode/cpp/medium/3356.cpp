/*
 * @lc app=leetcode id=3356 lang=cpp
 *
 * [3356] Zero Array Transformation II
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution1 {
public:
    int minZeroArray(vector<int>& nums, vector<vector<int>>& queries) {
        int n = nums.size(), m = queries.size();
        
        auto check = [&](auto &&check, int k) -> int {
            vector<int> diff(n + 1);
            for (int j = 0; j < k; j++) {
                int l = queries[j][0], r = queries[j][1], v = queries[j][2];
                diff[l] += v;
                diff[r + 1] -= v;
            }
            for (int i = 1; i <= n; i++) 
                diff[i] += diff[i - 1];
            for (int i = 0; i < n; i++)
                if (nums[i] > diff[i])
                    return false;
            return true;
        };

        int left = 0, right = m;
        while (left <= right) {
            int mid = left + (right - left) / 2;
            if (check(check, mid))
                right = mid - 1;
            else
                left = mid + 1;
        }
        cout << left << endl;
        return left <= m ? left : -1;
    }
};

class Solution : public Solution1 {};
// @lc code=end

