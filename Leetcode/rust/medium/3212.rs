/*
 * @lc app=leetcode id=3212 lang=rust
 *
 * [3212] Count Submatrices With Equal Frequency of X and Y
 */


// @lcpr-template-start
struct Solution;
// @lcpr-template-end
// @lc code=start
struct Solution1a;
impl Solution1a {
    pub fn number_of_submatrices(grid: Vec<Vec<char>>) -> i32 {
        let (m, n): (usize, usize) = (grid.len(), grid[0].len());
        let mut ans: i32 = 0;
        let mut s: Vec<Vec<[i32; 2]>> = vec![vec![[0; 2]; n + 1]; m + 1];
        for (i, row) in grid.iter().enumerate() {
            for (j, &ch) in row.iter().enumerate() {
                let c: usize = (ch as u8 - b'X') as usize;
                for b in 0..2 {
                    s[i + 1][j + 1][b] = s[i + 1][j][b] + s[i][j + 1][b] - s[i][j][b] + (c == b) as i32;
                }
                if s[i + 1][j + 1][0] == s[i + 1][j + 1][1] && s[i + 1][j + 1][0] > 0 {
                    ans += 1;
                }
            }
        }
        ans
    }
}

struct Solution1b;
impl Solution1b {
    pub fn number_of_submatrices(grid: Vec<Vec<char>>) -> i32 {
        let n: usize = grid[0].len();
        let mut ans: i32 = 0;
        let (mut f, mut nf): (Vec<[i32; 2]>, Vec<[i32; 2]>) = (vec![[0; 2]; n + 1], vec![[0; 2]; n + 1]);
        for row in grid {
            for (j, &ch) in row.iter().enumerate() {
                let c: usize = (ch as u8 - b'X') as usize;
                for b in 0..2 {
                    nf[j + 1][b] = f[j + 1][b] + nf[j][b] - f[j][b] + (c == b) as i32;
                }
                if nf[j + 1][0] == nf[j + 1][1] && nf[j + 1][0] > 0 {
                    ans += 1;
                }
            }
            std::mem::swap(&mut f, &mut nf);
        }
        ans
    }
}

struct Solution2;
impl Solution2 {
    pub fn number_of_submatrices(grid: Vec<Vec<char>>) -> i32 {
        let n: usize = grid[0].len();
        let mut ans: i32 = 0;
        let mut col: Vec<[i32; 2]> = vec![[0, 0]; n];
        for row in grid {
            let mut cnt: [i32; 2] = [0, 0];
            for (j, &ch) in row.iter().enumerate() {
                if ch != '.' {
                    col[j][(ch as u8 - b'X') as usize] += 1;
                }
                for b in 0..2 {
                    cnt[b] += col[j][b];
                }
                if cnt[0] == cnt[1] && cnt[0] > 0 {
                    ans += 1;
                }
            }
        }
        ans
    }
}

impl Solution {
    pub fn number_of_submatrices(grid: Vec<Vec<char>>) -> i32 {
        // Solution1a::number_of_submatrices(grid)
        // Solution1b::number_of_submatrices(grid)
        Solution2::number_of_submatrices(grid)
    }
}
// @lc code=end