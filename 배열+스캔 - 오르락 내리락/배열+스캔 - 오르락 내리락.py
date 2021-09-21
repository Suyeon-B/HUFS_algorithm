"""
<알고리즘 설명>
짝수 인덱스에는 상대적으로 작은 수,
홀수 인덱스에는 상대적으로 큰 수를 배치하면
주어진 조건에 맞는 리스트를 만들 수 있습니다.

우선 입력된 리스트 자체적으로 조건을 만족하면 바로 리턴하도록 하고,
만족하지 않는다면 아래 방법에 따라 새로 만듭니다.

1) 인덱스가 짝수일 때
: 다음 인덱스보다 작은 수라면 그대로 두고,
크다면 swap해줍니다.

2) 인덱스가 홀수일 때
: 다음 인덱스보다 큰 수라면 그대로 두고,
작다면 swap해줍니다.

<수행시간>
위 두 가지 경우를 통해, 총 O(n)시간으로 조건에 맞는 리스트를 만들 수 있습니다.
상세 분석은 아래에 표기했습니다.

"""

def solve(A):
    B = list(A) # B에 A를 복사한다. - O(n)
    size = len(A) # O(c) - c는 상수
    if check(B) is True: # 입력된 리스트가 이미 조건에 맞는지 체크한다. - O(n)
        return B

    # 조건에 맞지 않는다면 새로 리스트를 만들어준다.
    for i in range(size-1): # 아래 모두 합쳐 총 O(n)
        if i%2 == 0: # 인덱스가 짝수일 때 - O(c)
            if B[i] <= B[i+1]: # 상대적으로 작다면 - O(c)
                continue # 바꿀 필요 없다.
            else: # 크다면
                # swap 해준다. - O(c)
                temp = B[i]
                B[i] = B[i+1]
                B[i+1] = B[i]
        else: # 인덱스가 홀수일 때 - O(c)
            if B[i] >= B[i+1]: # 상대적으로 크다면 - O(c)
                continue # 바꿀 필요 없다.
            else: # 작다면
                # swap 해준다. - O(c)
                temp = B[i]
                B[i] = B[i+1]
                B[i+1] = B[i]

    return B

    



def check(B):
    if not (B[0] <= B[1]): return False
    for i in range(1, len(B) - 1):
        if i % 2 == 1 and not (B[i] >= B[i + 1]):
            return False
        if i % 2 == 0 and not (B[i] <= B[i + 1]):
            return False
    return True


A = [int(x) for x in input().split()]
B = solve(A)
print(check(B))