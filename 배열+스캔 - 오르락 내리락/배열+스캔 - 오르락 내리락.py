def solve(A):
    B = []
    # 홀수번째에 min값을 차례로 넣는다.
    for i in range(len(A)):
        if i%2 == 0:
            B.append(min(A))
            A.remove(min(A))
        else:
            B.append(max(A))
            A.remove(max(A))
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