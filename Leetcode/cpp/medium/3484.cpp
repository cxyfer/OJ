/*
 * @lc app=leetcode.cn id=3484 lang=cpp
 * @lcpr version=30204
 *
 * [3484] 设计电子表格
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Spreadsheet {
public:
    vector<vector<int>> tbl;
    Spreadsheet(int rows) {
        tbl = vector<vector<int>>(rows + 1, vector<int>(26));
    }
    
    void setCell(string cell, int value) {
        int r = stoi(cell.substr(1));
        int c = cell[0] - 'A';
        tbl[r][c] = value;
    }
    
    void resetCell(string cell) {
        int r = stoi(cell.substr(1));
        int c = cell[0] - 'A';
        tbl[r][c] = 0;
    }
    
    int getCell(string cell) {
        int r = stoi(cell.substr(1));
        int c = cell[0] - 'A';
        return tbl[r][c];
    }
    
    int getValue(string formula) {
        int idx = formula.find('+');
        string x1 = formula.substr(1, idx - 1);
        string x2 = formula.substr(idx + 1);
        return (isalpha(x1[0]) ? getCell(x1) : stoi(x1)) + (isalpha(x2[0]) ? getCell(x2) : stoi(x2));
    }
};
// @lc code=end

int main() {
    Spreadsheet obj = Spreadsheet(5);
    obj.setCell("A1", 1);
    obj.setCell("B2", 2);
    cout << obj.getValue("A1+B2") << endl;
    return 0;
}

/*
// @lcpr case=start
// 5+7"], ["A1", 10]\nA1+6"], ["B2", 15]\nA1+B2"], ["A1"]\nA1+B2"]]\n
// @lcpr case=end

 */

