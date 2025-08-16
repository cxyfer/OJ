/*
 * @lc app=leetcode.cn id=630 lang=cpp
 * @lcpr version=30204
 *
 * [630] 课程表 III
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution {
public:
    int scheduleCourse(vector<vector<int>>& courses) {
        ranges::sort(courses, [](vector<int>& a, vector<int>& b) {
            return a[1] < b[1];
        });
        priority_queue<int> pq;  // max heap
        int cur = 0;
        for (auto& course : courses) {
            int duration = course[0], last_day = course[1];
            if (cur + duration <= last_day) {
                cur += duration;
                pq.push(duration);
            }
            else if (!pq.empty() && duration < pq.top()) {
                cur -= pq.top(); pq.pop();
                cur += duration;
                pq.push(duration);
            }
        }
        return pq.size();
    }
};
// @lc code=end



/*
// @lcpr case=start
// [[100, 200], [200, 1300], [1000, 1250], [2000, 3200]]\n
// @lcpr case=end

// @lcpr case=start
// [[1,2]]\n
// @lcpr case=end

// @lcpr case=start
// [[3,2],[4,3]]\n
// @lcpr case=end

 */

