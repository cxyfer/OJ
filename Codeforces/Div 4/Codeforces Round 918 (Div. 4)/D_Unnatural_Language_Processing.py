T = int(input())

vowels = ['a', 'e']
consonants = ['b', 'c', 'd']

for tc in range(1, T+1):
    N = int(input())
    S = input()
    res = []
    """
        CV / CVC
        考慮 CVC
        - CV.CV
        - CV.CVC
        - CVC.CV
        - CVC.CVC
        往後看4個，若看到CVCV則一定是CV，或是看到CVCC則一定是CVC
    """
    i = 0
    while i < N:
        if S[i] in consonants:
            if i+3 >= N: # 剩下的字母<=3個，則不用管是CV還是CVC，直接加入即可
                res.append(S[i:])
                break
            if i+1 < N and S[i+1] in vowels and i+2 < N and S[i+2] in consonants and i+3 < N and S[i+3] in consonants:
                res.append(S[i:i+3])
                i += 3
            else:
                res.append(S[i:i+2])
                i += 2
    print('.'.join(res))
