/*
 * @lc app=leetcode id=1491 lang=cpp
 * @lcpr version=30111
 *
 * [1491] Average Salary Excluding the Minimum and Maximum Salary
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
const int INF = 0x3f3f3f3f;
class Solution {
public:
    double average(vector<int>& salary) {
        int n = salary.size();
        int s = 0, mx = -INF, mn = INF;
        for (int i = 0; i < n; i++) {
            s += salary[i];
            mx = max(mx, salary[i]);
            mn = min(mn, salary[i]);
        }
        return (s - mx - mn) * 1.0 / (n - 2);
    }
};
// @lc code=end
int main() {
    Solution sol = Solution();
    vector<int> salary1 = {4000,3000,1000,2000};
    cout << sol.average(salary1) << endl;
    vector<int> salary2 = {1000,2000,3000};
    cout << sol.average(salary2) << endl;
    return 0;
}