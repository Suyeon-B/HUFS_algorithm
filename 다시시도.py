W = int(input())
ch = input().split()

arr = [0] * 1001
psum = [0] * 1001

dp = []
for _ in range(1001):
	line = []
	for _ in range(1001):
		line.append(0)
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
                if (W - (psum[y] - psum[y - 1] - 1) >= 0):
                    dp[x][y] = (W - (psum[y] - psum[y-1] - 1)) ** 3
            else:
                if (W - psum[y] >= 0):
                    dp[x][y] = (W - psum[y]) ** 3
        elif (x < y) :
            if (x > 0):
                if (W - (psum[y] - psum[x-1] - 1) >= 0):
                    dp[x][y] = (W - (psum[y] - psum[x-1] - 1)) ** 3
            else:
                if (W - psum[y] >= 0):
                    dp[x][y] = (W - psum[y]) ** 3

i, j = len(ch)-1, len(ch)-1
result = [0]*len(ch)
while(True):
    if i<0 or j<0:
        break
    if (dp[i][j] > dp[i-1][j]) or (dp[i][j] > dp[i - 2][j - 2] + dp[i - 1][j]):
        result[i] = dp[i - 1][j]
        if (dp[i][j] > dp[i-1][j]):
            i -= 1
        else:
            i -= 2
            j = i
    elif dp[i][j] < dp[i - 2][j - 2] + dp[i - 1][j]:
        result[i] = dp[i][j]
        i -= 1
        j = i

answer = 0
for i in range(len(result)):
    answer += result[i]
print(answer)
