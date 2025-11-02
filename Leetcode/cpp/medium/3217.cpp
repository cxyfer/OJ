/*
 * @lc app=leetcode.cn id=3217 lang=cpp
 * @lcpr version=30204
 *
 * [3217] 从链表中移除在数组中存在的节点
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
    ListNode* modifiedList(vector<int>& nums, ListNode* head) {
        unordered_set<int> st(nums.begin(), nums.end());
        ListNode* dummy = new ListNode(0, head);
        ListNode* prev = dummy, *curr = head;
        while (curr != nullptr) {
            if (st.count(curr->val))
                prev->next = curr->next;
            else
                prev = curr;
            curr = curr->next;
        }
        return dummy->next;
    }
};
// @lc code=end



/*
// @lcpr case=start
// [1,2,3]\n[1,2,3,4,5]\n
// @lcpr case=end

// @lcpr case=start
// [1]\n[1,2,1,2,1,2]\n
// @lcpr case=end

// @lcpr case=start
// [5]\n[1,2,3,4]\n
// @lcpr case=end

 */

