/*
 * @lc app=leetcode.cn id=2181 lang=cpp
 *
 * [2181] 合并零之间的节点
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;

struct ListNode {
    int val;
    ListNode* next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode* next) : val(x), next(next) {}
};
// @lcpr-template-end
// @lc code=start
class Solution {
public:
    ListNode* mergeNodes(ListNode* head) {
        ListNode *pre = head, *cur = head->next;
        int s = 0;
        while (cur != nullptr) {
            if (cur->val == 0) {
                cur->val = s;
                s = 0;
                pre->next = cur;
                pre = cur;
            } else {
                s += cur->val;
            }
            cur = cur->next;
        }
        return head->next;
    }
};
// @lc code=end
