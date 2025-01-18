/*
 * @lc app=leetcode.cn id=3170 lang=cpp
 *
 * [3170] 删除星号以后字典序最小的字符串
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution {
public:
    string clearStars(string s) {
        // return solve1(s);
        return solve2(s);
    }
    string solve1(string s) {
        int n = s.size();
        vector<vector<int>> pos(26);
        for (int i = 0; i < n; i++) {
            if (s[i] != '*') {
                pos[s[i] - 'a'].push_back(i);
            } else {
                for (int j = 0; j < 26; j++) {
                    if (!pos[j].empty()) {
                        s[pos[j].back()] = '*'; // 把要刪除的字元改成星號
                        pos[j].pop_back();
                        break;
                    }
                }
            }
        }
        string ans = "";
        for (char ch : s)
            if (ch != '*')
                ans += ch;
        return ans;
    }
    string solve2(string s) {
        int n = s.size();
        priority_queue<pair<int, int>> pq; // Max heap, {char, index}
        for (int i = 0; i < n; i++) {
            if (s[i] != '*') {
                pq.push({-s[i], i});
            } else {
                s[pq.top().second] = '*'; // 把要刪除的字元改成星號
                pq.pop();
            }
        }
        s.erase(remove(s.begin(), s.end(), '*'), s.end());
        return s;
    }
};
// @lc code=end


int main() {
    Solution sol = Solution();
    cout << sol.clearStars("aaba*") << endl;
    cout << sol.clearStars("a*") << endl;
    return 0;
}