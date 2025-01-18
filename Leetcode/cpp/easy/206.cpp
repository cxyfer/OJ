/*
 * @lc app=leetcode.cn id=206 lang=cpp
 *
 * [206] 反转链表
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
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
class Solution1 {
public:
    ListNode* reverseList(ListNode* head) {
        ListNode *cur = head, *pre = nullptr;
        while (cur != nullptr) {
            ListNode *tmp = cur->next; // Save next node
            cur->next = pre; // Reverse cur node
            pre = cur; // Move pre to cur
            cur = tmp; // Move cur to next node
        }
        return pre;
    }
};

class Solution2 {
public:
    ListNode* reverseList(ListNode* head) {
        ListNode *cur = head, *pre = nullptr;
        while (cur != nullptr) {
            ListNode *tmp = pre; // Save pre node
            pre = cur; // Move pre to cur, so pre is current node actually
            cur = cur->next; // Move cur to next node, so cur is next node actually
            pre->next = tmp; // Reverse cur node
        }
        return pre;
    }
};

class Solution3 {
public:
    ListNode* reverseList(ListNode* head) {
        if (head == nullptr || head->next == nullptr) return head;
        ListNode *last = reverseList(head->next);
        head->next->next = head;
        head->next = nullptr;
        return last;
    }
};

// class Solution : public Solution1 {};
// class Solution : public Solution2 {};
class Solution : public Solution3 {};
// @lc code=end
