#include <bits/stdc++.h>
using namespace std;
#define endl '\n'

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    int kase = 1;
    char mp[5][5];
    string line, cmd;
    map<char, int> DIR_X = {{'A', -1}, {'B', 1}, {'L', 0}, {'R', 0}};
    map<char, int> DIR_Y = {{'A', 0}, {'B', 0}, {'L', -1}, {'R', 1}};
    while (1) {
        int x = 0, y = 0;
        bool flag1 = false;
        for (int i = 0; i < 5; i++) {
            getline(cin, line); // input a line
            if (line == "Z") {
                flag1 = true;
                break;
            }
            for (int j = 0; j < line.size(); j++) {
                mp[i][j] = line[j];
                if (mp[i][j] == ' ') {
                    x = i;
                    y = j;
                }
            }
        }
        if (flag1) {
            break;
        }
        cmd = "";
        while (1) {
            getline(cin, line);
            cmd += line;
            if (line[line.size() - 1] == '0') {
                break;
            }
        }
        if (kase > 1) cout << endl;
        cout << "Puzzle #" << kase++ << ":" << endl;
        bool flag2 = false; // no final configuration
        for (char ch : cmd) {
            if (ch != '0' && DIR_X.find(ch) == DIR_X.end()) { // invalid command
                flag2 = true;
                break;
            }
            int nx = x + DIR_X[ch];
            int ny = y + DIR_Y[ch];
            if (nx >= 0 && nx < 5 && ny >= 0 && ny < 5) {
                swap(mp[x][y], mp[nx][ny]);
                x = nx, y = ny;
            } else {
                flag2 = true;
                break;
            }
        }
        if (flag2) {
            cout << "This puzzle has no final configuration." << endl;
            continue;
        } else {
            for (int i = 0; i < 5; i++) {
                for (int j = 0; j < 5; j++) {
                    cout << mp[i][j] << (j < 4 ? " " : "");
                }
                cout << endl;
            }
        }
    }
    return 0;
}