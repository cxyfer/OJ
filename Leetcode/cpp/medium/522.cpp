/*
 * @lc app=leetcode.cn id=522 lang=cpp
 *
 * [522] 最长特殊序列 II
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution {
public:
    int findLUSlength(vector<string>& strs) {
        // return solve1(strs);
        // return solve2(strs);
        return solve3(strs);
    }

    int solve1(vector<string>& strs) {
        int n = strs.size(), ans = -1;
        for (int i = 0; i < n; i++) {
            bool flag = true;
            for (int j = 0; j < n; j++) {
                if (i != j && isSubsequence(strs[i], strs[j])) {
                    flag = false;
                    break;
                }
            }
            if (flag) ans = max(ans, (int)strs[i].size());
        }
        return ans;
    }

    int solve2(vector<string>& strs) {
        int n = strs.size();
        sort(strs.begin(), strs.end(), [](const string& a, const string& b) {
            return a.size() > b.size();
        });
        for (int i = 0; i < n; i++) {
            bool flag = true;
            for (int j = 0; j < n; j++) {
                if (i != j && isSubsequence(strs[i], strs[j])) {
                    flag = false;
                    break;
                }
            }
            if (flag) return strs[i].size();
        }
        return -1;
    }

    int solve3(vector<string>& strs) {
        int n = strs.size();
        unordered_map<string, int> cnt;
        for (string& s : strs) cnt[s]++;
        vector<string> uniques;
        for (auto kv : cnt) if (kv.second == 1) uniques.push_back(kv.first);
        sort(uniques.begin(), uniques.end(), [](const string& a, const string& b) {
            return a.size() > b.size();
        });
        for (string& s : uniques) {
            bool flag = true;
            for (string& t : strs) {
                if (s != t && isSubsequence(s, t)) {
                    flag = false;
                    break;
                }
            }
            if (flag) return s.size();
        }
        return -1;
    }

    bool isSubsequence(string s, string t) {
        int m = s.size(), n = t.size();
        int i = 0, j = 0;
        while (i < m && j < n) {
            if (s[i] == t[j++]) i++;
        }
        return i == m;
    }
};
// @lc code=end