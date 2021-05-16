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

def recv(s, e):
	if (s==e):
		dp[s][e] = (W - arr[s])**3
		return dp[s][e]

	temp = dp[s][e]
	if (temp != -1):
		return temp

	s_len = e-s
	w_len = psum[e] - psum[s-1]

	if (s_len + w_len <= W):
		ret = (W - (s_len + w_len))**3
		return ret

	ret = 1e9
	i = s
	while (i < e):
		ret = min(ret, recv(s, i) + recv(i + 1, e))
		i+=1
	return ret

for i in range(len(ch)):
	arr[i] = len(ch[i])

n = len(ch)
psum[0] = arr[0]
for i in range(1, n):
	psum[i] = psum[i-1] + arr[i]
	i += 1

answer = recv(1, n-1)
print(answer)
