/*
    Backtracking + Pruning
    完全暴力是 4 ^ 48 ，不管如何都會 TLE，必須剪枝：
    - 走到邊界外
    - 走過的格子不能再走
    - 走到終點時，步數必須正好是 48，否則若提早到達終點，則無法在最後一步走到終點
    - 會把未走過的格子分成兩部分 (最重要的剪枝)
        - 若上下走過但左右沒走過，或左右走過但上下沒走過，則會把圖分成兩部分，無法走到終點
*/
#include <bits/stdc++.h>
using namespace std;
const int N = 9;
const int S = 48;
#define endl '\n'

string cmd;
int ans = 0;
bool visited[N][N];

void dfs(int x, int y, int step) {
    if (x <= 0 || x >= N-1 || y <= 0 || y >= N-1) return; // 越界
    if (visited[x][y]) return; // 走過
    if (x == 7 && y == 1){ // 到達終點，檢查步數是否正確
        if (step == S) ans++;
        return; 
    }
    if (step >= S) return ; // 超過步數，不合法，但應該不會有這種情況
    // 由於起點和終點都在邊界上，因此若上下走過但左右沒走過，或左右走過但上下沒走過，則會把圖分成兩部分，無法走到終點
    if (visited[x-1][y] && visited[x+1][y] && !visited[x][y-1] && !visited[x][y+1]) return;
    if (!visited[x-1][y] && !visited[x+1][y] && visited[x][y-1] && visited[x][y+1]) return;

    visited[x][y] = true;
    if (cmd[step] == 'U') dfs(x-1, y, step+1);
    else if (cmd[step] == 'D') dfs(x+1, y, step+1);
    else if (cmd[step] == 'L') dfs(x, y-1, step+1);
    else if (cmd[step] == 'R') dfs(x, y+1, step+1);
    else {
        dfs(x-1, y, step+1);
        dfs(x+1, y, step+1);
        dfs(x, y-1, step+1);
        dfs(x, y+1, step+1);
    }
    visited[x][y] = false;
    return;
}

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    cin >> cmd;
    for (int i = 0; i < N; i++) { // padding
        visited[i][0] = visited[i][N-1] = visited[0][i] = visited[N-1][i] = true;
    }
    dfs(1, 1, 0);
    cout << ans << endl;
    return 0;
}