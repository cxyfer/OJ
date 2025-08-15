/*
 * P3379 【模板】最近公共祖先（LCA）
 * https://www.luogu.com.cn/problem/P3379
 * 用樹鏈剖分求 LCA
 */
#include <bits/stdc++.h>
using namespace std;
#define endl '\n'

struct Node {
    int fa, dep, sz, son, top;  // 求 LCA 其實不需要 dfn
    Node() : fa(0), dep(0), sz(0), son(0), top(0) {}
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);
    int N, M, R;
    cin >> N >> M >> R;

    vector<Node> A(N + 1);
    vector<vector<int>> g(N + 1);
    for (int i = 1; i < N; i++) {
        int u, v;
        cin >> u >> v;
        g[u].push_back(v);
        g[v].push_back(u);
    }

    auto dfs1 = [&](this auto&& dfs1, int u, int fa) -> void {
        A[u].fa = fa;
        A[u].dep = A[fa].dep + 1;
        A[u].sz = 1;
        for (int v : g[u]) {
            if (v == fa) continue;
            dfs1(v, u);
            A[u].sz += A[v].sz;
            if (A[u].son == 0 || A[A[u].son].sz < A[v].sz) A[u].son = v;
        }
        return;
    };
    dfs1(R, 0);

    int dfn = 0;
    auto dfs2 = [&](this auto&& dfs2, int u, int top) -> void {
        if (u == 0) return;
        A[u].top = top;
        dfs2(A[u].son, top);  // 先遍歷重鏈
        for (int v : g[u]) {
            if (v == A[u].fa || v == A[u].son) continue;
            dfs2(v, v);
        }
        return;
    };
    dfs2(R, R);

    int u, v;
    while (M--) {
        cin >> u >> v;
        while (A[u].top != A[v].top) {
            if (A[A[u].top].dep >= A[A[v].top].dep)
                u = A[A[u].top].fa;
            else
                v = A[A[v].top].fa;
        }
        cout << (A[u].dep < A[v].dep ? u : v) << endl;
    }
    return 0;
}