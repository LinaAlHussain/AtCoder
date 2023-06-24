n,d = map(int, input().split())
t = list(map(int, input().split()))
 
result = "-1"
for i in range(1,len(t)):
    x = t[i] - t[i-1]
    if x <= d:
        result = t[i]
        break
print(result)

'''
s = input()
 
R = False
K = False
B1 = -1
B2 = -1
 
for i in range(len(s)):
    if s[i] == 'B':
        if B1 == -1:
            B1 = i % 2
        else:
            B2 = i % 2
    if s[i] == 'R':
        R = not R
    if s[i] == 'K':
        if R is True:
            K = True
 
if K is True and B1 != B2:
    print('Yes')
else:
    print('No')
'''