N, M, P = map(int, input().split(" "))
print((N-M+1)//P+1) if (N-M+1)%P!=0 else print((N-M+1)//P)