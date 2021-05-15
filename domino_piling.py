n = int(input())

# 2*n타일로 채우려면 세로의 길이가 2로 정해져 있기 때문에,

# L모양으로 끝날 때 : dp
# I 모양으로 끝날 때 :dp_I
dp = [0] * (n + 1)
dp_I = [0] * (n + 1)
for i in range(1, n + 1):
    if i == 1:  # 1) 세로로 1개만 넣거나
        dp[i] = 0
        dp_I[i] = 1
        continue
    elif i == 2:  # 2) 가로로 2개를 넣으면 된다.
        dp[i] = 0
        dp_I[i] = 2
        continue
    elif i == 3:
        dp[i] = 2
        continue
    elif i == 4:
        dp[i] = 4
    elif i == 5:
        dp[i] = 8
        continue
    dp[i] = dp[i - 2] + dp[i - 3]
    dp_I[i] = dp_I[i - 2] + dp_I[i - 1] + dp[i - 1]

result = (dp[n] + dp_I[n]) % 10007
print(result)