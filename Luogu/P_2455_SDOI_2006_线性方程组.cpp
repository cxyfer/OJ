#include <bits/stdc++.h>
using namespace std;
#define endl '\n'

// Gauss elimination solver
int gauss_elimination(vector<vector<double>>& mat, vector<double>& ans, const double eps = 1e-6) {
    int n = mat.size(), rank = 0;
    
    // Forward elimination
    for (int col = 0; col < n; col++) {
        // Find pivot
        int pivot = rank;
        for (int i = rank + 1; i < n; i++) {
            if (abs(mat[i][col]) > abs(mat[pivot][col])) {
                pivot = i;
            }
        }
        
        // If current column is all zeros, continue
        if (abs(mat[pivot][col]) < eps) continue;
        
        // Swap rows if necessary
        if (pivot != rank) {
            swap(mat[rank], mat[pivot]);
        }
        
        // Eliminate column
        for (int i = rank + 1; i < n; i++) {
            if (abs(mat[i][col]) < eps) continue;
            double factor = mat[i][col] / mat[rank][col];
            for (int k = col; k <= n; k++) {
                mat[i][k] -= mat[rank][k] * factor;
            }
        }
        rank++;
    }
    
    // Check for no solution
    for (int i = rank; i < n; i++) {
        if (abs(mat[i][n]) > eps) return -1;  // No solution
    }
    
    // Check for infinite solutions
    if (rank < n) return 0;  // Infinite solutions
    
    // Back substitution
    for (int i = n - 1; i >= 0; i--) {
        double sum = 0;
        for (int j = i + 1; j < n; j++) {
            sum += mat[i][j] * ans[j];
        }
        ans[i] = (mat[i][n] - sum) / mat[i][i];
        if (abs(ans[i]) < eps) ans[i] = 0;
    }
    
    return 1;  // Unique solution
}

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    int n; cin >> n;
    
    vector<vector<double>> mat(n, vector<double>(n + 1));
    for (int i = 0; i < n; i++) {
        for (int j = 0; j <= n; j++) {
            cin >> mat[i][j];
        }
    }
    
    vector<double> ans(n, 0);
    int flag = gauss_elimination(mat, ans);
    
    if (flag == -1) {
        cout << -1 << endl;  // No solution
    } else if (flag == 0) {
        cout << 0 << endl;   // Infinite solutions
    } else {
        for (int i = 0; i < n; i++) {
            cout << format("x{}={:.2f}", i + 1, ans[i]) << endl;
        }
    }
    
    return 0;
}