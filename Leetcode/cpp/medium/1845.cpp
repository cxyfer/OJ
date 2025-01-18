/*
 * @lc app=leetcode.cn id=1845 lang=cpp
 *
 * [1845] 座位预约管理系统
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class SeatManager {
public:
    priority_queue<int, vector<int>, greater<int>> hp;
    SeatManager(int n) {
        for (int i = 1; i <= n; i++) hp.push(i);
    }
    
    int reserve() {
        int t = hp.top();
        hp.pop();
        return t;
    }
    
    void unreserve(int seatNumber) {
        hp.push(seatNumber);
    }
};

/**
 * Your SeatManager object will be instantiated and called as such:
 * SeatManager* obj = new SeatManager(n);
 * int param_1 = obj->reserve();
 * obj->unreserve(seatNumber);
 */
// @lc code=end

