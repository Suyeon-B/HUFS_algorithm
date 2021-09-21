# 끝에서 0이 아닌 2번째 수를 기준으로 한다.
# 우선 끝에서 0이 아닌 2번째 수에서 마지막까지 도달할 수 있는가를 판단해서,
# 불가능하면 False, 가능하면 다음 단계를 확인한다.
# 끝에서 0이 아닌 2번째 수로 도달할 수 있는 앞 인덱스의 값이 있는가를 판단한다. (인덱스 0이 될 때 까지 확인한다.)
def JUMP(A):
    current_idx = -1
    size = len(A)
    is_second = 0
    # 끝에서 0이 아닌 2번째 수를 기준으로 한다.
    for i in range(size-1, 0, -1):
        if A[i] != 0:
            is_second += 1
            if is_second == 2:
                current_idx = i
                break


    while True:
        # 우선 끝에서 0이 아닌 2번째 수에서 마지막까지 도달할 수 있는가를 판단해서,
        remain_behind_idx = size - current_idx -1

        if A[current_idx] < remain_behind_idx: # 못간다면 False를 출력하고,
            return False
        else: # 갈 수 있다면 다시 앞쪽을 살핀다.
            if A[current_idx-A[current_idx]] >= current_idx-A[current_idx]:
                current_idx = current_idx-A[current_idx]
            else:
                return False
            # 안되는 수 앞에도 가능함을 고려해야함



A = [int(x) for x in input().split()]
print(JUMP(A))