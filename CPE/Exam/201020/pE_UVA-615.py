""" UVA-615 Is It A Tree?
    找到唯一可能的樹根後， DFS 檢查是否有環以及是否所有節點都被訪問到
    CPE 上的題目敘述不一樣，要輸出樹根
    已於 UVA, CPE, ZeroJudge 測試通過
"""
CPE = False

from collections import defaultdict
import sys
buf = sys.stdin.read().split()
cin = lambda: buf.pop(0)

def dfs(u):
    visited.add(u)
    for v in g[u]:
        if v in visited:
            return False
        if not dfs(v):
            return False
    return True

kase = 1
while True:
    u, v = map(int, [cin(), cin()])
    if u < 0  and v < 0:
        break
    nodes = set()
    g = defaultdict(list)
    indeg = defaultdict(int)
    while u and v:
        nodes.add(u)
        nodes.add(v)
        g[u].append(v)
        indeg[v] += 1
        u, v = map(int, [cin(), cin()])
    st = -1
    for u in nodes:
        if indeg[u] == 0:
            if st != -1: # more than one node with indegree 0
                st = -1
                break
            st = u
    flag = True
    if len(nodes) == 0: # empty graph also a tree
        flag = True
    elif st == -1: # no node with indegree 0 / more than one node with indegree 0
        flag = False
    else:
        visited = set()
        flag = dfs(st)
        if len(visited) != len(nodes):
            flag = False
    if CPE:
        if flag:
            print(f"Case {kase} is a tree. Root is {st}.")
        else:
            print(f"Case {kase} is not a tree.")
    else:
        print(f"Case {kase} is{' not' if not flag else ''} a tree.")
    kase += 1
