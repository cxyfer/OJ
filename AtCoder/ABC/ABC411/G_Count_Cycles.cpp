#include <bits/stdc++.h>
using namespace std;
using LL = long long;
const int MOD = 998244353;
#define endl '\n'

int N_nodes_global;
vector<vector<int>> adj_matrix_global;
vector<vector<LL>> memo_dp_global;

LL power_global(LL base, LL exp) {
    LL res = 1;
    base %= MOD;
    while (exp > 0) {
        if (exp % 2 == 1) res = (res * base) % MOD;
        base = (base * base) % MOD;
        exp /= 2;
    }
    return res;
}

LL modInverse_global(LL n) {
    return power_global(n, MOD - 2);
}

LL dp_function_global(int msk, int u) {
    if (memo_dp_global[msk][u] != -1) {
        return memo_dp_global[msk][u];
    }

    int s = __builtin_ctz(msk); // Index of the least significant bit (smallest node in mask)

    if (__builtin_popcount(msk) == 1) {
        // Base case: mask has only one bit set.
        // Path from s to u, where msk = {s}. Only possible if u=s.
        return memo_dp_global[msk][u] = (u == s ? 1 : 0);
    }

    if (u == s) {
        // If u is the starting node s, and mask has more than one node,
        // this path configuration is invalid for extending (cannot return to s yet).
        return memo_dp_global[msk][u] = 0;
    }

    LL current_sum = 0;
    int prev_msk = msk ^ (1 << u); // Mask without current node u

    // Iterate over nodes v in prev_msk to be the predecessor of u
    int temp_iter_msk = prev_msk;
    while (temp_iter_msk > 0) {
        int v = __builtin_ctz(temp_iter_msk); // Get LSB index from remaining bits in prev_msk
        
        if (adj_matrix_global[v][u] > 0) { // If there's an edge from v to u
            LL paths_to_v = dp_function_global(prev_msk, v);
            current_sum = (current_sum + paths_to_v * adj_matrix_global[v][u]) % MOD;
        }
        
        temp_iter_msk &= (temp_iter_msk - 1); // Remove LSB to process next bit
    }

    return memo_dp_global[msk][u] = current_sum;
}

void solve_one_case() {
    int M_edges;
    cin >> N_nodes_global >> M_edges;

    adj_matrix_global.assign(N_nodes_global, vector<int>(N_nodes_global, 0));
    for (int i = 0; i < M_edges; ++i) {
        int u_in, v_in;
        cin >> u_in >> v_in;
        --u_in; --v_in; // 0-indexed
        adj_matrix_global[u_in][v_in]++;
        adj_matrix_global[v_in][u_in]++; // Undirected graph, counts parallel edges
    }

    LL ans1 = 0;
    for (int u_loop = 0; u_loop < N_nodes_global; ++u_loop) {
        for (int v_loop = u_loop + 1; v_loop < N_nodes_global; ++v_loop) {
            if (adj_matrix_global[u_loop][v_loop] >= 2) {
                LL count = adj_matrix_global[u_loop][v_loop];
                ans1 = (ans1 + count * (count - 1) / 2) % MOD;
            }
        }
    }
    
    // Max msk is (1 << N_nodes_global) - 1. So size is 1 << N_nodes_global.
    memo_dp_global.assign(1 << N_nodes_global, vector<LL>(N_nodes_global, -1));

    LL ans2 = 0;
    // Iterate over all possible masks for cycles of length >= 3
    for (int msk = 0; msk < (1 << N_nodes_global); ++msk) {
        if (__builtin_popcount(msk) < 3) {
            continue;
        }

        int s_cycle = __builtin_ctz(msk); // Smallest node in the cycle (LSB of mask)

        // Iterate over u_cycle_end in msk, u_cycle_end != s_cycle
        // This is the node just before returning to s_cycle to complete the cycle
        int msk_without_s = msk ^ (1 << s_cycle);
        int temp_iter_msk_for_u = msk_without_s;
        while (temp_iter_msk_for_u > 0) {
            int u_cycle_end = __builtin_ctz(temp_iter_msk_for_u);
            
            if (adj_matrix_global[u_cycle_end][s_cycle] > 0) { // If edge exists to close the cycle
                // dp_function_global(msk, u_cycle_end) counts paths from s_cycle to u_cycle_end
                // using all nodes in msk exactly once.
                LL paths_s_to_u = dp_function_global(msk, u_cycle_end);
                ans2 = (ans2 + paths_s_to_u * adj_matrix_global[u_cycle_end][s_cycle]) % MOD;
            }
            
            temp_iter_msk_for_u &= (temp_iter_msk_for_u - 1); // Remove LSB
        }
    }

    if (ans2 > 0) { // Avoid issues with modInverse(2) if ans2 is 0
        LL inv2 = modInverse_global(2);
        ans2 = (ans2 * inv2) % MOD;
    }
    
    LL final_ans = (ans1 + ans2) % MOD;
    // Ensure the result is non-negative before the final modulo, though with current logic it should be.
    final_ans = (final_ans + MOD) % MOD;
    cout << final_ans << endl;
}

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    solve_one_case();
    return 0;
}
