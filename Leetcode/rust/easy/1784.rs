/*
 * @lc app=leetcode id=1784 lang=rust
 *
 * [1784] Check if Binary String Has at Most One Segment of Ones
 */


// @lcpr-template-start
struct Solution;
// @lcpr-template-end
// @lc code=start
struct Solution1;
impl Solution1 {
    pub fn check_ones_segment(s: String) -> bool {
        // as_bytes -> Vec<u8>, can be sliced
        s.as_bytes().windows(2).filter(|w| w[0] != w[1]).count() <= 1
    }
}

struct Solution2;
impl Solution2 {
    pub fn check_ones_segment(s: String) -> bool {
        !s.contains("01")
    }
}

impl Solution {
    pub fn check_ones_segment(s: String) -> bool {
        Solution1::check_ones_segment(s)
        // Solution2::check_ones_segment(s)
    }
}
// @lc code=end

