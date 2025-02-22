/*
 * @lc app=leetcode id=1206 lang=cpp
 *
 * [1206] Design Skiplist
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
mt19937 gen;
uniform_int_distribution<> dis;

struct Node {
    int val;
    Node* next;
    Node* down;
};

class Skiplist {
private:
    Node* head;
    const int MAX_LVL = 15;
    const double P = 0.5;

    int get_random_level() {
        int lvl = 1;
        while (dis(gen) < P && lvl < MAX_LVL)
            lvl++;
        return lvl;
    }

public:
    Skiplist() {
        head = new Node{-1, nullptr, nullptr};
    }
    
    bool search(int target) {
        Node* curr = head;
        while (curr) {
            while (curr->next && curr->next->val < target)
                curr = curr->next;
            if (curr->next && curr->next->val == target)
                return true;
            curr = curr->down;
        }
        return false;
    }
    
    void add(int num) {
        vector<Node*> st;
        Node* curr = head;
        while (curr) {
            while (curr->next && curr->next->val < num)
                curr = curr->next;
            st.push_back(curr);
            curr = curr->down;
        }
        int lvl = get_random_level();
        Node* down = nullptr;
        while (lvl > 0 && st.size()) {
            Node* prev = st.back();
            st.pop_back();
            Node* new_node = new Node{num, prev->next, down};
            prev->next = new_node;
            down = new_node;
            lvl--;
        }
        while (lvl > 0) {
            Node* new_node = new Node{num, nullptr, down};
            head = new Node{-1, new_node, head};
            down = new_node;
            lvl--;
        }
    }
    
    bool erase(int num) {
        Node* curr = head;
        bool res = false;
        while (curr) {
            while (curr->next && curr->next->val < num)
                curr = curr->next;
            if (curr->next && curr->next->val == num) {
                res = true;
                curr->next = curr->next->next;
            }
            curr = curr->down;
        }
        return res;
    }
};
// @lc code=end

