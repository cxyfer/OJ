/*
 * @lc app=leetcode.cn id=212 lang=cpp
 *
 * [212] 单词搜索 II
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Node {
public:
    vector<Node*> child;
    bool isEnd;
    string word;
    Node() {
        child = vector<Node*>(26, nullptr);
        isEnd = false;
        word = "";
    }
};

class Solution {
public:
    vector<string> findWords(vector<vector<char>>& board, vector<string>& words) {
        int m = board.size(), n = board[0].size();
        vector<int> dx = {0, 0, 1, -1}, dy = {1, -1, 0, 0};
        Node* root = new Node(); // Trie root
        for (auto& word : words) {
            Node* cur = root;
            for (char ch : word) {
                if (cur->child[ch - 'a'] == nullptr) {
                    cur->child[ch - 'a'] = new Node();
                }
                cur = cur->child[ch - 'a'];
            }
            cur->isEnd = true;
            cur->word = word;
        }
        vector<string> ans;
        function<void(int, int, Node*)> dfs = [&](int i, int j, Node* cur) {
            if (cur->isEnd) {
                ans.push_back(cur->word);
                cur->isEnd = false;
            }
            if (i < 0 || i >= m || j < 0 || j >= n) return; // out of bound
            char ch = board[i][j];
            if (ch == '#' || cur->child[ch - 'a'] == nullptr) return; // visited or no match
            board[i][j] = '#'; // mark visited
            for (int k = 0; k < 4; k++) {
                dfs(i + dx[k], j + dy[k], cur->child[ch - 'a']);
            }
            board[i][j] = ch; // backtracking
        };
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                dfs(i, j, root);
            }
        }
        return ans;
    }
};
// @lc code=end