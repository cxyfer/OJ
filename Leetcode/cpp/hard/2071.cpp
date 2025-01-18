/*
 * @lc app=leetcode.cn id=2071 lang=cpp
 *
 * [2071] 你可以安排的最多任务数目
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution {
public:
    /*
        Binary Search + Greedy + Deque
        二分檢查是否可以完成 k 個任務，若滿足，則顯然是要求最低的 k 個任務。
        從需求最高的任務開始考慮，貪心思路如下：
            1. 如果有人不吃藥就能完成任務，那麽選擇體力最大的 worker 完成任務。
                因為其一定能完成所有任務，讓他完成要求最高的任務比較划算。
            2. 如果都需要吃藥才能完成任務，那麽選擇體力最小的 worker 吃藥完成任務。
                因為其他 worker 可能可以不吃藥完成要求更低的任務。
    */
    int maxTaskAssign(vector<int>& tasks, vector<int>& workers, int pills, int strength) {
        int m = tasks.size(), n = workers.size();
        sort(tasks.begin(), tasks.end());
        sort(workers.begin(), workers.end());

        auto check = [&] (int k) { // 檢查是否可以完成要求最低的 k 個任務
            int p = pills;
            int idx = n - 1;
            deque<int> dq; // 維護吃藥後可以完成當前任務的 worker，由體力大到小排序
            for (int j = k - 1; j >= 0; --j) {
                while (idx >= 0 && workers[idx] + strength >= tasks[j]) {
                    dq.push_back(workers[idx--]);
                }
                if (dq.empty()) return false; // 沒人可以完成當前任務
                if (dq.front() >= tasks[j]) dq.pop_front(); // 有人不用吃藥，就可以完成當前任務，此時選擇體力最大的 worker
                else { // deque 中所有人都需要吃藥才能完成當前任務，此時選擇體力最小的 worker
                    if (p-- > 0) dq.pop_back();
                    else return false; // 沒有藥了
                }
            }
            return true;
        };
        
        int left = 0, right = min(m, n), mid;
        while (left <= right) {
            mid = left + (right - left) / 2;
            if (check(mid)) left = mid + 1;
            else right = mid - 1;
        }
        return right;
    }
};
// @lc code=end

