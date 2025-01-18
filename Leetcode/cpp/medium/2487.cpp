/*
 * @lc app=leetcode id=2487 lang=cpp
 * @lcpr version=30122
 *
 * [2487] Remove Nodes From Linked List
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
    ListNode* removeNodes(ListNode* head) {
        if (head->next == nullptr) {
            return head;
        }
        ListNode* node = removeNodes(head->next); // 剩下裡面最大的
        if (node->val > head->val) { // 刪除 head
            return node;
        }
        head->next = node; // 不刪除 head
        return head;
    }
};
// @lc code=end



/*
// @lcpr case=start
// [5,2,13,3,8]\n
// @lcpr case=end

// @lcpr case=start
// [1,1,1,1]\n
// @lcpr case=end

 */

