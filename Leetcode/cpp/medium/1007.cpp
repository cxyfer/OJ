/*
 * @lc app=leetcode.cn id=1007 lang=cpp
 * @lcpr version=30204
 *
 * [1007] 行相等的最少多米诺旋转
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution {
public:
    int minDominoRotations(vector<int>& tops, vector<int>& bottoms) {
        int n = tops.size();
        auto cacl = [&](int x) -> int {
            int cnt1 = 0, cnt2 = 0;
            for (int i = 0; i < n; i++) {
                if (tops[i] == x && bottoms[i] == x) continue;
                else if (tops[i] == x) cnt1++;
                else if (bottoms[i] == x) cnt2++;
                else return n;
            }
            return min(cnt1, cnt2);
        };
        int ans = min(cacl(tops[0]), cacl(bottoms[0]));
        return ans == n ? -1 : ans;
    }
};
// @lc code=end



/*
// @lcpr case=start
// [2,1,2,4,2,2]\n[5,2,6,2,3,2]\n
// @lcpr case=end

// @lcpr case=start
// [3,5,1,2,3]\n[3,6,3,3,4]\n
// @lcpr case=end

 */

