# 0을 기준으로 왼쪽 값들을 차례로 검사하여,
# (모든 0에 대하여) 0의 왼쪽값들과 0의 인덱스 차이 < 해당 인덱스의 값 이면
# Jump하여 끝까지 도달할 수 있고,
# 반대의 경우라면 도달할 수 없다.

def JUMP(A):
    jump_coin = A[0]
    start = 0
    while True:
        if jump_coin == len(A)-1:
            return True
        if A[start] == 0:
            return False

        if A[jump_coin] == 0:
            start += 1
            jump_coin = A[start] + start
        else:
            start = A.index(A[jump_coin])
            jump_coin += A[start]
            continue







A = [int(x) for x in input().split()]
print(JUMP(A))