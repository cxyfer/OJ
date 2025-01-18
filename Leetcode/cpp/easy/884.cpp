/*
 * @lc app=leetcode.cn id=884 lang=cpp
 *
 * [884] 两句话中的不常见单词
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution {
public:
    vector<string> uncommonFromSentences(string s1, string s2) {
        unordered_map<string, int> cnt;

        function<void(string)> insert = [&](string s) {
            int n = s.size(), i = 0, st = 0;
            while (i < n) {
                st = i;
                while (i < n && s[i] != ' ') i++;
                cnt[s.substr(st, i - st)]++;
                i++; // skip space
            }
        };

        insert(s1);
        insert(s2);
        
        vector<string> ans;
        for (auto &[word, v] : cnt) {
            if (v == 1) {
                ans.push_back(word);
            }
        }
        return ans;
    }
};
// @lc code=end

int main() {
    Solution sol = Solution();
    string s1 = "this apple is sweet";
    string s2 = "this apple is sour";
    vector<string> ans = sol.uncommonFromSentences(s1, s2);
    for (auto &word : ans) {
        cout << word << " ";
    }
    cout << endl;
    return 0;
}