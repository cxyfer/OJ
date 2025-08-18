/*
 * @lc app=leetcode.cn id=679 lang=cpp
 * @lcpr version=30204
 *
 * [679] 24 点游戏
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
#include <ranges>
constexpr double EPS = 1e-6;
vector<function<double(double, double)>> OPS = {
    plus<double>(),
    minus<double>(),
    multiplies<double>(),
    divides<double>(),
    [](double x, double y) -> double { return y - x; },
    [](double x, double y) -> double { return y / x; }
};
class Solution {
public:
    bool judgePoint24(vector<int>& nums) {
        auto cards = nums | ranges::to<vector<double>>();
        auto dfs = [&](this auto&& dfs) -> bool {
            if (cards.size() == 1)
                return abs(cards[0] - 24) < EPS;
            for (int i = 0; i < cards.size(); ++i) {
                double x = cards[i];
                cards.erase(cards.begin() + i);
                for (int j = 0; j < i; ++j) {
                    double y = cards[j];
                    for (int k = 0; k < OPS.size(); ++k) {
                        if ((k == 3 && abs(y) < EPS) || (k == 5 && abs(x) < EPS))
                            continue;
                        cards[j] = OPS[k](x, y);
                        if (dfs())
                            return true;
                    }
                    cards[j] = y;
                }
                cards.insert(cards.begin() + i, x);
            }
            return false;
        };
        return dfs();
    }
};
// @lc code=end

int main() {
    Solution sol = Solution();
    vector<int> cards = {8, 1, 6, 6};
    cout << sol.judgePoint24(cards) << endl;  // true
    return 0;
}


/*
// @lcpr case=start
// [4, 1, 8, 7]\n
// @lcpr case=end

// @lcpr case=start
// [1, 2, 1, 2]\n
// @lcpr case=end

 */

