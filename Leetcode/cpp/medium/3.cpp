/*
 * @lc app=leetcode id=3 lang=cpp
 * @lcpr version=30112
 *
 * [3] Longest Substring Without Repeating Characters
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution {
public:
    // Sliding window
    int lengthOfLongestSubstring(string s) {
        int n = s.size();
        int ans = 0;
        map<char, int> cnt;
        int l = 0, r = 0; 
        while (r < n) {
            cnt[s[r]]++;
            while (cnt[s[r]] > 1) {
                cnt[s[l]]--;
                l++;
            }
            ans = max(ans, r - l + 1);
            r++;
        }
        return ans;
    }
};
// @lc code=end



/*
// @lcpr case=start
// "abcabcbb"\n
// @lcpr case=end

// @lcpr case=start
// "bbbbb"\n
// @lcpr case=end

// @lcpr case=start
// "pwwkew"\n
// @lcpr case=end

 */

