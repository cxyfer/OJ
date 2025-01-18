/*
 * @lc app=leetcode.cn id=1157 lang=cpp
 *
 * [1157] 子数组中占绝大多数的元素
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class MajorityChecker {
public:
    int k = 20;
    vector<int> arr;
    unordered_map<int, vector<int>> pos;

    MajorityChecker(vector<int>& arr) {
        this->arr = arr;
        srand(time(NULL)); // Seed the random number generator with current time
        for (int i = 0; i < arr.size(); i++) {
            pos[arr[i]].push_back(i);
        }
    }
    
    int query(int left, int right, int threshold) {
        int idx, x, cnt, ln = right - left + 1;
        for (int i = 0; i < k; i++) {
            x = arr[left + rand() % ln];
            const auto &v = pos[x];
            cnt = lower_bound(v.begin(), v.end(), right + 1) - lower_bound(v.begin(), v.end(), left);
            if (cnt >= threshold) {
                return x;
            }
            else if (cnt * 2 >= ln) {
                return -1;
            }
        }
        return -1;
    }
};

/**
 * Your MajorityChecker object will be instantiated and called as such:
 * MajorityChecker* obj = new MajorityChecker(arr);
 * int param_1 = obj->query(left,right,threshold);
 */
// @lc code=end

