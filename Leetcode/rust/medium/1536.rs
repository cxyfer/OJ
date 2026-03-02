/*
 * @lc app=leetcode id=1536 lang=rust
 *
 * [1536] Minimum Swaps to Arrange a Binary Grid
 */

// @lcpr-template-start
struct Solution;
// @lcpr-template-end
// @lc code=start
impl Solution {
    pub fn min_swaps(grid: Vec<Vec<i32>>) -> i32 {
        let n = grid.len();
        let mut tail0 = vec![n; n];
        for i in 0..n {
            for j in (0..n).rev() {
                if grid[i][j] == 1 {
                    tail0[i] = n - j - 1;
                    break;
                }
            }
        }
        let mut ans: i32 = 0;
        for i in 0..n {
            let tgt = n - i - 1;
            if let Some(j) = (i..n).find(|&j| tail0[j] >= tgt) {
                ans += (j - i) as i32;
                tail0[i..=j].rotate_right(1);
            } else {
                return -1;
            }
        }
        ans
    }
}
// @lc code=end
fn main() {
    let grid = vec![vec![0, 0, 1], vec![1, 1, 0], vec![1, 0, 0]];
    println!("{}", Solution::min_swaps(grid)); // 3
}
