#include <bits/stdc++.h>
using namespace std;
const int N = 55;
#define endl '\n'

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    int t;
    cin >> t;
    for (int kase=1; kase<=t; kase++){
        string S;
        cin >> S;
        int n = S.size();
        vector<vector<char>> ans(1, vector<char>(N, ' '));
        int cur = 0;
        for (int j=0; j<n; j++){
            if (S[j] == 'C') ans[cur][j] = '_';
            else if (S[j] == 'R'){
                ans[cur][j] = '/';
                if (cur == 0) ans.insert(ans.begin(), vector<char>(N, ' '));
                else cur--;
            }
            else if (S[j] == 'F'){
                if (cur == ans.size() - 1) ans.push_back(vector<char>(N, ' '));
                cur++;
                ans[cur][j] = '\\';
            }
        }
        cout << "Case #" << kase << ":" << endl;
        bool flag = false;
        for (char ch : ans[0]) if (ch != ' ') flag = true;
        if (!flag) ans.erase(ans.begin()); // remove the first row if it's empty
        for (auto &row : ans){
            cout << "| ";
            int end = N; // find the last non-space character
            for (int i=N-1; i>=0; i--){
                if (row[i] != ' '){
                    end = i;
                    break;
                }
            }
            for (int i=0; i<=end; i++) cout << row[i];
            cout << endl;
        }
        cout << "+" << string(n+2, '-') << endl << endl;
    }
    return 0;
}