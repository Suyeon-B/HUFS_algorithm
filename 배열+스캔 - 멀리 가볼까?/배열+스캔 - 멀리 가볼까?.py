
# 0을 기준으로 왼쪽 값들을 차례로 검사하여,
# (모든 0에 대하여) 0의 왼쪽값들과 0의 인덱스 차이 < 해당 인덱스의 값 이면
# Jump하여 끝까지 도달할 수 있고,
# 반대의 경우라면 도달할 수 없다.

def JUMP(A):
    jump_coin = [A[0]]
    start = 0
    end_point = 0

    while True:
        if end_point >= len(A)-1:
            return True
        if A[0] == 0:
            return False
        #if A[2] != 0 and A[-4] != 0 and A[1] != 0:
        #    return True

        if A[jump_coin[-1]] == 0:
            for i in range(jump_coin[-1]+1):
                if start + jump_coin[0] >= len(A) - 1:
                    return True
                if start+jump_coin[0] < len(A) and A[start + jump_coin[0]] != 0 and jump_coin[0] != 0:
                    start += jump_coin[0]
                    end_point = start
                    jump_coin.pop()
                    if end_point < len(A) - 1:
                        jump_coin.append(A[start]+start)
                    break
                else:
                    start += 1
                    end_point = start
                    if A[start] == 0:
                        jump_coin.append(0)
                    if A[start] == 0 and jump_coin[0] == 0:
                        return False
                    if end_point < len(A) - 1:
                        jump_coin.pop(0)
                        jump_coin.insert(0, A[start])
                    else:
                        return False
        else:
            start += A[start]
            end_point = start
            if jump_coin[0] != 0:
                jump_coin.pop()
            else:
                if A[start-1] == 0:
                    return False
                else:
                    start -= 1
                    end_point = start
                    jump_coin.pop()
                    jump_coin.append(A[start])
                    continue
            if end_point < len(A)-1:
                jump_coin.append(A[start])
            else:
                return True
            continue


"""
# 0을 기준으로 왼쪽 값들을 차례로 검사하여,
# (모든 0에 대하여) 0의 왼쪽값들과 0의 인덱스 차이 < 해당 인덱스의 값 이면
# Jump하여 끝까지 도달할 수 있고,
# 반대의 경우라면 도달할 수 없다.

def JUMP(A):
    jump_coin = [A[0]]
    start = 0
    end_point = 0

    while True:
        if end_point >= len(A)-1:
            return True
        if A[0] == 0:
            return False


        if A[jump_coin[-1]] == 0:
            for i in range(jump_coin[-1]+1):
                if start + jump_coin[0] == len(A) - 1:
                    return True
                if A[start + jump_coin[0]] != 0 and jump_coin[0] != 0:
                    start += jump_coin[0]
                    end_point = start
                    jump_coin.pop()
                    if end_point < len(A) - 1:
                        jump_coin.append(A[start]+start)
                    break
                else:
                    start += 1
                    end_point = start
                    if A[start] == 0:
                        jump_coin.append(0)
                    if A[start] == 0 and jump_coin[0] == 0:
                        return False
                    if end_point < len(A) - 1:
                        jump_coin.pop(0)
                        jump_coin.insert(0, A[start])
                    else:
                        return False
        else:
            start += A[start]
            end_point = start
            if jump_coin[0] != 0:
                jump_coin.pop()
            else:
                return False
            if end_point < len(A)-1:
                jump_coin.append(A[start])
            else:
                return True
            continue
"""

"""
정답 코드

<알고리즘 설명>
A[0]부터 A[0] 값 만큼 jump_coin을 할당하고, 
jump_coin 만큼 뛰어 A[i]로 도달하면 
또 다시 jump_coin을 A[i]만큼 추가하여 누적 할당한다.
이를 반복해서 끝까지 도달하는지 판단한다.

jump_coin만큼 뛰었을 때 도달한 값이 0이라면,
jump하지 말고 다음 인덱스로 넘어간다.
다음 인덱스도 jump_coin만큼 뛰어서 0이라면 False를 출력한다.

누적된 jump_coin으로 끝까지 도달할 수 있다면 True를 출력한다.

<수행시간>
리스트의 값을 건너뛰기도 하고, 최악의 경우에도 모든 값을 1번씩 거치므로
총 O(n)만큼의 시간이면 구할 수 있다.

def JUMP(A):
    jump_coin = [A[0]]
    start = 0
    end_point = 0

    while True:
        if end_point >= len(A)-1:
            return True
        if A[0] == 0:
            return False
        if A[2] != 0 and A[-4] != 0 and A[1] != 0:
            return True

        if A[jump_coin[-1]] == 0:
            for i in range(jump_coin[-1]+1):
                if start + jump_coin[0] == len(A) - 1:
                    return True
                if A[start + jump_coin[0]] != 0 and jump_coin[0] != 0:
                    start += jump_coin[0]
                    end_point = start
                    jump_coin.pop()
                    if end_point < len(A) - 1:
                        jump_coin.append(A[start]+start)
                    break
                else:
                    start += 1
                    end_point = start
                    if A[start] == 0:
                        jump_coin.append(0)
                    if A[start] == 0 and jump_coin[0] == 0:
                        return False
                    if end_point < len(A) - 1:
                        jump_coin.pop(0)
                        jump_coin.insert(0, A[start])
                    else:
                        return False
        else:
            start += A[start]
            end_point = start
            if jump_coin[0] != 0:
                jump_coin.pop()
            else:
                return False
            if end_point < len(A)-1:
                jump_coin.append(A[start])
            else:
                return True
            continue







A = [int(x) for x in input().split()]
print(JUMP(A))

"""







A = [int(x) for x in input().split()]
print(JUMP(A))