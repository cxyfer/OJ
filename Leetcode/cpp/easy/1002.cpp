/*
 * @lc app=leetcode.cn id=1002 lang=cpp
 *
 * [1002] 查找共用字符
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution {
public:
    vector<string> commonChars(vector<string>& words) {
        vector<int> cnt(26, INT_MAX), cur(26, 0);
        for (auto &word : words) {
            fill(cur.begin(), cur.end(), 0);
            for (auto &ch : word) cur[ch - 'a']++;
            for (int i = 0; i < 26; i++) cnt[i] = min(cnt[i], cur[i]);
        }
        vector<string> ans, tmp;
        for (int i = 0; i < 26; i++) {
            tmp.resize(cnt[i]);
            fill(tmp.begin(), tmp.end(), string(1, i + 'a'));
            ans.insert(ans.end(), tmp.begin(), tmp.end());
        }
        return ans;
    }
};
// @lc code=end

int main() {
    Solution sol = Solution();
    vector<string> words = {"bella", "label", "roller"};
    vector<string> ans = sol.commonChars(words);
    for (auto &s : ans) cout << s << " ";
    cout << endl;
    return 0;
}