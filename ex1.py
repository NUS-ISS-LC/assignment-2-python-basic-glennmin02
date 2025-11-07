def find(s, n):
    for i in range (len(s)):
        for j in range (i+1, len(s)):
             if s[i] + s[j] == n:
                 return [i,j]

print (find([1,3,4,5,1,11,4,1],9))