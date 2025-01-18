/*
 * @lc app=leetcode.cn id=2024 lang=cpp
 *
 * [2024] 考试的最大困扰度
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution {
public:
    int maxConsecutiveAnswers(string answerKey, int k) {
        int n = answerKey.size();
        function<int(char)> helper = [&](char ch) {
            int left = 0, cnt = 0, res = 0;
            for (int right = 0; right < n; right++) {
                if (answerKey[right] == ch) cnt++;
                while (cnt > k) {
                    if (answerKey[left] == ch) cnt--;
                    left++;
                }
                res = max(res, right - left + 1);
            }
            return res;
        };
        return max(helper('T'), helper('F'));
    }
};
// @lc code=end

