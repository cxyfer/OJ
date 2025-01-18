/*
 * @lc app=leetcode.cn id=3043 lang=cpp
 *
 * [3043] 最长公共前缀的长度
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class TrieNode {
public:
    vector<TrieNode*> child;
    int depth;
    TrieNode() {
        child = vector<TrieNode*>(10, nullptr);
        depth = 0;
    }
};

class Solution {
public:
    int longestCommonPrefix(vector<int>& arr1, vector<int>& arr2) {
        TrieNode* root = new TrieNode();
        for (int x : arr1) {
            TrieNode* node = root;
            auto digits = num_to_list(x);
            for (int d : digits) {
                if (node->child[d] == nullptr) {
                    node->child[d] = new TrieNode();
                    node->child[d]->depth = node->depth + 1;
                }
                node = node->child[d];
            }
        }
        int ans = 0;
        for (int x : arr2) {
            TrieNode* node = root;
            auto digits = num_to_list(x);
            for (int d : digits) {
                if (node->child[d] == nullptr) {
                    break;
                }
                ans = max(ans, node->child[d]->depth);
                node = node->child[d];
            }
        }
        return ans;
    }
    vector<int> num_to_list(int x) {
        vector<int> res;
        while (x > 0) {
            res.push_back(x % 10);
            x /= 10;
        }
        reverse(res.begin(), res.end());
        return res;
    }
};
// @lc code=end

