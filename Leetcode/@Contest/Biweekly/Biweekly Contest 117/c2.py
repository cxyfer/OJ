def countOcc(s):
 
    # To store the count of occurrences
    cnt = 0
 
    # Check first four characters from ith position
    for i in range(0, len(s) - 3): 
 
        # Variables for counting the required characters
        c, l, a, p = 0, 0, 0, 0
 
        # Check the four contiguous characters
        # which can be reordered to form 'clap'
        for j in range(i, i + 4): 
             
            if s[j] == 'c':
                c += 1
         
            elif s[j] == 'l':
                l += 1
                 
            elif s[j] == 'a':
                a += 1
                 
            elif s[j] == 'p':
                p += 1
 
        # If all four contiguous characters are
        # present then increment cnt variable
        if c == 1 and l == 1 and a == 1 and p == 1:
            cnt += 1
         
    return cnt
     
# Driver code
if __name__ == "__main__":
     
    s = "calap"
    print(countOcc(s.lower()))