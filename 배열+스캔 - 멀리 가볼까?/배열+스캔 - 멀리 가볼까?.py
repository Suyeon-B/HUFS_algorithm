# 0을 기준으로 왼쪽 값들을 차례로 검사하여,
# (모든 0에 대하여) 0의 왼쪽값들과 0의 인덱스 차이 < 해당 인덱스의 값 이면
# Jump하여 끝까지 도달할 수 있고,
# 반대의 경우라면 도달할 수 없다.

def JUMP(A):
    size = len(A)
    zero = 0
    zero_idx = []
    for i in range(size):
        if A[i] == 0:
            zero += 1
            zero_idx.append(i)

    temp = list(zero_idx)
    for i in range(zero-1):
        if temp[i]+1 == temp[i+1]:
            zero_idx.pop(i)
            zero -= 1



    for i in range(zero):
        count = zero_idx[i]
        start = i
        while True:
            if A[start] <= zero_idx[i]-start:
                if start+1 == size-1:
                    return True
                if count > 0 :
                    count -= 1
                    start += 1
                    continue
                else:
                    return False
            else:
                break
    return True



A = [int(x) for x in input().split()]
print(JUMP(A))