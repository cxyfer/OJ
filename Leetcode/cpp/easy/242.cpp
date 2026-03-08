/*
 * @lc app=leetcode id=242 lang=cpp
 *
 * [242] Valid Anagram
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution1 {
public:
    bool isAnagram(string s, string t) {
        if (s.size() != t.size()) return false;
        unordered_map<char, int> cnt_s, cnt_t;
        for (char c : s) cnt_s[c]++;
        for (char c : t) cnt_t[c]++;
        return cnt_s == cnt_t;
    }
};

class Solution2 {
public:
    bool isAnagram(string s, string t) {
        if (s.size() != t.size()) return false;
        unordered_map<char, int> cnt;
        for (char c : s) cnt[c]++;
        for (char c : t) cnt[c]--;
        return all_of(cnt.begin(), cnt.end(), [](const auto& p) { return p.second == 0; });
    }
};

// using Solution = Solution1;
using Solution = Solution2;
// @lc code=end

