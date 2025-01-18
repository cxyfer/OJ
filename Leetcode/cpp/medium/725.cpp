/*
 * @lc app=leetcode.cn id=725 lang=cpp
 *
 * [725] 分隔链表
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
class Solution {
public:
    vector<ListNode*> splitListToParts(ListNode* head, int k) {
        int cnt = 0;
        ListNode* cur = head, *tmp;
        while (cur != nullptr) {
            cnt++;  
            cur = cur->next;
        }
        int q = cnt / k, r = cnt % k, idx = 0, sz;
        vector<ListNode*> ans(k, nullptr);
        cur = head;
        while (idx < k && cur != nullptr) {
            ans[idx] = cur;
            sz = q + (idx++ < r ? 1 : 0);
            for (int i = 1; i < sz; ++i) cur = cur->next;
            tmp = cur->next; // backup of next node
            cur->next = nullptr; // break the link
            cur = tmp; // move to next node
        }
        return ans;        
    }
};
// @lc code=end

