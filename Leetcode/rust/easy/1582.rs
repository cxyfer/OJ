/*
 * @lc app=leetcode id=1582 lang=rust
 *
 * [1582] Special Positions in a Binary Matrix
 */


// @lcpr-template-start
struct Solution;
// @lcpr-template-end
// @lc code=start
impl Solution {
    pub fn num_special(mat: Vec<Vec<i32>>) -> i32 {
        let n = mat[0].len();
        let mut cols = vec![0; n];
        for row in mat.iter() {
            for (j, x) in row.iter().enumerate() {
                cols[j] += x;
            }
        }

        let mut ans = 0;
        for row in mat.iter() {
            if row.iter().sum::<i32>() == 1 {
                let j = row.iter().position(|&x| x == 1).unwrap();
                if cols[j] == 1 {
                    ans += 1;
                }
            }
        }
        ans
    }
}
// @lc code=end

