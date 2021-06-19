n = int(input())
A = list(map(int, input().split()))

# 올바른 값이 들어왔는지 확인
while True:
    len_of_A = len(A)
    if len_of_A < 1 or len_of_A > 100000:  # 입력 개수가 조건에 맞지 않으면
        print('입력은 1~100,000개의 정수 범위 내에서 가능합니다. 다시 입력하세요.')
        del A  # 삭제 후
        A = [int(x) for x in input().split()]  # 다시 입력받기
        continue  # 새로 입력받은 A에 대해 다시 조건을 확인한다.
    else:  # 입력 개수가 맞다면 입력된 수의 범위도 확인
        for x in A:
            if (x < -100000) or (x > 100000):  # 정수가 조건의 범위에 맞지 않으면
                print('입력값은 -100,000부터 100,000범위 내의 정수여야 합니다. 다시 입력하세요.')
                del A  # 삭제 후
                A = [int(x) for x in input().split()]  # 다시 입력받기
                continue  # 새로 입력받은 A에 대해 다시 조건을 확인한다.
        break  # 입력 개수와 입력값의 범위 모두 조건에 맞으면 반복 종료


# 조건을 모두 확인했으면 최대 구간 합을 구함
def find_max_sum(A):
    S = [0] * len_of_A
    S[0] = A[0]
    for i in range(1, len_of_A):
        S[i] = max(S[i - 1] + A[i], A[i])
    return max(S)


print(find_max_sum(A))
