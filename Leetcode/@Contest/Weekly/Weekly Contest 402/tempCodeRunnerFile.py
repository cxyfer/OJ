        if left == l and r == right:
            return self.tree[o]
        mid = (left + right) // 2
        if r <= mid: # 只需要查詢左半部分
            return self.query(2*o, left, mid, l, r)
        if mid < l: # 只需要查詢右半部分
            return self.query(2*o+1, mid + 1, right, l, r)
        left_part = self.query(2*o, left, mid, l, mid)
        right_part = self.query(2*o+1, mid+1, right, mid+1, r)
        return self.merge(left_part, right_part, l, mid, r) # 合併左右兩部分