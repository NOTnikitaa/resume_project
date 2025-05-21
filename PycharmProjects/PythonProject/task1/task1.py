n = int(input())
m = int(input())
s = m * [int(i) for i in range(1,n+1)]

count = 0
s2 = []
for i in range(len(s)):
    s2.append(s[i])

    if len(s2) % m == 0:
        s2.append(s[i])

print(s2)

s3 = []

for i in range(0,len(s),m):
    s3.append(s2[i])
    if s2[i] == 1 and i != 0:
        print(*s3)
        break

if s3[-1] == 1:
    del s3[-1]

print(*s3)

