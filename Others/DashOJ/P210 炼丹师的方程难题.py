class Operand:
    def __init__(self, val, mul = 1):
        self.init = val
        self.val = val
        self.mul = mul
        self.related = []
    
    def __add__(self, other):
        self.val += other.val
        self.related.append(other)
        self.related.extend(other.related)
        return self

    def __mul__(self, other):
        self.val *= other.val
        self.mul *= other.val
        for related in self.related:
            related.mul *= other.val
        self.related.append(other)
        self.related.extend(other.related)
        return self

def parse(s):
    res = []
    cur = None
    for ch in s:
        if ch.isdigit():
            if cur is None:
                cur = 0
            cur = cur * 10 + int(ch)
        else:
            if cur is not None:
                res.append(Operand(cur))
            cur = None
            res.append(ch)
    if cur is not None:
        res.append(Operand(cur))
    return res

def eval(res):
    st = []
    i = 0
    while i < len(res):
        if isinstance(res[i], Operand):
            st.append(res[i])
        elif res[i] == '*':
            st[-1] *= res[i + 1]
            i += 1
        elif res[i] == '+':
            st.append('+')
        i += 1
    result = st[0]
    i = 1
    while i < len(st):
        if st[i] == '+':
            result += st[i + 1]
            i += 2
        else:
            i += 1
    return result

def check(lhs_ops, tgt):
    for op in lhs_ops:
        x = op.init
        for d in range(len(str(x)) + 1):
            q, r = divmod(x, 10 ** d)
            for i in range(10):
                nx = q * 10 ** (d + 1) + i * 10 ** d + r
                if nx * op.mul - x == tgt:
                    return "Yes"
    return "No"

t = int(input().strip())

for _ in range(t):
    s = input().strip()
    lhs, rhs = s.split('=')

    lhs_list = parse(lhs)
    rhs_list = parse(rhs)

    lhs_val = eval(lhs_list)
    rhs_val = eval(rhs_list)

    if lhs_val.val == rhs_val.val:
        print('Yes')
        continue

    lhs_ops = [lhs_val] + lhs_val.related
    rhs_ops = [rhs_val] + rhs_val.related

    if lhs_val.val < rhs_val.val:
        ans = check(lhs_ops, rhs_val.val - lhs_val.val)
    else:
        ans = check(rhs_ops, lhs_val.val - rhs_val.val)
    print(ans)