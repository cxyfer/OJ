#include <bits/stdc++.h>
using namespace std;
#define endl '\n'

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    int kase = 1, r, c;
    while (true){
        cin >> r >> c;
        if (r == 0) break;
        vector<string> tbl(r);
        for (int i = 0; i < r; i++) cin >> tbl[i];
        vector<vector<int>> mark(r, vector<int>(c, 0));
        int idx = 1;
        for (int i = 0; i < r; i++){
            for (int j = 0; j < c; j++){
                if (tbl[i][j] != '*' && (i == 0 || j == 0 || tbl[i - 1][j] == '*' || tbl[i][j - 1] == '*')){
                    mark[i][j] = idx++;
                }
            }
        }
        if (kase > 1) cout << endl;
        cout << "puzzle #" << kase++ << ":" << endl;
        cout << "Across" << endl;
        for (int i = 0; i < r; i++){
            for (int j = 0; j < c; j++){
                if (tbl[i][j] != '*' && (j == 0 || tbl[i][j - 1] == '*')){
                    string cur = "";
                    for (int k = j; k < c; k++){
                        if (tbl[i][k] == '*') break;
                        cur += tbl[i][k];
                    }
                    cout << setw(3) << mark[i][j] << "." << cur << endl;
                }
            }
        }
        cout << "Down" << endl;
        for (int i = 0; i < r; i++){
            for (int j = 0; j < c; j++){
                if (tbl[i][j] != '*' && (i == 0 || tbl[i - 1][j] == '*')){
                    string cur = "";
                    for (int k = i; k < r; k++){
                        if (tbl[k][j] == '*') break;
                        cur += tbl[k][j];
                    }
                    cout << setw(3) << mark[i][j] << "." << cur << endl;
                }
            }
        }
    }    
    return 0;
}