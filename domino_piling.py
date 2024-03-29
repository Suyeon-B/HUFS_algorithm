n = int(input())

# I 모양으로 끝날 때 : A
# L 모양으로 끝날 때 : B
A, B = [0] * (n + 1), [0] * (n + 1)
for i in range(1, n + 1):
    if i == 1:
        A[i] = 1
        continue
    elif i == 2:
        A[i] = 2
        B[i] = 1
        continue
    A[i] = A[i-1] + A[i-2] + 2*B[i-1]
    B[i] = A[i-2] + B[i-1]

result = A[n]
print(result)

# 도미노의 맨 끝이 I 모양으로 끝날 때와 L 모양으로 끝날 때로 나누어 풀었습니다.

# A[n] : I 모양과 L 모양 도미노로 2*n 판을 채우는 경우의 수
# 1) I 모양으로 끝날 때
#   (1) 세로로 세운 I 모양 하나로 끝날 때
#       : 마지막 도미노를 제외한 앞쪽 부분 n-1만큼을 채워야 함. -> A[n-1]
#   (2) 가로로 눕힌 I 모양 두 개로 끝날 때
#       : 마지막 도미노를 제외한 앞쪽 부분 n-2만큼을 채워야 함. -> A[n-2]
# 2) L 모양으로 끝날 때
#   (1) ㄱ자로 끝날 때
#       : 마지막 도미노를 제외한 앞쪽 부분 n-1만큼을 채워야 함. -> B[n-1]
#   (2) L자로 끝날 때
#       : 마지막 도미노를 제외한 앞쪽 부분 n-1만큼을 채워야 함. -> B[n-1]

# B[n] : 끝 부분이 모두 채워지지 않은 형태(L 모양 도미노로 인해서)로 끝나도록 판을 채우는 경우의 수
# 1) L 모양으로 끝날 때
#   = A[n-2] -> L 모양 도미노로 인해 앞 부분이 A[n-2]와 같아진다.
# 2) I 모양이 가로로 눕혀진 형태로 끝날 때
#   = B[n-1] -> 가로로 눕혀진 I 모양 도미노로 인해 앞 부분이 B[n-1]과 같아진다.

# 따라서, A[n]을 구하는 점화식은 아래와 같습니다.
# A[n] = A[n-1] + A[n-2] + 2*B[n-1]