import sys
import math
from collections import defaultdict

def main():
    import sys
    import sys
    import sys
    def input():
        return sys.stdin.read()
    
    data = input().split()
    idx = 0
    T = int(data[idx])
    idx +=1
    for _ in range(T):
        n = int(data[idx])
        idx +=1
        a = list(map(int, data[idx:idx+n]))
        idx +=n
        b = list(map(int, data[idx:idx+n]))
        idx +=n
        
        # Compute prefix_gcd_a and prefix_gcd_b
        prefix_gcd_a = [0]*(n+1)
        prefix_gcd_b = [0]*(n+1)
        for i in range(1, n+1):
            prefix_gcd_a[i] = math.gcd(prefix_gcd_a[i-1], a[i-1])
            prefix_gcd_b[i] = math.gcd(prefix_gcd_b[i-1], b[i-1])
        
        # Compute suffix_gcd_a and suffix_gcd_b
        suffix_gcd_a = [0]*(n+1)
        suffix_gcd_b = [0]*(n+1)
        for i in range(n-1, -1, -1):
            suffix_gcd_a[i] = math.gcd(a[i], suffix_gcd_a[i+1])
            suffix_gcd_b[i] = math.gcd(b[i], suffix_gcd_b[i+1])
        
        res = []  # List of tuples (g1, g2, l)
        mx = 0
        cnt = 0
        for i in range(n):
            new_res = []
            # Update existing tuples
            for (g1, g2, l) in res:
                updated_g1 = math.gcd(g1, b[i])
                updated_g2 = math.gcd(g2, a[i])
                new_res.append( (updated_g1, updated_g2, l) )
            # Add new tuple with only current position swapped
            g1_new = math.gcd(prefix_gcd_a[i], b[i])
            g2_new = math.gcd(prefix_gcd_b[i], a[i])
            new_res.append( (g1_new, g2_new, i) )
            # Deduplicate: keep only the last occurrence of each (g1, g2)
            dedup_res = []
            seen = set()
            for tup in reversed(new_res):
                key = (tup[0], tup[1])
                if key not in seen:
                    seen.add(key)
                    dedup_res.append(tup)
            dedup_res = dedup_res[::-1]  # Reverse back to original order
            res = dedup_res
            # Now, iterate res from end to start to calculate s and update mx and cnt
            prePos = i +1
            for (g1, g2, l) in reversed(res):
                # Compute s = gcd(g1, suffix_gcd_a[i+1]) + gcd(g2, suffix_gcd_b[i+1])
                # Handle i+1 ==n case where suffix_gcd_a[n] =0, so gcd(g1,0)=g1
                if i+1 <n:
                    s = math.gcd(g1, suffix_gcd_a[i+1]) + math.gcd(g2, suffix_gcd_b[i+1])
                else:
                    s = g1 + g2
                if s > mx:
                    mx = s
                    cnt = prePos - l
                elif s == mx:
                    cnt += prePos - l
                prePos = l
        print(mx, cnt)

if __name__ == "__main__":
    main()
