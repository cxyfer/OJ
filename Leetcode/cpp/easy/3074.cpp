/*
 * @lc app=leetcode.cn id=3074 lang=cpp
 * @lcpr version=30204
 *
 * [3074] 重新分装苹果
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution {
public:
    int minimumBoxes(vector<int>& apple, vector<int>& capacity) {
        int s = accumulate(apple.begin(), apple.end(), 0);
        sort(capacity.begin(), capacity.end(), greater<int>());
        int cur = 0;
        for (int i = 0; i < capacity.size(); i++) {
            cur += capacity[i];
            if (cur >= s) return i + 1;
        }
        return 0;
    }
};
// @lc code=end



/*
// @lcpr case=start
// [1,3,2]\n[4,3,1,5,2]\n
// @lcpr case=end

// @lcpr case=start
// [5,5,5]\n[2,4,2,7]\n
// @lcpr case=end

 */

