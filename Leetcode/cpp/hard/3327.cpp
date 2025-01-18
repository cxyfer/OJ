/*
 * @lc app=leetcode.cn id=3327 lang=cpp
 *
 * [3327] 判断 DFS 字符串是否是回文串
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Manacher {
public:
    string s, t;
    vector<int> halfLen;
    int max_i;
    Manacher(string s) {
        this->s = s;
        t = "^";
        for (char ch : s) {
            t += "#";
            t += ch;
        }
        t += "#$";

        halfLen.resize(t.size() - 2, 0);
        halfLen[1] = 1;
        int boxM = 0, boxR = 0, hl = 1;
        max_i = 0;
        for (int i = 2; i < halfLen.size(); i++) {
            hl = 1;
            if (i < boxR) {
                hl = min(halfLen[boxM * 2 - i], boxR - i);
            }
            while (t[i - hl] == t[i + hl]) {
                hl++;
                boxM = i;
                boxR = i + hl;
            }
            halfLen[i] = hl;
            if (hl > halfLen[max_i]) {
                max_i = i;
            }
        }
    }

    // 判斷 [l, r) 是否為回文字串
    bool isPalindrome(int l, int r) {
        return halfLen[l + r + 1] > r - l;
    }
};

class Solution {
public:
    vector<bool> findAnswer(vector<int>& parent, string s) {
        int n = parent.size();
        vector<vector<int>> g(n);
        for (int i = 1; i < n; i++) {
            g[parent[i]].push_back(i);
        }

        string dfsStr = "";
        vector<pair<int, int>> nodes(n);
        int time = 0;
        auto dfs = [&](auto&& dfs, int x) -> void {
            nodes[x].first = time;
            for (int y : g[x]) {
                dfs(dfs, y);
            }
            dfsStr += s[x];
            time++;
            nodes[x].second = time;
        };
        dfs(dfs, 0);

        Manacher manacher(dfsStr);
        vector<bool> ans(n);
        for (int i = 0; i < n; i++) {
            ans[i] = manacher.isPalindrome(nodes[i].first, nodes[i].second);
        }
        return ans;
    }
};
// @lc code=end