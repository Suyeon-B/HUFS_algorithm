W = int(input())
ch = input().split()

arr = [0] * 1001
psum = [0] * 1001

dp = []
for _ in range(1001):
	line = []
	for _ in range(1001):
		line.append(-1)
	dp.append(line)

for i in range(len(ch)):
    arr[i] = len(ch[i])

n = len(ch)
psum[0] = arr[0]
for i in range(1, n):
    psum[i] = psum[i-1] + arr[i] + 1
    i += 1

for x in range(len(ch)):
    for y in range(len(ch)):
        if (x == y):
            if (x > 0):
                dp[x][y] = (W - (psum[y] - psum[y-1] - 1)) ** 3
            else:
                dp[x][y] = (W - psum[y]) ** 3
        elif (x < y) :
            if (x > 0):
                dp[x][y] = (W - (psum[y] - psum[x-1] - 1)) ** 3
            else:
                dp[x][y] = (W - psum[y]) ** 3
                continue

result = 0
x, y = 0, 0
while (True):
    if (x == len(ch)) and (y == len(ch)):
        break
    if (x <= y) and (dp[x][y] > 0):
        if ((dp[x][y] > dp[x][y+1]) and (dp[x][y+1] > 0)):
            result += dp[x][y+1]
            x, y = y + 2, y + 2
        else:
            result += dp[x][y]
            x, y = y+1, y+1
    else:
        continue

print(result)
