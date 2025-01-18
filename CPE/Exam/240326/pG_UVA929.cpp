/*
    Dijkstra
    tags: CPE-140325
*/
#include <bits/stdc++.h>
using namespace std;
using LL = long long;
const int N = 1000 + 5;
const int INF = 0x3f3f3f3f;
#define endl '\n'

struct Node {
    int x, y, w;
    // Node(int _x, int _y, int _w) { x = _x, y = _y, w = _w; } // constructor
    Node(int x, int y, int w): x(x), y(y), w(w) {} // constructor
    bool operator < (const Node &a) const {
        return w < a.w;
    }
    bool operator > (const Node &a) const {
        return w > a.w;
    }
};
int mp[N][N], dist[N][N];
bool visited[N][N];
int dx[] = {1, -1, 0, 0}, dy[] = {0, 0, 1, -1};

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    int t, n, m, w, x, y, nx, ny;
    
    cin >> t;
    while (t--) {
        cin >> n >> m;
        for (int i = 0; i < n; i++) 
            for (int j = 0; j < m; j++){
                cin >> mp[i][j];
            }

        memset(dist, INF, sizeof(dist));
        memset(visited, false, sizeof(visited));

        dist[0][0] = mp[0][0];
        Node node = Node(0, 0, mp[0][0]);
        priority_queue<Node, vector<Node>, greater<Node>> pq;
        pq.push(node);
        while (!pq.empty()) {
            Node u = pq.top(); pq.pop();
            int w = u.w, x = u.x, y = u.y;
            if (dist[x][y] < w) continue;
            if (visited[x][y]) continue;
            visited[x][y] = true;
            for (int i = 0; i < 4; i++) {
                nx = x + dx[i], ny = y + dy[i];
                if (nx >= 0 && nx < n && ny >= 0 && ny < m && !visited[nx][ny]) {
                    dist[nx][ny] = min(dist[nx][ny], w + mp[nx][ny]);
                    pq.push(Node(nx, ny, dist[nx][ny]));
                }
            }
        }
        cout << dist[n - 1][m - 1] << endl;
    }
    return 0;
}