n = 8
a = [] # [s1, s2, s3 ... s8]

for x in range(n):
    s = input()
    a.append(s)

x = -1
y = -1

for i in range(n):
    for j in range(len(a[i])):
        if a[i][j] == '*':
            x = i
            y = j

x = n - x
y = chr(ord('a') + y);

print(y, end = '')
print(x, end = '')