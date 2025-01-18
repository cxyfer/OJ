/*
 * @lc app=leetcode.cn id=387 lang=cpp
 *
 * [387] 字符串中的第一个唯一字符
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution {
public:
    /*
        1. Hash Table
            使用 Counter 來計算每個字母出現的次數，再遍歷一次 s 找到第一個只出現一次的字母
            - Time: O(n)
            - Space: O(\Sigma) = O(26) = O(1)
        2. Hash Table
            類似 1. ，但是改成保存每個字母的位置，若重複出現則設為 -1。第二次遍歷時只需要遍歷 Hash Table 即可
            - Time: O(n)
            - Space: O(\Sigma) = O(26) = O(1)
        3. Hash Table + Queue
            類似 2. ，但使用 Queue 來維護第一個出現的唯一字母，一次遍歷
    */
    int firstUniqChar(string s) {
        // return solve1(s);
        // return solve2(s);
        return solve3(s);
    }
    int solve1(string s) {
        unordered_map<char, int> cnt;
        for (char ch : s) cnt[ch]++;
        for (int i = 0; i < s.size(); i++) {
            if (cnt[s[i]] == 1) return i;
        }
        return -1;
    }
    int solve2(string s) {
        int n = s.size();
        unordered_map<char, int> pos;
        for (int i = 0; i < n; i++) {
            pos[s[i]] = (pos.find(s[i]) == pos.end()) ? i : -1;
        }
        int ans = n;
        for (auto p : pos) {
            if (p.second != -1 && p.second < ans) ans = p.second;
        }
        return ans == n ? -1 : ans;
    }
    int solve3(string s) {
        unordered_map<char, int> pos;
        queue<char> q;
        for (int i = 0; i < s.size(); i++) {
            if (pos.find(s[i]) == pos.end()) { // not in pos
                pos[s[i]] = i;
                q.push(s[i]);
            }
            else {
                pos[s[i]] = -1;
                while (!q.empty() && pos[q.front()] == -1) q.pop(); // ensure q[0] is unique
            }
        }
        return q.empty() ? -1 : pos[q.front()];
    }
};
// @lc code=end

