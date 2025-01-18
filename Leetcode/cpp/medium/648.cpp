/*
 * @lc app=leetcode.cn id=648 lang=cpp
 *
 * [648] 单词替换
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution1 {
public:
    string replaceWords(vector<string>& dictionary, string sentence) {
        int n = sentence.size(), i = 0, st;
        unordered_set<string> dict;
        for (auto& word : dictionary) dict.insert(word);
        string ans, word;
        // 分組循環
        while (i < n) {
            st = i;
            while (i < n && sentence[i] != ' ') i++;
            word = sentence.substr(st, i - st);
            i++;
            // Process word
            for (int j = 1; j <= word.size(); j++) {
                if (dict.count(word.substr(0, j))) {
                    word = word.substr(0, j);
                    break;
                }
            }
            if (ans.empty()) ans = word;
            else ans += " " + word;
        }
        return ans;
    }
};

class Node { // Trie
public:
    Node* child[26];
    bool isEnd;
    Node() {
        memset(child, 0, sizeof(child));
        isEnd = false;
    }
};

class Solution2 {
public:
    string replaceWords(vector<string>& dictionary, string sentence) {
        Node *root = new Node();
        for (auto& word : dictionary) {
            Node* cur = root;
            for (auto& ch : word) {
                if (!cur->child[ch - 'a']) cur->child[ch - 'a'] = new Node();
                cur = cur->child[ch - 'a'];
            }
            cur->isEnd = true;
        }
        int n = sentence.size(), i = 0, st;
        string ans, word;
        while (i < n) {
            st = i;
            while (i < n && sentence[i] != ' ') i++;
            word = sentence.substr(st, i - st);
            i++;
            // Process word
            Node* cur = root;
            for (int j = 0; j < word.size(); j++) {
                if (!cur->child[word[j] - 'a']) break;
                cur = cur->child[word[j] - 'a'];
                if (cur->isEnd) {
                    word = word.substr(0, j + 1);
                    break;
                }
            }
            if (ans.empty()) ans = word;
            else ans += " " + word;
        }
        return ans;
    }
};

// class Solution : public Solution1 {};
class Solution : public Solution2 {};
// @lc code=end

