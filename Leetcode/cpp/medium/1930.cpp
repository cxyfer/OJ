/*
 * @lc app=leetcode.cn id=1930 lang=cpp
 * @lcpr version=30204
 *
 * [1930] 长度为 3 的不同回文子序列
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution1 {
public:
    int countPalindromicSubsequence(string s) {
        int n = s.size();
        int ans = 0;
        for (int c = 0; c < 26; c++) {
            int left = 0, right = n - 1;
            while (left < n && s[left] - 'a' != c) left++;
            while (right >= 0 && s[right] - 'a' != c) right--;
            int mask = 0;
            for (int i = left + 1; i < right; i++)
                mask |= 1 << (s[i] - 'a');
            ans += __builtin_popcount(mask);
        }
        return ans;
    }
};

class Solution2 {
public:
    int countPalindromicSubsequence(string s) {
        int n = s.size();
        vector<int> pre(26), suf(26), masks(26);
        for (int i = 1; i < n; i++) suf[s[i] - 'a']++;
        for (int i = 1; i < n - 1; i++) {
            pre[s[i - 1] - 'a']++;
            suf[s[i] - 'a']--;
            for (int c = 0; c < 26; c++)
                if (pre[c] > 0 && suf[c] > 0)
                    masks[s[i] - 'a'] |= 1 << c;
        }
        int ans = 0;
        for (int c = 0; c < 26; c++)
            ans += __builtin_popcount(masks[c]);
        return ans;
    }
};

// using Solution = Solution1;
using Solution = Solution2;
// @lc code=end



/*
// @lcpr case=start
// "aabca"\n
// @lcpr case=end

// @lcpr case=start
// "adc"\n
// @lcpr case=end

// @lcpr case=start
// "bbcbaba"\n
// @lcpr case=end

 */

