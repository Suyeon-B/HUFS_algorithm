"""
<알고리즘 설명>
아래 세 가지 함수를 구현하여 해결했습니다.

1. slice(A)
: 리스트를 처음부터 하나씩 살피며 0이 나왔을 때,
다음 수도 0이 아닌 경우에 해당 인덱스까지 잘라서
temp 리스트에 저장하고 인덱스와 함께 리턴합니다.

2. JUMPABLE(A, temp, slice_idx)
: 잘라진 temp 리스트의 요소를 뒤에서부터 확인해서,
0을 넘길 수 있는 숫자들로 구성되어 있다면 True를,
넘길 수 없다면 False를 리턴합니다.

3. JUMP
: 1, 2번 함수를 반복하면서
리스트 A 끝까지 점프가 가능한지 판단하고 결과를 리턴합니다.


<수행시간>
한번씩 리스트의 원소들을 살펴보고 판단하므로,
총 O(n)만큼의 시간이면 구할 수 있습니다.
상세 표기는 아래 추가했습니다.

"""

def slice(A):
    temp = []
    for i in range(len(A) - 1): # O(n) + O(c) = O(n) - c는 상수
        if A[i] == 0 and A[i + 1] != 0: # 연속으로 0이 나온다면 맨 마지막 0까지 해서 자름
            temp = A[:i+1]
            slice_idx = i+1
            return temp, slice_idx
        else:
            continue
    if temp == []: # 만약 자를 곳이 없다면
        temp = A[:]
        slice_idx = len(A)  # O(c) - c는 상수
        return temp, slice_idx # A를 복사해서 리턴


def JUMPABLE(A, temp, slice_idx):
    size = len(A) # O(c) - c는 상수
    slice_size = len(temp) # O(c) - c는 상수
    count = 0
    for j in range(slice_size-2, 0, -1): # O(n) / 뒤에서 부터 0을 넘길 수 있는지 판단
        if slice_size == size:  # 잘리지 않고 A 그대로 복사한 temp라면
            if temp[j] >= count or slice_size == 1: # 최종적으로 0을 넘을 수 있거나, 넘을 필요가 없다면
                return True # True
            else:
                slice_size -= 1
                size -= 1
                count += 1
                continue
        else:  # 잘려 온 파트이면
            if temp[j] > slice_size-1: # 넘길 수 있다면 다음 잘린 조각으로 temp를 변경
                temp = A[slice_idx:]
                return temp
            else:
                slice_size -= 1
                continue
    return False


def JUMP(A):
    temp, slice_idx = slice(A)
    result = JUMPABLE(A, temp, slice_idx)
    while True:
        if result == True:
            return True
        elif result == False:
            return False
        else: # 마지막까지 검사될 때 까지 반복한다.
            temp, slice_idx_plus = slice(result)
            if temp == result:
                return True
            slice_idx += slice_idx_plus
            result = JUMPABLE(A, temp, slice_idx)
            if result == False:
                return True
            if len(result) == 1:
                return True

A = [int(x) for x in input().split()]
print(JUMP(A))