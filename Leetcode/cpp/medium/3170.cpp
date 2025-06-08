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
class Solution1 {
public:
    string clearStars(string s) {
        int n = s.size();
        vector<stack<int>> pos(26);
        for (int i = 0; i < n; i++) {
            if (s[i] == '*') {
                for (int j = 0; j < 26; j++) {
                    if (!pos[j].empty()) {
                        s[pos[j].top()] = '*'; pos[j].pop();  // 把要刪除的字元改成星號
                        break;
                    }
                }
            } else {
                pos[s[i] - 'a'].push(i);
            }
        }
        erase(s, '*');
        return s;
    }
};

class Solution2 {
public:
    string clearStars(string s) {
        int n = s.size();
        priority_queue<pair<int, int>> pq;  // Max heap, {char, index}
        for (int i = 0; i < n; i++) {
            if (s[i] != '*') {
                pq.push({-s[i], i});
            } else {
                s[pq.top().second] = '*';  // 把要刪除的字元改成星號
                pq.pop();
            }
        }
        erase(s, '*');
        return s;
    }
};

class Solution3 {
public:
    string clearStars(string s) {
        int n = s.size(), vis = 0;
        vector<stack<int>> pos(26);
        for (int i = 0; i < n; i++) {
            if (s[i] == '*') {
                int c = __builtin_ctz(vis);
                s[pos[c].top()] = '*'; pos[c].pop();
                if (pos[c].empty())
                    vis &= ~(1 << c);
            } else {
                pos[s[i] - 'a'].push(i);
                vis |= 1 << (s[i] - 'a');
            }
        }
        erase(s, '*');
        return s;
    }
};

// using Solution = Solution1;
// using Solution = Solution2;
using Solution = Solution3;
// @lc code=end


int main() {
    Solution sol = Solution();
    cout << sol.clearStars("aaba*") << endl;
    cout << sol.clearStars("a*") << endl;
    return 0;
}