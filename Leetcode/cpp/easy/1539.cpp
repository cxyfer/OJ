/*
 * @lc app=leetcode.cn id=1539 lang=cpp
 * @lcpr version=30204
 *
 * [1539] 第 k 个缺失的正整数
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution {
public:
    int findKthPositive(vector<int>& arr, int k) {
        auto check = [&](int m) -> bool {
            return arr[m] - (m + 1) >= k;
        };

        int left = 0, right = arr.size() - 1;
        while (left <= right) {
            int mid = left + (right - left) / 2;
            if (check(mid)) right = mid - 1;
            else left = mid + 1;
        }
        // if (right < 0) return k;
        // return arr[right] + k - (arr[right] - (right + 1));
        return k + right + 1;
    }
};
// @lc code=end

/*
// @lcpr case=start
// [2,3,4,7,11]\n5\n
// @lcpr case=end

// @lcpr case=start
// [1,2,3,4]\n2\n
// @lcpr case=end

 */

