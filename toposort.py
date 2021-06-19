def topological_sort_stack(adj_list):
    stack = []
    in_degree = [0] * len(adj_list)
    answer = []

    for i in range(len(adj_list)):
        for j in range(len(adj_list)):
            temp = adj_list[j]
            for k in range(len(temp)):
                if temp[k] == i:
                    in_degree[i] += 1


    for i in range(len(in_degree)-1,-1,-1):
        if in_degree[i] == 0:
            stack.append(i)

    while stack:
        node = stack.pop()
        answer.append(node)

        for i in range(len(adj_list[node])):
            idx = adj_list[node][i]
            in_degree[idx] -= 1
            if in_degree[idx] == 0:
                stack.append(idx)

    return answer


n = int(input())
m = int(input())

adj_list={}
for i in range(n):
    adj_list[i]=[]
for i in range(m):
    a, b = [int(x) for x in input().split()]
    adj_list[a].append(b)
result = topological_sort_stack(adj_list)
for i in range(n):
    print(result[i], end=" ")
