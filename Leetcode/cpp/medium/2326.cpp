/*
 * @lc app=leetcode.cn id=2326 lang=cpp
 *
 * [2326] 螺旋矩阵 IV
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
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
    vector<vector<int>> spiralMatrix(int m, int n, ListNode* head) {
        vector<pair<int, int>> DIR = {{0, 1}, {1, 0}, {0, -1}, {-1, 0}};
        vector<vector<int>> ans(m, vector<int>(n, -1));
        int x = 0, y = 0, cd = 0, nx, ny;
        while (head != nullptr) {
            ans[x][y] = head->val;
            head = head->next;
            nx = x + DIR[cd].first;
            ny = y + DIR[cd].second;
            if (nx < 0 || nx >= m || ny < 0 || ny >= n || ans[nx][ny] != -1) {
                cd = (cd + 1) % 4;
                nx = x + DIR[cd].first;
                ny = y + DIR[cd].second;
            }
            x = nx;
            y = ny;
        }
        return ans;
    }
};
// @lc code=end