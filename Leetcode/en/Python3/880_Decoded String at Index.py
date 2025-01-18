# @algorithm @lc id=916 lang=python3 
# @title decoded-string-at-index


from en.Python3.mod.preImport import *
# @test("leet2code3",10)="o"
# @test("ha22",5)="h"
# @test("a2345678999999999999999",1)="a"
class Solution:
    def decodeAtIndex(self, s: str, k: int) -> str:
        size = 0 # length of decoded string
        for ch in s:
            if ch.isdigit():
                size *= int(ch)
            else:
                size += 1
        for ch in reversed(s): # 由後往前，縮減長度
            k %= size
            if k == 0 and ch.isalpha():
                return ch
            if ch.isdigit(): # 前面的字串重複int(ch)次，所以長度可以縮減int(ch)倍
                size //= int(ch)
            else:
                size -= 1
        