s = input()
contest_id = int(s[3:])
print("Yes" if 1 <= contest_id <= 349 and contest_id != 316 else "No")