"""
왼쪽, 오른쪽, 가운데의 최대구간 합을 구해서
그 셋 중의 max값을 구하면 됩니다.

우선 바닥조건으로 시작 index인 L과 끝 index R이 같아지는, 즉 값이 하나만 남은 지점에서 리턴하도록 해줍니다.

그 다음
최대 구간 합이 왼쪽과 오른쪽에 걸친 부분을 계산해줍니다.
걸친 부분은 L과 R의 절반인 M인덱스에 있고, 반드시 그 부분을 포함한 최대 구간을 찾아야합니다.
그래서 M의 왼쪽 부분과 오른쪽 부분을 더해가며 max값을 찾습니다.

양쪽 반 구간은,
L과 R 부분 각각 인덱스를 늘려가며 더해준 수와 더하기 이전의 수 중에 max값을 찾아서 재귀적으로 업뎃하면서 구하면 됩니다.

따라서 점화식은 T(n) = 2T(n/2) + cn 이고,
O(nlogn)시간에 가능합니다.
"""

def max_interval(A, L, R):
    if L == R:
        return A[L]
    middle = (L + R) // 2

    # m을 포함한 최대 구간
    curr_sum = 0
    L_side = -1000000000
    index = middle
    while index >= L:
        curr_sum += A[index]
        L_side = max(L_side, curr_sum)
        index -= 1

    curr_sum = 0
    R_side = -1000000000
    index = middle+1
    while index <= R:
        curr_sum += A[index]
        R_side = max(R_side, curr_sum)
        index += 1

    M = L_side + R_side

    # L, R에 최대구간이 있을 때
    L_max = max_interval(A, L, middle)
    R_max = max_interval(A, middle + 1, R)

    return max(L_max, M, R_max)


A = [int(x) for x in input().split()]
print(max_interval(A, 0, len(A)-1))