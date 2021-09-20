# n개의 번지수를 입력받아 address 리스트에 저장한다.
address = [int(x) for x in input().split()]
num_of_houses = len(address) # 집의 개수


# 번지수 차이를 계산해 저장한다.
distance_sum = 0
distance_sum_list = []

distances = []

for i in range(num_of_houses):
    line = []
    for j in range(num_of_houses):
        if i<j:
            line.append(abs(address[i] - address[j]))
        elif i>j:
            line.append(distances[j][i])
        else:
            line.append(0)
    distances.append(line)
    distance_sum = sum(distances[i])
    distance_sum_list.append(distance_sum)


print(min(distance_sum_list))
