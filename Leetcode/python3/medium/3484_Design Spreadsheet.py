#
# @lc app=leetcode id=3484 lang=python3
#
# [3484] Design Spreadsheet
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Spreadsheet:

    def __init__(self, rows: int):
        self.tbl = [[0] * 26 for _ in range(rows + 1)]

    def setCell(self, cell: str, value: int) -> None:
        r = int(cell[1:])
        c = ord(cell[0]) - ord('A')
        self.tbl[r][c] = value

    def resetCell(self, cell: str) -> None:
        r = int(cell[1:])
        c = ord(cell[0]) - ord('A')
        self.tbl[r][c] = 0
    
    def getCell(self, cell: str) -> int:
        r = int(cell[1:])
        c = ord(cell[0]) - ord('A')
        return self.tbl[r][c]

    def getValue(self, formula: str) -> int:
        cell1, cell2 = formula[1:].split('+')
        x = int(cell1) if cell1.isdigit() else self.getCell(cell1)
        y = int(cell2) if cell2.isdigit() else self.getCell(cell2) 
        return x + y

# @lc code=end

sheet = Spreadsheet(458)
print(sheet.getValue("=O126+10272"))

sheet = Spreadsheet(24)
sheet.setCell("B24", 66688)
sheet.resetCell("O15")

