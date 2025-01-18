kuti = 1e7
lakh = 1e5
hajar = 1e3
shata = 1e2

def bangla(n):
    if n >= kuti:
        bangla(n // kuti) # recursive
        print(" kuti", end="")
        n %= kuti
    if n >= lakh:
        print(" %d lakh" % (n // lakh), end="")
        n %= lakh
    if n >= hajar:
        print(" %d hajar" % (n // hajar), end="")
        n %= hajar
    if n >= shata:
        print(" %d shata" % (n // shata), end="")
        n %= shata
    if n:
        print(" %d" % n, end="")

tc = 1
while True:
    try:
        n = int(input())
    except EOFError:
        break
    print(f"{tc:>4}.", end="")
    if n == 0:
        print(" 0")
    else:
        bangla(n)
        print()
    tc += 1