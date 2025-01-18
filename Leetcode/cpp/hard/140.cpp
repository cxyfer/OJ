/*
 * @lc app=leetcode.cn id=140 lang=cpp
 *
 * [140] 单词拆分 II
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution1 {
public:
    int n;
    unordered_map<int, vector<string>> memo; // Memoization
    unordered_set<string> wordSet;
    vector<string> wordBreak(string s, vector<string>& wordDict) {
        n = s.size();
        for (string& word : wordDict) wordSet.insert(word);
        return dfs(0, s);
    }
    vector<string> dfs(int i, string &s) { // 返回 s[i:] 的所有可能劃分
        if (i == n) return {""};
        if (memo.count(i)) return memo[i];
        vector<string> res;
        for (int j = i; j < n; j++) { // 枚舉當前單字的結尾位置
            string word = s.substr(i, j - i + 1);
            if (wordSet.count(word)) { 
                vector<string> sentences = dfs(j + 1, s);
                for (string& st : sentences) {
                    res.push_back(word + (st.empty() ? "" : " ") + st);
                }
            }
        }
        return memo[i] = res;
    }
};

class Node { // Trie Node
public:
    vector<Node*> children;
    bool isEnd;
    Node() : children(26), isEnd(false) {}
};
class Solution2 {
public:
    int n;
    string s;
    Node* root = new Node(); // Trie
    vector<string> ans;
    vector<string> wordBreak(string s, vector<string>& wordDict) {
        n = s.size();
        this->s = s;
        for (string& word : wordDict) {
            Node* cur = root;
            for (char ch : word) {
                int idx = ch - 'a';
                if (cur->children[idx] == nullptr) {
                    cur->children[idx] = new Node();
                }
                cur = cur->children[idx];
            }
            cur->isEnd = true; // 標記當前 Trie 節點是某個單字的結尾
        }
        dfs(0, root, "", "");
        return ans;
    }
    void dfs(int i, Node* cur, string word, string path) { // Backtracking
        if (i == n) {
            if (cur == root) ans.push_back(path);
            return;
        }
        if (!cur->children[s[i]-'a']) return; // 如果當前字元不在 Trie 中，則直接返回 (剪枝)
        word += s[i]; // 當前字元加入 word
        Node* nxt = cur->children[s[i]-'a'];
        dfs(i + 1, nxt, word, path); // 不劃分，繼續往下找
        if (nxt->isEnd) { // 當前字元是單字的結尾，可以劃分
            path += (path.empty() ? "" : " ") + word;
            dfs(i + 1, root, "", path); // 劃分，繼續從 Trie 的根節點開始
        }
    }
};

class Solution3 {
public:
    vector<string> wordBreak(string s, vector<string>& wordDict) {
        int n = s.size();
        unordered_set<string> wordSet(wordDict.begin(), wordDict.end());
        vector<string> ans;
        for (int i = 0; i < (1 << (n - 1)); i++) {
            string res = "";
            int k = -1;
            bool valid = true;
            for (int j = 0; j < n && valid; j++) {
                res += s[j];
                if (i & (1 << j) || j == n - 1) {
                    if (!wordSet.count(res.substr(k + 1))){
                        valid = false;
                        break;
                    }
                    if (j != n - 1) res += " ";
                    k = res.size() - 1;
                }
            }
            if (valid) ans.push_back(res);
        }
        return ans;
    }
};
// class Solution : public Solution1 {};
// class Solution : public Solution2 {};
class Solution : public Solution3 {};
// @lc code=end

