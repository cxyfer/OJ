/*
 * @lc app=leetcode id=1634 lang=cpp
 *
 * [1634] Add Two Polynomials Represented as Linked Lists
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;

struct PolyNode {
    int coefficient, power;
    PolyNode *next;
    PolyNode(): coefficient(0), power(0), next(nullptr) {};
    PolyNode(int x, int y): coefficient(x), power(y), next(nullptr) {};
    PolyNode(int x, int y, PolyNode* next): coefficient(x), power(y), next(next) {};
};
// @lcpr-template-end
// @lc code=start
class Solution {
public:
    PolyNode* addPoly(PolyNode* poly1, PolyNode* poly2) {
        PolyNode* head = new PolyNode();
        PolyNode* cur = head;
        while (poly1 && poly2) {
            if (poly1->power > poly2->power) {
                cur->next = poly1;
                poly1 = poly1->next;
                cur = cur->next;
            } else if (poly1->power < poly2->power) {
                cur->next = poly2;
                poly2 = poly2->next;
                cur = cur->next;
            } else {
                int sum = poly1->coefficient + poly2->coefficient;
                if (sum != 0) {
                    cur->next = new PolyNode(sum, poly1->power);
                    cur = cur->next;
                }
                poly1 = poly1->next;
                poly2 = poly2->next;
            }
        }
        cur->next = poly1 ? poly1 : poly2;
        return head->next;
    }
};
// @lc code=end


