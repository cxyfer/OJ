/*
 * @lc app=leetcode.cn id=2058 lang=cpp
 *
 * [2058] 找出临界点之间的最小和最大距离
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;

struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};
// @lcpr-template-end
// @lc code=start
class Solution {
public:
    vector<int> nodesBetweenCriticalPoints(ListNode* head) {
        ListNode *pre = nullptr, *cur = head;
        int first = -1, last = -1;
        int mn = INT_MAX; // min distance
        int idx = 0;
        while (cur && cur->next) {
            if (pre != nullptr && (pre->val < cur->val && cur->val > cur->next->val || pre->val > cur->val && cur->val < cur->next->val)) {
                if (first == -1) first = idx;
                else mn = min(mn, idx - last);
                last = idx;
            }
            pre = cur;
            cur = cur->next;
            idx++;
        }
        return mn != INT_MAX ? vector<int>{mn, last - first} : vector<int>{-1, -1};
    }
};
// @lc code=end