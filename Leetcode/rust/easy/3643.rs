/*
 * @lc app=leetcode id=3643 lang=rust
 *
 * [3643] Flip Square Submatrix Vertically
 */


// @lcpr-template-start
struct Solution;
// @lcpr-template-end
// @lc code=start
impl Solution {
    pub fn reverse_submatrix(mut grid: Vec<Vec<i32>>, x: i32, y: i32, k: i32) -> Vec<Vec<i32>> {
        let (x, y, k): (usize, usize, usize) = (x as usize, y as usize, k as usize);
        for i in 0..k / 2 {
            let (s1, s2) = grid.split_at_mut(x + k - 1 - i);
            let (row1, row2) = (&mut s1[x + i], &mut s2[0]);
            row1[y..y + k].swap_with_slice(&mut row2[y..y + k]);
        }
        grid
    }
}
// @lc code=end

