while True:
    I = int(input())
    if I == 0:
        break
    print(f"The parity of {bin(I)[2:]} is {bin(I).count('1')} (mod 2).")