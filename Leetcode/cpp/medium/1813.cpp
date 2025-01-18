/*
 * @lc app=leetcode.cn id=1813 lang=cpp
 *
 * [1813] 句子相似性 III
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution {
public:
    bool areSentencesSimilar(string sentence1, string sentence2) {
        vector<string> tokens1, tokens2;
        stringstream ss1(sentence1), ss2(sentence2);
        string token;
        while (ss1 >> token) tokens1.push_back(token);
        while (ss2 >> token) tokens2.push_back(token);
        if (tokens1.size() > tokens2.size()) swap(tokens1, tokens2);
        int n = tokens1.size(), m = tokens2.size();
        int i = 0, j = 0;
        while (i < n && tokens1[i] == tokens2[i]) i++;
        while (j < n - i && tokens1[n - 1 - j] == tokens2[m - 1 - j]) j++;
        return i + j == n;
    }
};
// @lc code=end

