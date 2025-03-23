/*
 * @lc app=leetcode.cn id=2255 lang=cpp
 * @lcpr version=30204
 *
 * [2255] 统计是给定字符串前缀的字符串数目
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution {
public:
    int countPrefixes(vector<string>& words, string s) {
        // int ans = 0;
        // for (auto& w : words)
        //     // ans += s.find(w) == 0;
        //     ans += s.starts_with(w);
        // return ans;
        return count_if(words.begin(), words.end(), [&](string& w) {
            return s.starts_with(w);
        });
    }
};
// @lc code=end



/*
// @lcpr case=start
// ["a","b","c","ab","bc","abc"]\n"abc"\n
// @lcpr case=end

// @lcpr case=start
// ["a","a"]\n"aa"\n
// @lcpr case=end

 */

