s=input()

x=1
r1=-1
r2=-1
b1=-1
b2=-1
k=-1
for i in range(len(s)):
    if s[i] == 'R' and r1 == -1:
        r1=i
    elif s[i] == 'R' and r1 != -1:
        r2=i
    if s[i] == 'B' and b1 ==-1 :
        b1=i
    elif s[i] == 'B' and b1 != -1:
        b2=i
    if s[i] == 'K' :
        k=i

if b1%2==0 and b2%2==0 :
    x=-1
elif b1%2!=0 and b2%2!=0 :
    x=-1
if k>r2 or k<r1 :
    x=-1

if x==1:
    print("Yes")
else:
    print("No")

'''
n, k = map(int, input().split())
a = list(map(int, input().split()))
 
ans = -1
 
for i in range(1, n):
    if a[i] - a[i - 1] <= k:
        ans = a[i]
        break
 
print(ans)
'''