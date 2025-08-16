/*
 * @lc app=leetcode id=253 lang=cpp
 *
 * [253] Meeting Rooms II
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
#include <ranges>

class Solution1 {
public:
    int minMeetingRooms(vector<vector<int>>& intervals) {
        map<int, int> diff;
        for (auto& interval : intervals) {
            diff[interval[0]]++;
            diff[interval[1]]--;
        }
        int ans = 0;
        int s = 0;
        for (auto& [_, d] : diff) {
            s += d;
            ans = max(ans, s);
        }
        return ans;
    }
};

class Solution2 {
public:
    int minMeetingRooms(vector<vector<int>>& intervals) {
        ranges::sort(intervals, [](const vector<int>& a, const vector<int>& b) {
            return a[0] < b[0];
        });
        int ans = 0;
        priority_queue<int, vector<int>, greater<int>> pq;  // Min heap
        for (auto& interval : intervals) {
            while (!pq.empty() && pq.top() <= interval[0])
                pq.pop();
            pq.push(interval[1]);
            ans = max(ans, static_cast<int>(pq.size()));
        }
        return ans;
    }
};

// using Solution = Solution1;
using Solution = Solution2;
// @lc code=end

