/*
 * @lc app=leetcode.cn id=2517 lang=cpp
 *
 * [2517] 礼盒的最大甜蜜度
 */

// @lc code=start
class Solution {
public:
    int maximumTastiness(vector<int>& price, int k) {
        int n = price.size();
        sort(price.begin(), price.end());

        auto check = [&](int d) {
            int cnt = 1;
            int pre = price[0];
            for (int i = 1; i < n; ++i) {
                if (price[i] - pre >= d) {
                    cnt++;
                    pre = price[i];
                }
            }
            return cnt >= k;
        };

        int left = 0, right = price[n - 1] - price[0];
        while (left <= right) {
            int mid = (left + right) / 2;
            if (check(mid)) {
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }
        return right;
    }
};
// @lc code=end

