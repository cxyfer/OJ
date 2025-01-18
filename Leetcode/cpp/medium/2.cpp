/*
 * @lc app=leetcode id=2 lang=cpp
 * @lcpr version=30112
 *
 * [2] Add Two Numbers
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
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode head = ListNode(0);
        ListNode *p = &head;
        int carry=0;
        while(l1 || l2 || carry){
            int val = 0;
            if (l1){
                val += l1->val;
                l1 = l1->next;
            }
            if (l2){
                val += l2->val;
                l2 = l2->next;
            }
            val += carry;
            carry = val/10;
            p->next = new ListNode(val%10);
            p = p->next;
        }
        return head.next;
    }
};
// @lc code=end



/*
// @lcpr case=start
// [2,4,3]\n[5,6,4]\n
// @lcpr case=end

// @lcpr case=start
// [0]\n[0]\n
// @lcpr case=end

// @lcpr case=start
// [9,9,9,9,9,9,9]\n[9,9,9,9]\n
// @lcpr case=end

 */

