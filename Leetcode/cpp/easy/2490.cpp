/*
 * @lc app=leetcode.cn id=2490 lang=cpp
 *
 * [2490] 回环句
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution1 {
public:
    bool isCircularSentence(string sentence) {
        stringstream ss(sentence);
        string word;
        vector<string> words;
        while (ss >> word) {
            words.push_back(word);
        }
        int n = words.size();
        for (int i = 0; i < n; ++i) {
            if (words[i].back() != words[(i + 1) % n].front()) {
                return false;
            }
        }
        return true;
    }
};

class Solution2 {
public:
    bool isCircularSentence(string sentence) {
        int n = sentence.size();
        for (int i = 0; i < n; i++) {
            if (sentence[i] == ' ' and sentence[i - 1] != sentence[i + 1]) {
                return false;
            }
        }
        return sentence.front() == sentence.back();
    }
};

// class Solution : public Solution1 {};
class Solution : public Solution2 {};
// @lc code=end

