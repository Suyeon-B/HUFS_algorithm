k = int(input())
n = [int(x) for x in input().split()]
n = sorted(n)
size = len(n)
count = 0
i = 0

while size > i+1:
    if k-n[i] > n[-1]:
        i+=1
        continue
    elif k-n[i] == n[-1]:
        count += 1
        i += 1
        n.pop()
        size -= 1
    else:
        n.pop()
        size -= 1

print(count)