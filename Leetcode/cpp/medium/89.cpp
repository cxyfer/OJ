/*
 * @lc app=leetcode.cn id=89 lang=cpp
 * @lcpr version=30204
 *
 * [89] 格雷编码
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution1 {
public:
    vector<int> grayCode(int n) {
        if (n == 0) return {0};
        vector<int> ans = grayCode(n - 1);
        for (int i = ans.size() - 1; i >= 0; i--) {
            ans.push_back(ans[i] | (1 << (n - 1)));
        }
        return ans;
    }
};

class Solution2 {
public:
    vector<int> grayCode(int n) {
        vector<int> ans = {0};
        for (int i = 0; i < n; i++)
            for (int j = ans.size() - 1; j >= 0; j--)
                ans.push_back(ans[j] | (1 << i));
        return ans;
    }
};

using Solution = Solution1;
// using Solution = Solution2;
// @lc code=end



/*
// @lcpr case=start
// 2\n
// @lcpr case=end

// @lcpr case=start
// 1\n
// @lcpr case=end

 */

