#
# @lc app=leetcode id=2115 lang=python3
#
# [2115] Find All Possible Recipes from Given Supplies
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        g = defaultdict(list)
        indeg = defaultdict(int)
        for recipe, ingredient in zip(recipes, ingredients):
            for ing in ingredient:
                g[ing].append(recipe)
                indeg[recipe] += 1
        q = deque(supplies)
        while q:
            u = q.popleft()
            for v in g[u]:
                indeg[v] -= 1
                if indeg[v] == 0:
                    q.append(v)
        return [recipe for recipe in recipes if indeg[recipe] == 0]
# @lc code=end

