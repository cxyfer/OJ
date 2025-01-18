/*
 * @lc app=leetcode.cn id=2813 lang=cpp
 *
 * [2813] 子序列最大优雅度
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution {
public:
    long long findMaximumElegance(vector<vector<int>>& items, int k) {
        int n = items.size();
        sort(items.begin(), items.end(), greater<vector<int>>());
        long long ans = 0, cur = 0, sz = 0;
        unordered_set<int> seen; // 已經出現過的種類
        vector<int> dulplicate; // 所有種類中，第二個以後的物品，利潤由大到小
        for (int i = 0; i < min(k, n); i++) { // 先加入前 k 個物品
            int profit = items[i][0], category = items[i][1];
            cur += profit;
            if (seen.count(category)) dulplicate.push_back(profit); // 重複的種類
            else seen.insert(category); // 新的種類
        }
        sz = seen.size();
        ans = cur + sz * sz; // 初始化答案為前 k 個物品的利潤 + 種類數量的平方
        for (int i = k; i < n; i++) {
            int profit = items[i][0], category = items[i][1];
            // 有新的種類，且之前有重複種類的物品，則取代最小的重複物品，嘗試看看會不會讓答案變大
            if (!dulplicate.empty() && !seen.count(category)) {
                seen.insert(category);
                cur += profit - dulplicate.back(); // 去除重複種類的物品中，利潤最小的
                dulplicate.pop_back();
            }
            sz = seen.size();
            ans = max(ans, cur + sz * sz); // 更新答案
        }
        return ans;
    }
};
// @lc code=end

int main() {
    Solution sol = Solution();
    int k; vector<vector<int>> items;
    items = {{3, 2}, {5, 1}, {10, 1}};
    k = 2;
    cout << sol.findMaximumElegance(items, k) << endl; // 17
    items = {{3, 1}, {3, 1}, {2, 2}, {5, 3}};
    k = 3;
    cout << sol.findMaximumElegance(items, k) << endl; // 19
    return 0;
}