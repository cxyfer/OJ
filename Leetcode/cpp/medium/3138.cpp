/*
 * @lc app=leetcode id=3138 lang=cpp
 * @lcpr version=30201
 *
 * [3138] Minimum Length of Anagram Concatenation
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution {
public:
    int minAnagramLength(string s) {
        int n = s.size();
        int cnt[26] = {0};
        for (int k = 1; k <= n / 2; k++) {
            cnt[s[k - 1] - 'a']++;
            if (n % k != 0) continue;
            bool flag = true;
            for (int i = k; i < n && flag; i += k) {
                int cnt2[26] = {0};
                for (int j = 0; j < k; j++) {
                    cnt2[s[i + j] - 'a']++;
                }
                for (int j = 0; j < 26 && flag; j++) {
                    if (cnt2[j] != cnt[j]) flag = false;
                }
            }
            if (flag) return k;
        }
        return n;
    }
};
// @lc code=end



/*
// @lcpr case=start
// "abba"\n
// @lcpr case=end

// @lcpr case=start
// "cdef"\n
// @lcpr case=end

 */

