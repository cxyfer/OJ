"""
    tags: string, palindrome, 紫書-Ch3, CPE-140325
"""
mp = "A   3  HIL JM O   2TUVWXY51SE Z  8 "

while True:
    try:
        s = input()
    except EOFError:
        break
    n = len(s)
    flag1 = (s == s[::-1]) # is a palindrome
    flag2 = True
    for i in range(n//2+1):
        if s[i].isupper():
            idx = ord(s[i]) - ord('A')
        elif s[i].isdigit():
            idx = ord(s[i]) - ord('0') + 25
        else:
            idx = -1
        if idx == -1 or s[n-1-i] != mp[idx]:
            flag2 = False
            break
    print(s, end=" -- is ")
    if not flag1 and not flag2:
        print("not a palindrome.")
    elif flag1 and not flag2:
        print("a regular palindrome.")
    elif not flag1 and flag2:
        print("a mirrored string.")
    else:
        print("a mirrored palindrome.")
    print()