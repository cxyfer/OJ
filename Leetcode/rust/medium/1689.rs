/*
 * @lc app=leetcode id=1689 lang=rust
 *
 * [1689] Partitioning Into Minimum Number Of Deci-Binary Numbers
 */

// @lc code=start
use std::cmp::max;

impl Solution {
    pub fn min_partitions(n: String) -> i32 {
        let mut ans: i32 = 0;
        for c in n.chars() {
            ans = max(ans, (c as u8 - b'0') as i32);
        }
        ans
    }
}
// @lc code=end

