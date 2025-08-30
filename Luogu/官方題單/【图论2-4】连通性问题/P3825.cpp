/*
P3825 [NOI2017] 游戏
https://www.luogu.com.cn/problem/P3825

P ⇒ Q 邏輯上等價於 ¬P ∨ Q，有以下兩個蘊含關係：
1. P ⇒ Q
2. ¬Q ⇒ ¬P

對於一個 x 地圖，與其枚舉「用哪輛車」，不如枚舉「禁用哪輛車」。
如果禁止使用賽車 A，那麼選擇就變成了 B 或 C，又回到了「二選一」的問題。
而考慮禁用 A 和 禁用 B 兩種情況，就能包含到所有的 3 種車，
因此枚舉 3 種車的哪種，不如枚舉禁用哪 2 種車。

其餘參考 P4782 【模板】2-SAT
*/
#include <bits/stdc++.h>
using namespace std;
#define endl '\n'

class SCC {
public:
    /* 建圖*/
    int n;
    vector<vector<int>> g;

    /* Tarjan & SCC 相關 */
    int time;
    vector<int> dfn, low, stk;
    vector<bool> in_stk;
    vector<int> scc_id;
    int scc_cnt;

    SCC(int n) : n(n) {
        g.resize(n);
        time = 0;
        dfn.assign(n, -1);
        low.assign(n, -1);
        in_stk.assign(n, false);
        scc_id.assign(n, -1);
        scc_cnt = 0;
    }

    void add_edge(int u, int v) {
        g[u].push_back(v);
    }

    void dfs(int u) {
        dfn[u] = low[u] = time++;
        stk.push_back(u);
        in_stk[u] = true;
        for (auto v : g[u]) {
            if (dfn[v] == -1) {
                dfs(v);
                low[u] = min(low[u], low[v]);
            } else if (in_stk[v]) {
                low[u] = min(low[u], dfn[v]);
            }
        }
        if (dfn[u] == low[u]) {
            int v;
            while (true) {
                v = stk.back();
                stk.pop_back();
                in_stk[v] = false;
                scc_id[v] = scc_cnt;
                if (v == u) break;
            }
            scc_cnt++;
        }
    }

    void run() {
        for (int u = 0; u < n; u++)
            if (dfn[u] == -1) dfs(u);
    }

    void reset() {
        time = 0;
        for (int i = 0; i < n; ++i)
            g[i].clear();
        dfn.assign(n, -1);
        low.assign(n, -1);
        in_stk.assign(n, false);
        scc_id.assign(n, -1);
        stk.clear();
        scc_cnt = 0;
    }
};

struct Rule {
    int i, j;
    char x, y;
};

void solve() {
    int n, d, m;
    string s;
    cin >> n >> d >> s >> m;
    vector<Rule> rules(m);
    for (auto& r : rules) {
        cin >> r.i >> r.x >> r.j >> r.y;
        r.i--, r.j--;
    }

    vector<pair<char, char>> choices(n);
    vector<int> x_pos;
    for (int i = 0; i < n; i++) {
        if (s[i] == 'a')
            choices[i] = {'B', 'C'};
        else if (s[i] == 'b')
            choices[i] = {'A', 'C'};
        else if (s[i] == 'c')
            choices[i] = {'A', 'B'};
        else
            x_pos.push_back(i);
    }

    SCC T(2 * n);
    // 二進位枚舉 d 個 x 地圖的禁用情況
    for (int k = 0; k < (1 << d); k++) {
        // for (auto [i, pos] : views::enumerate(x_pos))
        for (int i = 0; i < x_pos.size(); i++) {
            int pos = x_pos[i];
            if ((k >> i) & 1)
                choices[pos] = {'B', 'C'};  // 禁用 A
            else
                choices[pos] = {'A', 'C'};  // 禁用 B
        }

        T.reset();
        
        // 對於每個規則，建圖
        for (auto& [i, j, x, y] : rules) {
            int p, np, q, nq;

            auto [c1, c2] = choices[i];
            // 如果要求 x 是第一種選項，那麼 P 對應 i， ¬P 對應 i + n
            if (x == c1)
                p = i, np = i + n;
            else if (x == c2)
                p = i + n, np = i;
            // P 不可能成立，因此 P ⇒ Q 一定成立
            else
                continue;

            auto [c3, c4] = choices[j];
            if (y == c3)
                q = j, nq = j + n;
            else if (y == c4)
                q = j + n, nq = j;
            else {
                // Q 不可能成立，因此 P 需要不成立才能使 P ⇒ Q 成立
                // P 不成立可以用 P ⇒ ¬P 來限制，
                // 這意味著如果選了 P，那麼也要選 ¬P，這一定會導致矛盾
                T.add_edge(p, np);
                continue;
            }

            T.add_edge(p, q);
            T.add_edge(nq, np);
        }

        T.run();

        // 檢查是否有解
        bool ok = true;
        for (int i = 0; i < n; i++) {
            if (T.scc_id[i] == T.scc_id[i + n]) {
                ok = false;
                break;
            }
        }
        if (!ok) continue;

        string ans = "";
        for (int i = 0; i < n; i++)
            ans += (T.scc_id[i] < T.scc_id[i + n]) ? choices[i].first
                                                   : choices[i].second;
        cout << ans << endl;
        return;
    }
    // 無解
    cout << -1 << endl;
    return;
}

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr);
#ifdef LOCAL
    ifstream fin("input.txt");
    cin.rdbuf(fin.rdbuf());
#endif
    solve();
    return 0;
}