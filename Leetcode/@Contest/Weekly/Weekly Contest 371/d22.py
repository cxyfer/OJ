class TrieNode:
    def __init__(self):
        self.children = {}


def findMaximumXOR(nums):
    # 构建前缀树
    root = TrieNode()
    for num in nums:
        node = root
        for i in range(31, -1, -1):  # 从最高位到最低位遍历
            bit = (num >> i) & 1
            if bit not in node.children:
                node.children[bit] = TrieNode()
            node = node.children[bit]

    max_xor = 0

    # 遍历每个数，更新最大异或结果
    for num in nums:
        node = root
        curr_xor = 0
        for i in range(31, -1, -1):
            bit = (num >> i) & 1
            # 如果当前位为 1，则尽量选择与当前位不同的子节点
            if 1 - bit in node.children:
                node = node.children[1 - bit]
                curr_xor |= (1 << i)
            else:
                node = node.children[bit]
        max_xor = max(max_xor, curr_xor)

    return max_xor


# 示例用法
print(findMaximumXOR([1,2,3,4,5]))
print(findMaximumXOR([10,100])) # 0
print(findMaximumXOR([5,6,25,30])) # 7
print(findMaximumXOR([1,2,2,1,2])) # 3