/*
 * @lc app=leetcode id=2839 lang=rust
 *
 * [2839] Check if Strings Can be Made Equal With Operations I
 */


// @lcpr-template-start
struct Solution;
// @lcpr-template-end
// @lc code=start
impl Solution {
    pub fn can_be_equal(s1: String, s2: String) -> bool {
        let mut cnts = [[0; 26]; 2];
        for (i, (ch1, ch2)) in s1.chars().zip(s2.chars()).enumerate() {
            cnts[i & 1][(ch1 as u8 - b'a') as usize] += 1;
            cnts[i & 1][(ch2 as u8 - b'a') as usize] -= 1;
        }
        cnts.iter().all(|cnt| cnt.iter().all(|&v| v == 0))
    }
}
// @lc code=end

