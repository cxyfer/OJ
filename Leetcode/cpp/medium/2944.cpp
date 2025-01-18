/*
 * @lc app=leetcode.cn id=2944 lang=cpp
 *
 * [2944] 购买水果需要的最少金币数
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution1 {
public:
    int minimumCoins(vector<int>& prices) {
        int n = prices.size();
        vector<int> memo(n + 1, -1);
        function<int(int)> f = [&](int i) -> int {
            if (i * 2 >= n) return prices[i - 1];
            if (memo[i] != -1) return memo[i];
            int res = f(i * 2 + 1);
            for (int j = i + 1; j <= i * 2; j++) {
                res = min(res, f(j));
            }
            return memo[i] = prices[i - 1] + res;
        };
        return f(1);
    }
};

class Solution2 {
public:
    int minimumCoins(vector<int>& prices) {
        int n = prices.size();
        vector<int> f(n + 1, 0);
        for (int i = n; i >= 1; i--) {
            if (i * 2 >= n) f[i] = prices[i - 1];
            else {
                f[i] = prices[i - 1] + *min_element(f.begin() + i + 1, f.begin() + i * 2 + 2);
            }
        }
        return f[1];
    }
};

class Solution3 {
public:
    int minimumCoins(vector<int>& prices) {
        int n = prices.size();
        deque<pair<int, int>> dq; // (i, f[i]), f(i) 是單調遞減的
        for (int i = n; i >= 1; i--) {
            // 1. 彈出右側超過窗口範圍的元素
            while (!dq.empty() && dq.back().first > i * 2 + 1) {
                dq.pop_back();
            }
            // 2. 計算 f[i]
            int f = prices[i - 1] + (i * 2 >= n ? 0 : dq.back().second);
            // 3. 將 f[i] 插入到左側
            while (!dq.empty() && f <= dq.front().second) { // 彈出左側大於等於 f[i] 的元素
                dq.pop_front();
            }
            dq.push_front({i, f});
        }
        return dq.front().second;
    }
};
// class Solution : public Solution1 {};
// class Solution : public Solution2 {};
class Solution : public Solution3 {};
// @lc code=end

int main() {
    Solution sol = Solution();
    vector<int> prices;
    prices = {1,37,19,38,11,42,18,33,6,37,15,48,23,12,41,18,27,32};
    cout << sol.minimumCoins(prices) << endl;
    return 0;
}