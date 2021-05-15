n = int(input())

# 2*n타일로 채우려면 세로의 길이가 2로 정해져 있기 때문에,

# I 모양으로 끝날 때 : A
# L 모양으로 끝날 때 : B
A, B = [0] * (n + 1), [0] * (n + 1)
for i in range(1, n + 1):
    if i == 1:  # 1) 세로로 1개만 넣거나
        A[i] = 0
        B[i] = 1
        continue
    elif i == 2:  # 2) 가로로 2개를 넣으면 된다.
        A[i] = 0
        B[i] = 2
        continue
    elif i == 3:
        A[i] = 2
        continue
    elif i == 4:
        A[i] = 4
    elif i == 5:
        B[i] = 8
        continue
    A[i] = A[i - 1] + A[i - 2] + (B[n-1]*2)
    B[i] = A[i - 2] + B[i - 1]

result = (dp[n] + dp_I[n]) % 10007
print(result)