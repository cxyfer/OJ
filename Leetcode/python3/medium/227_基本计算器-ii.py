#
# @lc app=leetcode.cn id=227 lang=python3
#
# [227] 基本计算器 II
#
from preImport import *
# @lc code=start
class Solution:
    """
        Infix to Postfix
    """
    def calculate(self, s: str) -> int:
        postfix = self.infixToPostfix(s)  # 轉後綴表達式
        return self.evalPostfix(postfix)

    def priority(self, op: str) -> int: # operator priority
        if op in ['+', '-']:
            return 1
        elif op in ['*', '/']:
            return 2
        return 0
    
    def infixToPostfix(self, s: str) -> List[str]: # 中綴表達式轉後綴表達式
        n = len(s)
        res = []
        st = []
        num = None # 累加數字，None 表示當前沒有數字
        for i, ch in enumerate(s):
            if ch == ' ':
                continue
            if ch.isdigit(): # 遇到數字，進行累加
                if num is None:
                    num = int(ch)
                else:
                    num = num * 10 + int(ch)
            else: # 遇到 operator ，將數字加入到結果中
                if num is not None:
                    res.append(str(num))
                    num = None
                # 處理 unary operator，將 (-x) 轉換為 (0-x)
                elif num is None and ch == '-' and ((st and st[-1] == '(') or not res):
                    res.append('0')
                if ch in ['+', '-', '*', '/']:
                    while st and st[-1] != '(' and self.priority(st[-1]) >= self.priority(ch):
                        res.append(st.pop())
                    st.append(ch) # 當前操作符入棧
                elif ch == '(': # 遇到左括號，直接入棧
                    st.append(ch)
                elif ch == ')': # 遇到右括號，將出棧元素加入到結果中，直到遇到左括號
                    while st and st[-1] != '(': 
                        res.append(st.pop())
                    st.pop() # 左括號出棧
                # print(i, ch, res, st) 
        if num is not None: # 如果有數字，將數字加入到結果
            res.append(str(num))
        while st: # 棧中的其他元素加入到結果中
            res.append(st.pop())
        return res

    
    def evalPostfix(self, tokens: List[str]) -> int: # Same to LC 150. Evaluate Postfix Expression
        st = []
        for token in tokens:
            if token in ['+', '-', '*', '/']:
                a = int(st.pop())
                b = int(st.pop())
                if token == '+':
                    st.append(b + a)
                elif token == '-':
                    st.append(b - a)
                elif token == '*':
                    st.append(b * a)
                elif token == '/':
                    st.append(int(b / a))
            else:
                st.append(int(token))
        return st[-1]
# @lc code=end

