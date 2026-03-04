/*
 * @lc app=leetcode.cn id=146 lang=cpp
 * @lcpr version=30204
 *
 * [146] LRU 缓存
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
struct Node {
    int key, value;
    Node *prev, *next;
    Node(int key = 0, int value = 0)
        : key(key), value(value), prev(nullptr), next(nullptr) {}
};

class LRUCache {
public:
    int capacity, size;
    Node* dummy;
    unordered_map<int, Node*> cache;
    LRUCache(int capacity) {
        this->capacity = capacity;
        size = 0;
        dummy = new Node(-1, -1);
        dummy->prev = dummy;
        dummy->next = dummy;
    }

    int get(int key) {
        if (cache.find(key) == cache.end()) return -1;
        Node* node = cache[key];
        moveToHead(node);
        return node->value;
    }

    void put(int key, int value) {
        if (cache.find(key) != cache.end()) {
            Node* node = cache[key];
            node->value = value;
            moveToHead(node);
        } else {
            Node* node = new Node(key, value);
            cache[key] = node;
            addToHead(node);
            size++;
            if (size > capacity) {
                Node* node = removeTail();
                cache.erase(node->key);
                size--;
            }
        }
    }

    void removeNode(Node* node) {
        node->prev->next = node->next;
        node->next->prev = node->prev;
    }

    void addToHead(Node* node) {
        node->prev = dummy;
        node->next = dummy->next;
        node->prev->next = node;
        node->next->prev = node;
    }

    void moveToHead(Node* node) {
        removeNode(node);
        addToHead(node);
    }

    Node* removeTail() {
        Node* node = dummy->prev;
        removeNode(node);
        return node;
    }
};
// @lc code=end



