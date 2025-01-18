/*
 * @lc app=leetcode.cn id=3298 lang=cpp
 *
 * [3298] 统计重新排列后包含另一个字符串的子字符串数目 II
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution {
public:
    long long validSubstringCount(string word1, string word2) {
        vector<int> cnt(26, 0); // 需要的字元數量
        for (char ch : word2) cnt[ch - 'a']++;
        long long ans = 0;
        int left = 0, need = 0, have = 0;
        for (int x : cnt) if (x > 0) need++; // 需要的字元種類數
        for (int right = 0; right < word1.size(); right++) {
            char rc = word1[right];
            if (--cnt[rc - 'a'] == 0) have++; // 這個字元的數量夠了
            while (left <= right && have == need) {
                char lc = word1[left++];
                if (++cnt[lc - 'a'] == 1) have--; // 這個字元的數量變回不夠
            }
            ans += left; // [0, right], [1, right], [2, right], ..., [left - 1, right] 都是符合條件的子字串
        }
        return ans;
    }
};
// @lc code=end

