/*
 * @lc app=leetcode.cn id=412 lang=cpp
 * @lcpr version=30204
 *
 * [412] Fizz Buzz
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
const int MAX_N = 1e4 + 5;
vector<string> ans;
auto init = []() {
    for (int i = 1; i < MAX_N; i++) {
        bool flag1 = i % 3 == 0, flag2 = i % 5 == 0;
        if (flag1 && flag2) ans.push_back("FizzBuzz");
        else if (flag1) ans.push_back("Fizz");
        else if (flag2) ans.push_back("Buzz");
        else ans.push_back(to_string(i));
    }
    return 0;
}();

class Solution {
public:
    vector<string> fizzBuzz(int n) {
        return vector<string>(ans.begin(), ans.begin() + n);
    }
};
// @lc code=end



/*
// @lcpr case=start
// 3\n
// @lcpr case=end

// @lcpr case=start
// 5\n
// @lcpr case=end

// @lcpr case=start
// 15\n
// @lcpr case=end

 */

