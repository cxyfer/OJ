#include<iostream>
#define SZ(X) ((int)(X).size())
using namespace std;
const int SIZE = 1 << 10;
char s[SIZE][SIZE];
bool ban[SIZE][SIZE], visited[SIZE][SIZE];
int dx[4] = {1, 0, -1, 0};
int dy[4] = {0, 1, 0, -1};
int H, W;
bool out(int x, int y) {
    return x < 0 || y < 0 || x >= H || y >= W;
}
int tag;
int label[SIZE][SIZE];
int dfs(int x, int y) {
    if(visited[x][y]) return 0;
    visited[x][y] = 1;
    int ret = 1;
    for(int dir = 0; dir < 4; dir++) {
        int nx = x + dx[dir];
        int ny = y + dy[dir];
        if(out(nx, ny) || s[nx][ny] == '#') continue;
        if(visited[nx][ny]) continue;
        if(ban[nx][ny]) {
            if(label[nx][ny] == tag) continue;
            ret++;
            label[nx][ny] = tag;
        } else {
            ret += dfs(nx, ny);
        }
    }
    return ret;
}
int main() {
    cin.tie(0);
    ios_base::sync_with_stdio(false);
    cin >> H >> W;
    for(int i = 0; i < H; i++) {
        cin >> s[i];
    }
    for(int i = 0; i < H; i++) {
        for(int j = 0; j < W; j++) {
            if(s[i][j] == '#') {
                for(int dir = 0; dir < 4; dir++) {
                    int nx = i + dx[dir];
                    int ny = j + dy[dir];
                    if(out(nx, ny)) continue;
                    ban[nx][ny] = 1;
                }
            }
        }
    }
    int ma = 1;
    for(int i = 0; i < H; i++) {
        for(int j = 0; j < W; j++) {
            if(s[i][j] == '#' || ban[i][j]) continue;
            tag++;
            ma = max(ma, dfs(i, j));
        }
    }
    cout << ma << '\n';
}