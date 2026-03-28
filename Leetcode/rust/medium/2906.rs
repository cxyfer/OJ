/*
 * @lc app=leetcode id=2906 lang=rust
 *
 * [2906] Construct Product Matrix
 */


// @lcpr-template-start
struct Solution;
// @lcpr-template-end
// @lc code=start
const MOD: i32 = 12345;

struct Solution1;
impl Solution1 {
    pub fn construct_product_matrix(mut grid: Vec<Vec<i32>>) -> Vec<Vec<i32>> {
        let (m, n): (usize, usize) = (grid.len(), grid[0].len());
        let mut ans: Vec<Vec<i32>> = vec![vec![0; n]; m];

        let mut pre: i32 = 1;
        for (i, row) in grid.iter_mut().enumerate() {
            for (j, x) in row.iter_mut().enumerate() {
                *x %= MOD;
                ans[i][j] = pre;
                pre = pre * (*x) % MOD;
            }
        }
        
        let mut suf: i32 = 1;
        for i in (0..m).rev() {
            for j in (0..n).rev() {
                ans[i][j] = ans[i][j] * suf % MOD;
                suf = suf * grid[i][j] % MOD;
            }
        }
        ans
    }
}


pub fn qpow(mut base: i64, mut exp: i32, m: i32) -> i64 {
    let mut res: i64 = 1;
    let mut exp: i64 = exp as i64;
    let m: i64 = m as i64;
    base %= m;
    while exp > 0 {
        if exp & 1 == 1 {
            res = (res * base) % m;
        }
        base = (base * base) % m;
        exp >>= 1;
    }
    res
}


use itertools::izip;
const FACTORS: [i64; 3] = [3, 5, 823];
// phi(12345) = 12345 * (1-1/3) * (1-1/5) * (1-1/823) = 6576
const PHI: i32 = 6576;

struct Solution2;
impl Solution2 {
    pub fn construct_product_matrix(grid: Vec<Vec<i32>>) -> Vec<Vec<i32>> {
        let (m, n) = (grid.len(), grid[0].len());
        let mut ans = vec![vec![0; n]; m];

        let mut exps: [i32; 3] = [0; 3];
        let mut rem: i64 = 1;

        for row in &grid {
            for &val in row {
                let mut x: i64 = val as i64;
                for (k, &p) in FACTORS.iter().enumerate() {
                    while x % p == 0 {
                        exps[k] += 1;
                        x /= p;
                    }
                }
                rem = (rem * x % MOD as i64) % MOD as i64;
            }
        }

        for (i, row) in grid.iter().enumerate() {
            for (j, &val) in row.iter().enumerate() {
                let mut x: i64 = val as i64;
                let mut cur_exps: [i32; 3] = [0; 3];
                for (k, &p) in FACTORS.iter().enumerate() {
                    while x % p == 0 {
                        cur_exps[k] += 1;
                        x /= p;
                    }
                }

                let mut res: i64 = 1;
                for (&p, &e1, &e2) in izip!(&FACTORS, &exps, &cur_exps) {
                    res = (res * qpow(p, e1 - e2, MOD)) % MOD as i64;
                }
                res = (res * rem * qpow(x % MOD as i64, PHI - 1, MOD)) % MOD as i64;
                ans[i][j] = res as i32;
            }
        }
        ans
    }
}

impl Solution {
    pub fn construct_product_matrix(grid: Vec<Vec<i32>>) -> Vec<Vec<i32>> {
        Solution1::construct_product_matrix(grid)
        // Solution2::construct_product_matrix(grid)
    }
}
// @lc code=end
