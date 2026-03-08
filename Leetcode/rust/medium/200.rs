/*
 * @lc app=leetcode id=200 lang=rust
 *
 * [200] Number of Islands
 */


// @lcpr-template-start
struct Solution;
// @lcpr-template-end
// @lc code=start
struct Solution1;
impl Solution1 {
    pub fn num_islands(mut grid: Vec<Vec<char>>) -> i32 {
        let m = grid.len();
        let n = grid[0].len();
        let mut ans = 0;

        fn dfs(grid: &mut Vec<Vec<char>>, x: i32, y: i32, m: i32, n: i32) {
            grid[x as usize][y as usize] = '0';
            let dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)];
            for (dx, dy) in dirs {
                let nx = x + dx;
                let ny = y + dy;
                if nx < 0 || nx >= m || ny < 0 || ny >= n || grid[nx as usize][ny as usize] == '0' {
                    continue;
                }
                grid[nx as usize][ny as usize] = '0';
                dfs(grid, x + dx, y + dy, m, n);
            }
        }

        for i in 0..m {
            for j in 0..n {
                if grid[i][j] == '1' {
                    ans += 1;
                    grid[i][j] = '0';
                    dfs(&mut grid, i as i32, j as i32, m as i32, n as i32);
                }
            }
        }
        ans
    }
}

struct Solution2;
impl Solution2 {
    pub fn num_islands(grid: Vec<Vec<char>>) -> i32 {
        let m = grid.len();
        let n = grid[0].len();
        
        let mut ans = grid.iter().flatten().filter(|&&c| c == '1').count() as i32;

        let mut fa: Vec<usize> = (0..m * n).collect();
        let mut sz = vec![1; m * n];

        fn find(fa: &mut Vec<usize>, i: usize) -> usize {
            if fa[i] == i {
                return i;
            }
            let p = fa[i];
            let root = find(fa, p);
            fa[i] = root;
            root
        }

        fn union(fa: &mut Vec<usize>, sz: &mut Vec<usize>, ans: &mut i32, x: usize, y: usize) {
            let mut fx = find(fa, x);
            let mut fy = find(fa, y);
            if fx != fy {
                if sz[fx] < sz[fy] {
                    std::mem::swap(&mut fx, &mut fy);
                }
                fa[fy] = fx;
                sz[fx] += sz[fy];
                *ans -= 1;
            }
        }

        for i in 0..m {
            for j in 0..n {
                if grid[i][j] == '1' {
                    // 只需檢查右邊和下邊，避免重複合併
                    let dirs = [(0, 1), (1, 0)];
                    for (dx, dy) in dirs {
                        let ni = i + dx;
                        let nj = j + dy;
                        if ni < m && nj < n && grid[ni][nj] == '1' {
                            union(&mut fa, &mut sz, &mut ans, i * n + j, ni * n + nj);
                        }
                    }
                }
            }
        }
        ans
    }
}

impl Solution {
    pub fn num_islands(grid: Vec<Vec<char>>) -> i32 {
        // Solution1::num_islands(grid)
        Solution2::num_islands(grid)
    }
}
// @lc code=end

