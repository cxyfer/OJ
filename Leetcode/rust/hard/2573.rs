/*
 * @lc app=leetcode id=2573 lang=rust
 *
 * [2573] Find the String with LCP
 */

// @lcpr-template-start
struct Solution;
// @lcpr-template-end
// @lc code=start
struct DSU {
    pa: Vec<usize>,
    sz: Vec<usize>,
    cnt: usize,
}

impl DSU {
    fn new(n: usize) -> Self {
        Self {
            pa: (0..n).collect(),
            sz: vec![1; n],
            cnt: n,
        }
    }

    fn find(&mut self, mut x: usize) -> usize {
        while self.pa[x] != x {
            self.pa[x] = self.pa[self.pa[x]];
            x = self.pa[x];
        }
        x
    }

    fn union(&mut self, x: usize, y: usize) -> bool {
        let mut fx = self.find(x);
        let mut fy = self.find(y);
        if fx == fy {
            return false;
        }
        if self.sz[fx] < self.sz[fy] {
            std::mem::swap(&mut fx, &mut fy);
        }
        self.pa[fy] = fx;
        self.sz[fx] += self.sz[fy];
        self.cnt -= 1;
        return true;
    }
}

struct Solution1;
impl Solution1 {
    pub fn find_the_string(lcp: Vec<Vec<i32>>) -> String {
        let n = lcp.len();

        let mut uf = DSU::new(n);
        for (i, row) in lcp.iter().enumerate() {
            if row[i] != (n - i) as i32 {
                return "".to_string();
            }
            for j in i + 1..n {
                if row[j] != lcp[j][i] || row[j] > (n - j) as i32 {
                    return "".to_string();
                }
                if row[j] > 0 {
                    uf.union(i, j);
                }
            }
        }

        let mut mp: Vec<usize> = vec![n; n];
        let mut comps: Vec<Vec<usize>> = vec![];
        for u in 0..n {
            let fu = uf.find(u);
            if mp[fu] == n {
                mp[fu] = comps.len();
                comps.push(vec![]);
            }
            comps[mp[fu]].push(u);
        }

        if comps.len() > 26 {
            return "".to_string();
        }

        let mut s: Vec<u8> = vec![0; n];
        for (i, comp) in comps.iter().enumerate() {
            for &u in comp {
                s[u] = (b'a' + i as u8) as u8;
            }
        }

        let mut lcp2: Vec<Vec<i32>> = vec![vec![0; n + 1]; n + 1];
        for ln in 1..=n {
            for i in (0..=n - ln).rev() {
                let j = i + ln - 1;
                if s[i] == s[j] {
                    lcp2[i][j] = lcp2[i + 1][j + 1] + 1;
                } else {
                    lcp2[i][j] = 0;
                }
                if lcp2[i][j] != lcp[i][j] {
                    return "".to_string();
                }
            }
        }

        String::from_utf8(s).unwrap()
    }
}

struct Solution2;
impl Solution2 {
    pub fn find_the_string(lcp: Vec<Vec<i32>>) -> String {
        let n = lcp.len();

        // 透過 lcp 矩陣可以找到必須為相同字元的索引，採用貪心的方式由小到大填入字元
        let mut s: Vec<u8> = vec![0; n];
        let mut i: usize = 0;
        for ch in 'a'..='z' {
            s[i] = ch as u8;
            for j in i + 1..n {
                // 如果 lcp[i][j] > 0，代表 s[i] 和 s[j] 是相同的字元
                if lcp[i][j] > 0 {
                    s[j] = ch as u8;
                }
            }
            // 找到下一個還沒填入字元的索引
            while i < n && s[i] != 0 {
                i += 1;
            }
            if i == n {
                break;
            }
        }

        // 用完所有字元，但還有空位，說明無法構造出符合 LCP 矩陣的字串
        // if s.iter().any(|&x| x == 0) {
        if i < n {
            return "".to_string();
        }

        // 驗證構造的字串是否符合 LCP 矩陣
        for i in (0..n).rev() {
            for j in (0..n).rev() {
                // 計算構造的字串的 LCP
                let exp = if s[i] == s[j] {
                    if i < n - 1 && j < n - 1 {
                        lcp[i + 1][j + 1] + 1
                    } else {
                        1
                    }
                } else {
                    0
                };
                // 若與 LCP 矩陣不符，則說明無法構造出符合 LCP 矩陣的字串
                if lcp[i][j] != exp {
                    return "".to_string();
                }
            }
        }

        String::from_utf8(s).unwrap()
    }
}

impl Solution {
    pub fn find_the_string(lcp: Vec<Vec<i32>>) -> String {
        // Solution1::find_the_string(lcp)
        Solution2::find_the_string(lcp)
    }
}
// @lc code=end
