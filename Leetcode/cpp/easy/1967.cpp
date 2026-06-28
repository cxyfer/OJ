/*
 * @lc app=leetcode id=1967 lang=cpp
 *
 * [1967] Number of Strings That Appear as Substrings in Word
 */

// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
constexpr int ALPH = 26;

class Solution1 {
public:
    int numOfStrings(vector<string>& patterns, string word) {
        int ans = 0;
        for (const auto& pattern : patterns) {
            if (word.contains(pattern)) {
                ans++;
            }
        }
        return ans;
    }
};

struct Node {
    array<Node*, ALPH> child;
    Node* fail;
    int cnt;
    Node() : fail(nullptr), cnt(0) {
        fill(child.begin(), child.end(), nullptr);
    }
};

class AhoCorasick {
public:
    Node* root;

    AhoCorasick() {
        root = new Node();
    }

    void insert(const string& word) {
        Node* node = root;
        for (char ch : word) {
            int idx = ch - 'a';
            if (node->child[idx] == nullptr) node->child[idx] = new Node();
            node = node->child[idx];
        }
        node->cnt += 1;
    }

    void build() {
        root->fail = root;
        // BFS
        queue<Node*> q;
        for (int i = 0; i < ALPH; ++i) {
            if (root->child[i] == nullptr) {
                root->child[i] = root;
            } else {
                root->child[i]->fail = root;
                q.push(root->child[i]);
            }
        }
        while (!q.empty()) {
            Node* u = q.front();
            q.pop();
            for (int i = 0; i < ALPH; ++i) {
                if (u->child[i] == nullptr) {
                    u->child[i] = u->fail->child[i];
                } else {
                    Node* v = u->child[i];
                    v->fail = u->fail->child[i];
                    q.push(v);
                }
            }
        }
    }
};

class Solution2 {
public:
    int numOfStrings(vector<string>& patterns, string word) {
        AhoCorasick ac;
        for (const auto& pattern : patterns) ac.insert(pattern);
        ac.build();

        int ans = 0;
        Node* node = ac.root;
        for (char ch : word) {
            // 由於是 Trie 圖，直接轉移即可
            int idx = ch - 'a';
            node = node->child[idx];

            // 沿著 fail 鏈向上搜集所有匹配的模式串
            Node* temp = node;
            while (temp != ac.root && temp->cnt != -1) {
                ans += temp->cnt;
                // 標記為 -1，代表此節點已被統計過，避免重複計算
                temp->cnt = -1;
                temp = temp->fail;
            }
        }
        return ans;
    }
};

// using Solution = Solution1;
using Solution = Solution2;
// @lc code=end
