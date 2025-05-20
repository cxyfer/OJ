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
            for (int i = 0; i < n; i++) {
                if (nums[i] > diff[i])
                    return false;
                diff[i + 1] += diff[i];
            }
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
        return left <= m ? left : -1;
    }
};

class Solution2 {
public:
    int minZeroArray(vector<int>& nums, vector<vector<int>>& queries) {
        int n = nums.size(), m = queries.size();
        vector<int> diff(n + 1);
        int s = 0, k = 0;
        for (int i = 0; i < n; i++) {
            s += diff[i];
            while (k < m && s < nums[i]) {
                int l = queries[k][0], r = queries[k][1], v = queries[k][2];
                diff[l] += v;
                diff[r + 1] -= v;
                if (l <= i && i <= r)
                    s += v;
                k++;
            }
            if (s < nums[i])
                return -1;
        }
        return k;
    }
};

// using Solution = Solution1;
using Solution = Solution2;
// @lc code=end

