/*
 * @lc app=leetcode.cn id=1358 lang=cpp
 *
 * [1358] 包含所有三种字符的子字符串数目
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution {
public:
    int numberOfSubstrings(string s) {
        int n = s.size();
        int ans = 0, left = 0, have = 0;
        vector<int> cnt(3);
        for (char& ch : s) {
            // 1. 入窗口
            if (++cnt[ch - 'a'] == 1) have++;
            // 2. 出窗口，維持窗口在向左延伸即可滿足條件的狀態
            while (have == 3) {
                if (--cnt[s[left] - 'a'] == 0) have--;
                left++;
            }
            // 3. 累加答案，即以 right 為右端點的子字串中，滿足條件的數量
            ans += left;
        }
        return ans;
    }
};
// @lc code=end

