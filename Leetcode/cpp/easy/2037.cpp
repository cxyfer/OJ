/*
 * @lc app=leetcode.cn id=2037 lang=cpp
 *
 * [2037] 使每位学生都有座位的最少移动次数
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
const int N = 101;

class Solution {
public:
    int minMovesToSeat(vector<int>& seats, vector<int>& students) {
        int n = seats.size(), ans = 0;
        countingSort(seats);
        countingSort(students);
        // sort(seats.begin(), seats.end());
        // sort(students.begin(), students.end());
        for (int i = 0; i < n; i++) {
            ans += abs(seats[i] - students[i]);
        }
        return ans;
    }
    void countingSort(vector<int>& arr) {
        int n = arr.size();
        vector<int> cnt(N, 0);
        for (int i = 0; i < n; i++) {
            cnt[arr[i]]++;
        }
        int idx = 0;
        for (int i = 0; i < N; i++) {
            while (cnt[i]--) {
                arr[idx++] = i;
            }
        }
        return;
    }
};
// @lc code=end

