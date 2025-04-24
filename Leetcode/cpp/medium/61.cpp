/*
 * @lc app=leetcode.cn id=61 lang=cpp
 * @lcpr version=30204
 *
 * [61] 旋转链表
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};
// @lc code=start
class Solution {
public:
    ListNode* rotateRight(ListNode* head, int k) {
        if (!head) return head;

        // 計算 Linked List 的長度
        int n = 1;
        ListNode* tail = head;
        while (tail->next) {
            tail = tail->next;
            n++;
        }

        // 如果 k 為 0 或 n 為 1，則直接返回 head
        k %= n;
        if (k == 0 || n == 1) return head;

        // 將 Linked List 形成一個環
        tail->next = head;

        // 找到新的 tail
        for (int i = 0; i < n - k; i++)
            tail = tail->next;

        // 新的 head 是新的 tail 的下一個節點
        head = tail->next;

        // 斷開環
        tail->next = nullptr;

        return head;
    }
};
// @lc code=end



/*
// @lcpr case=start
// [1,2,3,4,5]\n2\n
// @lcpr case=end

// @lcpr case=start
// [0,1,2]\n4\n
// @lcpr case=end

 */

