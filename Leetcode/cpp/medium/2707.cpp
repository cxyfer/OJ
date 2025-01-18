/*
 * @lc app=leetcode.cn id=2707 lang=cpp
 *
 * [2707] 字符串中的额外字符
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution1 {
public:
    int minExtraChar(string s, vector<string>& dictionary) {
        int n = s.size();
        unordered_set<string> words(dictionary.begin(), dictionary.end());
        vector<int> memo(n, -1);
        function<int(int)> dfs = [&](int i) -> int {
            if (i >= n) return 0;
            int& res = memo[i];
            if (res != -1) return res;
            res = dfs(i + 1) + 1; // 不選，即第 i 個字元為獨立字元的情況
            for (int j = i; j < n; ++j) {
                if (words.count(s.substr(i, j - i + 1))) {
                    res = min(res, dfs(j + 1));
                }
            }
            return res;
        };
        return dfs(0);
    }
};

class TrieNode {
public:
    vector<TrieNode*> child;
    bool is_end;
    TrieNode() {
        child = vector<TrieNode*>(26, nullptr);
        is_end = false;
    }
};

class Solution2 {
public:
    int minExtraChar(string s, vector<string>& dictionary) {
        int n = s.size();

        TrieNode* root = new TrieNode();
        for (const string& word : dictionary) {
            TrieNode* node = root;
            for (char ch : word) {
                if (node->child[ch - 'a'] == nullptr) {
                    node->child[ch - 'a'] = new TrieNode();
                }
                node = node->child[ch - 'a'];
            }
            node->is_end = true;
        }

        vector<int> memo(n, -1);
        function<int(int)> dfs = [&](int i) -> int {
            if (i >= n) return 0;
            int& res = memo[i];
            if (res != -1) return res;
            res = dfs(i + 1) + 1; // 不選，即第 i 個字元為獨立字元的情況
            TrieNode* node = root;
            for (int j = i; j < n; ++j) {
                if (node->child[s[j] - 'a'] == nullptr) break; // 當前字元不在字典樹中，不用繼續往下找
                node = node->child[s[j] - 'a'];
                if (node->is_end) res = min(res, dfs(j + 1)); // 選，s[i:j+1] 在字典中
            }
            return res;
        };
        return dfs(0);
    }
};

class Solution: public Solution1 {};
// class Solution: public Solution2 {};
// @lc code=end