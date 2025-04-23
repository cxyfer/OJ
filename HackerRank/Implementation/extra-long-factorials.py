#
# Complete the 'extraLongFactorials' function below.
#
# The function accepts INTEGER n as parameter.
#

MAX_N = 100
fact = [1] * (MAX_N + 1)
for x in range(2, MAX_N + 1):
    fact[x] = fact[x - 1] * x
def extraLongFactorials(n):
    # Write your code here
    print(fact[n])