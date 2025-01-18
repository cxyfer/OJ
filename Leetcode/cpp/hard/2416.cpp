/*
 * @lc app=leetcode.cn id=2416 lang=cpp
 *
 * [2416] 字符串的前缀分数和
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class TrieNode {
public:
    vector<TrieNode*> child;
    // TrieNode* child[26];
    int cnt;
    TrieNode() {
        child = vector<TrieNode*>(26, nullptr);
        // memset(child, 0, sizeof(child));
        // for (int i = 0; i < 26; i++) child[i] = nullptr;
        cnt = 0;
    }
};

class Solution {
public:
    vector<int> sumPrefixScores(vector<string>& words) {
        int n = words.size();

        TrieNode* root = new TrieNode();
        for (const string& word : words) {
            TrieNode* node = root;
            for (char ch : word) {
                int idx = ch - 'a';
                if (node->child[idx] == nullptr) {
                    node->child[idx] = new TrieNode();
                }
                node = node->child[idx];
                node->cnt++;
            }
        }

        vector<int> ans(n, 0);
        for (int i = 0; i < n; ++i) {
            TrieNode* node = root;
            int score = 0;
            for (char ch : words[i]) {
                node = node->child[ch - 'a'];
                score += node->cnt;
            }
            ans[i] = score;
        }
        return ans;
    }
};
// @lc code=end

int main() {
    Solution sol = Solution();
    vector<string> words = {"abc", "ab", "bc", "b"};
    vector<int> ans = sol.sumPrefixScores(words);
    for (int score : ans) {
        cout << score << " ";
    }
    cout << endl;
    return 0;
}