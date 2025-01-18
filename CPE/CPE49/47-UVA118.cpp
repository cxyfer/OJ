#include <bits/stdc++.h>
using namespace std;
using LL = long long;
const int N = 55;
#define endl '\n'

vector<int> DIR_X = {0, 1, 0, -1};
vector<int> DIR_Y = {1, 0, -1, 0};
map <char, int> DIR_MAP = {{'N', 0}, {'E', 1}, {'S', 2}, {'W', 3}};
string DIR = "NESW";

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);

    int X, Y, x, y, nx, ny;
    char d;
    string s;
    bool scent[N][N] = {0};

    cin >> X >> Y;
    while (cin >> x >> y >> d){
        cin >> s;
        d = DIR_MAP[d];
        bool lost = false;

        for (auto &ch: s){
            if (ch == 'F'){ // Forward
                nx = x + DIR_X[d];
                ny = y + DIR_Y[d];
                if (nx < 0 || nx > X || ny < 0 || ny > Y){ // Out of bound
                    if (!scent[x][y]){
                        scent[x][y] = true;
                        lost = true;
                        break;
                    }
                } else { // In bound
                    x = nx;
                    y = ny;
                }
            } else if (ch == 'L'){
                d = (d - 1 + 4) % 4;
            } else if (ch == 'R'){
                d = (d + 1) % 4;
            }
        }
        cout << x << " " << y << " " << DIR[d] << (lost ? " LOST" : "") << endl;
    }
    return 0;
}