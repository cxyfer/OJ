/*
 * @lc app=leetcode.cn id=3325 lang=cpp
 *
 * [3325] 字符至少出现 K 次的子字符串 I
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
/*
    Sliding Window: 求子陣列個數 - 越長越合法
*/
class Solution {
public:
    int numberOfSubstrings(string s, int k) {
        int ans = 0, left = 0;
        unordered_map<char, int> cnt;
        for (char ch : s) {
            cnt[ch]++;
            while (cnt[ch] >= k) {
                cnt[s[left]]--;
                left++;
            }
            ans += left;
        }
        return ans;
    }
};
// @lc code=end

