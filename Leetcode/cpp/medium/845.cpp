/*
 * @lc app=leetcode.cn id=845 lang=cpp
 * @lcpr version=30204
 *
 * [845] 数组中的最长山脉
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution {
public:
    int longestMountain(vector<int>& arr) {
        int n = arr.size();
        if (n < 3) return 0;
        int ans = 0;
        int i = 0;
        for (int i = 0; i < n - 2; i++) {
            int st = i;
            while (i < n - 1 && arr[i] < arr[i + 1]) i++;
            if (i == st) continue;
            int md = i;
            while (i < n - 1 && arr[i] > arr[i + 1]) i++;
            if (i == md) continue;
            ans = max(ans, i - st + 1);
            i--;
        }
        return ans;
    }
};
// @lc code=end


/*
// @lcpr case=start
// [2,1,4,7,3,2,5]\n
// @lcpr case=end

// @lcpr case=start
// [2,2,2]\n
// @lcpr case=end

 */

