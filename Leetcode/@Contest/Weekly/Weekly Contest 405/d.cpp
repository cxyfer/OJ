#include <bits/stdc++.h>
using namespace std;

class Node {
public:
    vector<Node*> child;
    bool isEnd;
    int cost;
    Node() {
        child = vector<Node*>(26, nullptr);
        isEnd = false;
        cost = INT_MAX / 2;
    }
};

class Solution {
public:
    int minimumCost(string target, vector<string>& words, vector<int>& costs) {
        Node *trie = new Node();
        for (int i = 0; i < words.size(); i++) {
            Node *node = trie;
            for (int j = words[i].size() - 1; j >= 0; j--) {
                int idx = words[i][j] - 'a';
                if (node->child[idx] == nullptr) {
                    node->child[idx] = new Node();
                }
                node = node->child[idx];
            }
            node->isEnd = true;
            node->cost = min(node->cost, costs[i]);
        }

        vector<int> dp(target.size() + 1, INT_MAX / 2);
        dp[0] = 0;
        for (int i = 1; i <= target.size(); i++) {
            Node *cur = trie;
            for (int j = i - 1; j >= 0; j--) {
                int idx = target[j] - 'a';
                if (cur->child[idx] == nullptr) {
                    break;
                }
                cur = cur->child[idx];
                if (cur->isEnd) {
                    dp[i] = min(dp[i], dp[j] + cur->cost);
                }
            }
        }
        return dp[target.size()] == INT_MAX / 2 ? -1 : dp[target.size()];
    }
};