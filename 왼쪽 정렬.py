import ctypes
W = int(input())

arr = [0] * 1001
psum = [0] * 1001

dp = []
for _ in range(1001):
	line = []
	for _ in range(1001):
		line.append(-1)
	dp.append(line)

def p(a, y):
	x = 1
	while(y):
		#print(int(y) & 1)
		if (int(y) & 1):
			x *= a
		a *= a
		y /= 2
	return x

def recv(s, e):
	if (s==e):
		dp[s][e] = p((W - arr[s]), 3)
		result = dp[s][e]
		return result
	ret = dp[s][e]
	if (ret != -1):
		return ret

	s_len = e-s
	w_len = psum[e] - psum[s-1]

	if (s_len + w_len <= W):
		ret = p(W - (s_len + w_len), 3)
		return ret

	ret = 1e9
	i = s
	while (i<e):
		ret = min(ret, recv(s, i) + recv(i + 1, e))
		i+=1
	return ret


n = 1
Len = 0
ch = input().split()

for i in range(len(ch)):
	arr[i] = len(ch[i])

n = i
for i in range(1, n):
	psum[i] = psum[i-1] + arr[i]
	i +=1

answer = recv(1, n-1)
print(answer)
