/*
    BFS
    注意是跳到下一個與當前不同的按鍵，可以預處理
    有點類似 SPFA (Shortest Path Faster Algorithm)
*/

#include <bits/stdc++.h>
using namespace std;
const int N = 55;
#define endl '\n'

struct Node {
    int x, y, idx, step;
};

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    int r, c, x, y, nx, ny, idx, step;
    vector<pair<int, int>> nxt[N][N];
    int visited[N][N];
    int DX[4] = {1, -1, 0, 0}, DY[4] = {0, 0, 1, -1};
    while (cin >> r >> c){
        vector<string> kb(r);
        for (int i = 0; i < r; i++){
            cin >> kb[i];
        }
        string s;
        cin >> s;
        s += "*"; // add end mark (enter)
        // find next key that is different from current key
        for (int i = 0; i < r; i++){
            for (int j = 0; j < c; j++){
                nxt[i][j].clear();
                for (int k = 0; k < 4; k++){
                    nx = i + DX[k], ny = j + DY[k];
                    while (nx >= 0 && nx < r && ny >= 0 && ny < c && kb[nx][ny] == kb[i][j]){
                        nx += DX[k], ny += DY[k];
                    }
                    if (nx >= 0 && nx < r && ny >= 0 && ny < c){ // valid
                        nxt[i][j].push_back({nx, ny});
                    }
                }
            }
        }
        // BFS
        int ans = INT_MAX;
        // visited[i][j] = k means that when we reach (i, j), we have at most input s[k]
        memset(visited, -1, sizeof(visited));
        queue<Node> q;
        q.push({0, 0, 0, 0}); // (x, y, idx, step)
        while (!q.empty()){
            Node node = q.front(); q.pop();
            x = node.x, y = node.y, idx = node.idx, step = node.step;
            if (kb[x][y] == s[idx]){
                if (idx == s.size() - 1){ // reach the end
                    ans = step + 1;
                    break;
                }
                q.push({x, y, idx+1, step+1}); // stay at current position, but press the botton
                visited[x][y] = max(visited[x][y], idx+1); // update visited
            } else {
                for (pair<int, int> p : nxt[x][y]){
                    nx = p.first, ny = p.second;
                    if (visited[nx][ny] >= idx){ // Pruning
                        continue;
                    }
                    visited[nx][ny] = idx;
                    q.push({nx, ny, idx, step+1}); // move to next position
                }
            }
        }
        cout << ans << endl;
    }
    return 0;
}