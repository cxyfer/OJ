/*
 * @lc app=leetcode.cn id=290 lang=cpp
 * @lcpr version=30201
 *
 * [290] 单词规律
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start

// class Solution:
//     def wordPattern(self, pattern: str, s: str) -> bool:
//         ch2word, word2ch = dict(), dict()
//         words = s.split()
//         if len(pattern) != len(words):
//             return False
//         for ch, word in zip(pattern, words):
//             if word in word2ch and word2ch[word] != ch:
//                 return False
//             if ch in ch2word and ch2word[ch] != word:
//                 return False
//             word2ch[word] = ch
//             ch2word[ch] = word
//         return True
class Solution {
public:
    bool wordPattern(string pattern, string s) {
        unordered_map<char, string> ch2word;
        unordered_map<string, char> word2ch;
        vector<string> words;
        stringstream ss(s);
        string word;
        while (ss >> word) {
            words.push_back(word);
        }
        if (pattern.size() != words.size()) return false;
        for (int i = 0; i < pattern.size(); i++) {
            if (word2ch.count(words[i]) && word2ch[words[i]] != pattern[i]) {
                return false;
            }
            if (ch2word.count(pattern[i]) && ch2word[pattern[i]] != words[i]) {
                return false;
            }
            word2ch[words[i]] = pattern[i];
            ch2word[pattern[i]] = words[i];
        }
        return true;
    }
};
// @lc code=end



/*
// @lcpr case=start
// "abba"\n"dog cat cat dog"\n
// @lcpr case=end

// @lcpr case=start
// "abba"\n"dog cat cat fish"\n
// @lcpr case=end

// @lcpr case=start
// "aaaa"\n"dog cat cat dog"\n
// @lcpr case=end

 */

