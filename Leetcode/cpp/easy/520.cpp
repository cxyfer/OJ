/*
 * @lc app=leetcode.cn id=520 lang=cpp
 *
 * [520] 检测大写字母
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution1 {
public:
    bool detectCapitalUse(string word) {
        bool ck1 = true, ck2 = true, ck3 = true;
        for (int i = 0; i < word.size(); i++) {
            if (islower(word[i])) {
                ck1 = false;
                if (i == 0) ck3 = false;
            }
            else {
                ck2 = false;
                if (i > 0) ck3 = false;
            }
        }
        return ck1 || ck2 || ck3;
    }
};

class Solution2 {
public:
    bool detectCapitalUse(string word) {
        int cnt = 0;
        for (char ch : word) cnt += isupper(ch) ? 1 : 0;
        return cnt == 0 || cnt == word.size() || (cnt == 1 && isupper(word[0])); 
    }
};

// class Solution : public Solution1 {};
class Solution : public Solution2 {};
// @lc code=end

