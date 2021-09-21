def solve(A):
    B = list(A)
    BigOrSmall = []
    for i in range(1, len(B)):
        if B[i] > B[i - 1]:
            BigOrSmall.append(0) # 작으면 0
        elif B[i] < B[i - 1]:
            BigOrSmall.append(1) # 크면 1

        if len(BigOrSmall) > 1:
            if BigOrSmall[0] == BigOrSmall[1]:
                temp = B[i]
                B[i] = B[i - 1]
                B[i - 1] = temp
                BigOrSmall = []
            else:
                continue
    return B
        #else:
            # B = 1, S = 0일 때
            # B = 0, S = 1일 때
            # 즉, abs(B-S) == 1일 때
            #if B != S:




            # B = 1, S = 1일 때
            # B = 0, S = 0일 때
            # 즉, abs(B-S) == 0일 때

    



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