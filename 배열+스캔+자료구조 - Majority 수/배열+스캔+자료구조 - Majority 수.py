"""
딕셔너리를 가지고 O(n)?

딕셔너리 키에는 값을, value에는 들어온 갯수를 세어 넣으면(key값으로 value를 찾아 +1씩) 될 것 같습니다.
A리스트를 끝까지 돌았을 때 가장 큰 value값을 꺼내 전체의 절반보다 큰지를 판단하면 됩니다.
그럼 총 두번 n만큼 돌기 때문에 O(n)이면 됩니다.
"""

A = [int(x) for x in input().split()]
size = len(A)
dictionary = {}
dictionary[A[-1]] = 1 # 마지막 수를 미리 넣어 1개로 저장
A.pop() # O(1)

for i in range(len(A)):
	if A[i] in dictionary.keys(): # 이미 있는 수라면
		dictionary[A[i]] = dictionary[A[i]] + 1 # 그 값의 개수를 하나 늘려 저장
	else: # 없는 수라면
		dictionary[A[i]] = 1 # 1개로 카운트

max_value = max(dictionary.values())
if size/2 < max_value:
	result = [k for k, v in dictionary.items() if v == max_value] # O(n)
	print(result[0])
else:
	print(-1)