/*
 * @lc app=leetcode.cn id=2288 lang=cpp
 *
 * [2288] 价格减免
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution {
public:
    string discountPrices(string sentence, int discount) {
        double d = 1 - discount / 100.0;
        stringstream ssin(sentence), ssout;
        string w, ans;
        while (ssin >> w) {
            if (!ans.empty()) ans += ' ';
            if (w.length() > 1 && w[0] == '$' && all_of(w.begin() + 1, w.end(), ::isdigit)) {
                ssout.str(""); // clear
                ssout << fixed << setprecision(2) << '$' << stoll(w.substr(1)) * d;
                ans += ssout.str();
            } else {
                ans += w;
            }
        }
        return ans;
    }
};
// @lc code=end

// class Solution:
//     def discountPrices(self, sentence: str, discount: int) -> str:
//         ans = sentence.split()
//         for i, s in enumerate(ans):
//             if s[0] == '$' and s[1:].isdigit():
//                 price = int(s[1:]) * (100 - discount) / 100
//                 ans[i] = "$" + f"{price:.2f}"
//         return " ".join(ans)