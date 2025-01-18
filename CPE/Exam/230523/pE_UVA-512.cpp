/*
    模擬(Simulation)
    由於要求原座標經過操作後的位置，因此可以讓原本的表格中保存原座標的位置，
    這樣在經過表格操作後，只要遍歷表格，就能找出原座標的新位置。
*/
#include <bits/stdc++.h>
using namespace std;
#define endl '\n';

class Sheet {
    int r, c;
    vector<vector<pair<int, int>>> tbl;
public:
    Sheet(int r, int c) : r(r), c(c) {
        tbl = vector<vector<pair<int, int>>>(r, vector<pair<int, int>>(c));
        for (int i = 0; i < r; i++) {
            for (int j = 0; j < c; j++) {
                tbl[i][j] = {i+1, j+1};
            }
        }
    }
    void DR(vector<int> target) {
        for (int i: target) {
            tbl.erase(tbl.begin()+i);
        }
        r -= target.size();
    }
    void DC(vector<int> target) {
        for (int i = 0; i < r; i++) {
            for (int j: target) {
                tbl[i].erase(tbl[i].begin()+j);
            }
        }
        c -= target.size();
    }
    void IR(vector<int> target) {
        for (int i: target) {
            tbl.insert(tbl.begin()+i, vector<pair<int, int>>(c, {0, 0}));
        }
        r += target.size();
    }
    void IC(vector<int> target) {
        for (int i = 0; i < r; i++) {
            for (int j: target) {
                tbl[i].insert(tbl[i].begin()+j, {0, 0});
            }
        }
        c += target.size();
    }
    void EX(vector<int> pos) {
        int r1 = pos[0], c1 = pos[1], r2 = pos[2], c2 = pos[3];
        swap(tbl[r1][c1], tbl[r2][c2]);
    }
    void query(int x, int y) {
        for (int i = 0; i < r; i++) {
            for (int j = 0; j < c; j++) {
                if (tbl[i][j] == make_pair(x, y)) {
                    cout << "Cell data in (" << x << "," << y << ") moved to (" << i+1 << "," << j+1 << ")" << endl;
                    return;
                }
            }
        }
        cout << "Cell data in (" << x << "," << y << ") GONE" << endl;
        return;
    }
};

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    int kase = 1, r, c, m, n, x, y, argc;
    while (cin >> r >> c && (r || c)){
        Sheet sheet(r, c);
        cin >> n;
        while (n--){
            // Read command
            string cmd;
            cin >> cmd;
            vector<int> args;
            if (cmd == "EX"){
                for (int i = 0; i < 4; i++){
                    cin >> x;
                    args.push_back(x-1);
                }
            } else {
                cin >> argc;
                for (int i = 0; i < argc; i++){
                    cin >> x;
                    args.push_back(x-1);
                }
            }
            // sort in descending order
            if (cmd != "EX"){
                sort(args.begin(), args.end(), greater<int>());
            }
            // Process command
            if (cmd == "DR") sheet.DR(args);
            else if (cmd == "DC") sheet.DC(args);
            else if (cmd == "IR") sheet.IR(args);
            else if (cmd == "IC") sheet.IC(args);
            else if (cmd == "EX") sheet.EX(args);
        }
        // Output & Query
        if (kase > 1) cout << endl;
        cout << "Spreadsheet #" << kase++ << endl;
        cin >> m;
        while (m--){
            cin >> x >> y;
            sheet.query(x, y);
        }
    }
    return 0;
}