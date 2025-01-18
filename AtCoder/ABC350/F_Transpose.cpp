#include <bits/stdc++.h>
using namespace std;
const int N = 5e5 + 10;
#define endl '\n'

string s;
int pos[N] = {-1};
stack<int> st;

void dfs(int i, int j, bool flag){
    if (i > j) return;
    if (flag) {
        int k = i;
        while (k <= j) {
            char ch = s[k];
            if (ch == '(') {
                dfs(k+1, pos[k]-1, flag^1);
                k = pos[k];
            } else {
                cout << ch;
            }
            k++;
        }
    } else {
        while (j >= i) {
            char ch = s[j];
            if (s[j] == ')') {
                dfs(pos[j]+1, j-1, flag^1);
                j = pos[j];
            } else {
                cout << (char) (islower(ch) ? toupper(ch) : tolower(ch));
            }
            j--;
        }
    }
}

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    cin >> s;
    int n = s.size();
    for (int i = 0; i < n; i++) { // 預處理括號對應位置
        if (s[i] == '(') {
            st.push(i);
        } else if (s[i] == ')') {
            pos[i] = st.top();
            pos[st.top()] = i;
            st.pop();
        }
    }
    dfs(0, n-1, 1);
    return 0;
}