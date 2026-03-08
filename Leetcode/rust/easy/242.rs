/*
 * @lc app=leetcode id=242 lang=rust
 *
 * [242] Valid Anagram
 */


// @lcpr-template-start
struct Solution;
// @lcpr-template-end
// @lc code=start
use std::collections::HashMap;

struct Solution1;
impl Solution1 {
    pub fn is_anagram(s: String, t: String) -> bool {
        if s.len() != t.len() { return false; }
        let mut cnt_s = HashMap::new();
        let mut cnt_t = HashMap::new();
        for c in s.chars() {
            *cnt_s.entry(c).or_insert(0) += 1;
        }
        for c in t.chars() {
            *cnt_t.entry(c).or_insert(0) += 1;
        }
        cnt_s == cnt_t
    }
}

struct Solution2;
impl Solution2 {
    pub fn is_anagram(s: String, t: String) -> bool {
        if s.len() != t.len() { return false; }
        let mut cnt = HashMap::new();
        for c in s.chars() {
            *cnt.entry(c).or_insert(0) += 1;
        }
        for c in t.chars() {
            *cnt.entry(c).or_insert(0) -= 1;
        }
        cnt.values().all(|&v| v == 0)
    }
}

impl Solution {
    pub fn is_anagram(s: String, t: String) -> bool {
        // Solution1::is_anagram(s, t)
        Solution2::is_anagram(s, t)
    }
}
// @lc code=end

