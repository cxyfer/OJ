/*
 * @lc app=leetcode id=1758 lang=rust
 *
 * [1758] Minimum Changes To Make Alternating Binary String
 */


// @lcpr-template-start
struct Solution;
// @lcpr-template-end
// @lc code=start
impl Solution {
    pub fn min_operations(s: String) -> i32 {
        let calc = |b: usize| -> i32 {
            s.bytes()
                .enumerate()
                .map(|(i, ch)| {
                    if (ch - b'0') as usize != (i & 1) ^ b { 1 } else { 0 }
                })
                .sum()
        };
        std::cmp::min(calc(0), calc(1))
    }
}
// @lc code=end
