/*
 * @lc app=leetcode id=146 lang=rust
 *
 * [146] LRU Cache
 */


// @lcpr-template-start
struct Solution;
// @lcpr-template-end
// @lc code=start
use std::collections::HashMap;

struct Node {
    key: i32,
    val: i32,
    prev: usize,
    next: usize,
}

impl Node {
    fn new(key: i32, val: i32) -> Self {
        Node { key, val, prev: 0, next: 0 }
    }
}

// Arena-based doubly linked list: nodes[0] is the dummy sentinel.
struct LRUCache {
    capacity: usize,
    size: usize,
    cache: HashMap<i32, usize>,  // key -> index
    nodes: Vec<Node>,
}

impl LRUCache {
    fn new(capacity: i32) -> Self {
        LRUCache {
            capacity: capacity as usize,
            size: 0,
            cache: HashMap::new(),
            nodes: vec![Node::new(-1, -1)],
        }
    }

    fn remove_node(&mut self, node: usize) {
        let prev = self.nodes[node].prev;
        let next = self.nodes[node].next;
        self.nodes[prev].next = next;
        self.nodes[next].prev = prev;
    }

    fn add_to_head(&mut self, node: usize) {
        let head_next = self.nodes[0].next;
        self.nodes[node].prev = 0;
        self.nodes[node].next = head_next;
        self.nodes[head_next].prev = node;
        self.nodes[0].next = node;
    }

    fn move_to_head(&mut self, node: usize) {
        self.remove_node(node);
        self.add_to_head(node);
    }

    fn remove_tail(&mut self) -> usize {
        let tail = self.nodes[0].prev;
        self.remove_node(tail);
        tail
    }

    fn get(&mut self, key: i32) -> i32 {
        if let Some(&node) = self.cache.get(&key) {
            self.move_to_head(node);
            self.nodes[node].val
        } else {
            -1
        }
    }

    fn put(&mut self, key: i32, value: i32) {
        if let Some(&node) = self.cache.get(&key) {
            self.nodes[node].val = value;
            self.move_to_head(node);
        } else {
            let node = self.nodes.len(); // next free slot
            self.nodes.push(Node::new(key, value));
            self.cache.insert(key, node);
            self.add_to_head(node);
            self.size += 1;
            if self.size > self.capacity {
                let tail = self.remove_tail();
                let tail_key = self.nodes[tail].key;
                self.cache.remove(&tail_key);
                self.size -= 1;
            }
        }
    }
}
// @lc code=end
