/*
 * @lc app=leetcode.cn id=2187 lang=cpp
 *
 * [2187] 完成旅途的最少时间
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution {
public:
    long long minimumTime(vector<int>& time, int totalTrips) {
        function<bool(long long)> check = [&](long long t) -> bool {
            long long sum = 0;
            for (int x : time) {
                sum += t / x;
            }
            return sum >= totalTrips;
        };
        long long left = 1;
        long long right = (long long) *min_element(time.begin(), time.end()) * totalTrips;
        while (left <= right) {
            long long mid = (left + right) / 2;
            if (check(mid)) {
                right = mid - 1;
            } else {
                left = mid + 1;
            }
        }
        return left;
    }
};
// @lc code=end

int main() {
    Solution sol = Solution();
    vector<int> time = {10000};
    int totalTrips = 10000000;
    cout << sol.minimumTime(time, totalTrips) << endl;
    return 0;
}