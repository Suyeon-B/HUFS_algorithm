# n개의 번지수를 입력받아 address 리스트에 저장한다.
address = [int(x) for x in input().split()]
num_of_houses = len(address) # 집의 개수


# 번지수 차이를 계산해 저장한다.
distance = 0
distances = []
address.sort() # 리스트를 정렬해서 가운데 값을 찾는다.
if num_of_houses%2 != 0: # 집이 홀수개 있다면
    for i in range(num_of_houses):
        distance += abs(address[num_of_houses//2] - address[i]) # 정 가운데 값이 거리의 합이 최소가 되는 집이다.
    print(distance)
else: # 짝수개 있다면 가운데 두 집들 중 하나가 거리의 합이 최소가 되는 집이다.
    for i in range(num_of_houses):
        distance += abs(address[num_of_houses//2] - address[i]) # 가운데의 왼쪽 집
    distances.append(distance)

    for i in range(num_of_houses):
        distance += abs(address[num_of_houses//2+1] - address[i]) # 가운데의 오른쪽 집
    distances.append(distance)

    print(min(distances))
