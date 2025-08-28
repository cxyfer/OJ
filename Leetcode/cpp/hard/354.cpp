/*
 * @lc app=leetcode id=354 lang=cpp
 * @lcpr version=30112
 *
 * [354] Russian Doll Envelopes
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution {
public:
    int maxEnvelopes(vector<vector<int>>& envelopes) {
        sort(envelopes.begin(), envelopes.end(), [](const vector<int>& a, const vector<int>& b) {
            if (a[0] == b[0]) return a[1] > b[1];
            return a[0] < b[0];
        });
        vector<int> f;
        for (auto& e : envelopes) {
            auto it = lower_bound(f.begin(), f.end(), e[1]);
            if (it == f.end()) f.push_back(e[1]);
            else *it = e[1];
        }
        return f.size();
    }
};
// @lc code=end
int main() {
    Solution sol = Solution();
    vector<vector<int>> envelopes1 = {{5,4},{6,4},{6,7},{2,3}}; // 3
    cout << sol.maxEnvelopes(envelopes1) << endl;
    vector<vector<int>> envelopes2 = {{1,1},{1,1},{1,1}}; // 1
    cout << sol.maxEnvelopes(envelopes2) << endl;
    return 0;
}


/*
// @lcpr case=start
// [[5,4],[6,4],[6,7],[2,3]]\n
// @lcpr case=end

// @lcpr case=start
// [[1,1],[1,1],[1,1]]\n
// @lcpr case=end

 */

