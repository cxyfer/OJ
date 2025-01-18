/*
 * @lc app=leetcode.cn id=676 lang=cpp
 *
 * [676] 实现一个魔法字典
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Trie {
public:
    bool is_end;
    vector<Trie*> child;
    Trie() : is_end(false), child(vector<Trie*>(26, nullptr)) {}
};

class MagicDictionary {
public:
    Trie* root;
    MagicDictionary() {
        root = new Trie();
    }
    
    void buildDict(vector<string> dictionary) {
        for (string& word : dictionary) {
            Trie* node = root;
            for (char& ch : word) {
                if (node->child[ch - 'a'] == nullptr)
                    node->child[ch - 'a'] = new Trie();
                node = node->child[ch - 'a'];
            }
            node->is_end = true;
        }
    }
    
    bool search(string searchWord) {
        function<bool(Trie*, int, bool)> dfs = [&](Trie* node, int i, bool modified) {
            if (i == searchWord.size()) return modified && node->is_end;
            int ch = searchWord[i] - 'a';
            if (node->child[ch] != nullptr) { // 不修改當前位置的字母
                if (dfs(node->child[ch], i + 1, modified)) return true;
            }
            if (!modified) { // 嘗試修改當前位置的字母，但只能修改一次
                for (int j = 0; j < 26; j++) {
                    if (j == ch || node->child[j] == nullptr) continue;
                    if (dfs(node->child[j], i + 1, true)) return true;
                }
            }
            return false;
        };
        return dfs(root, 0, false);
    }
};

/**
 * Your MagicDictionary object will be instantiated and called as such:
 * MagicDictionary* obj = new MagicDictionary();
 * obj->buildDict(dictionary);
 * bool param_2 = obj->search(searchWord);
 */
// @lc code=end

