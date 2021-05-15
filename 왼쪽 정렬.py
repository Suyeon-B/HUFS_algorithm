W = int(input())
words = input().split()
# code below
len_words = [None] * len(words)
for i in range(len(words)):
	len_words[i] = len(words[i])

# 1) w 내의 값이라면 최대한 붙여 쓴 경우
len_one_line = [0] * len(words)
len_one_line[0] = len(words[0])
penalties = [0] * len(words)

i = 0
j = 0
while(True):
	if i+1 == len(words):
		break
	if ((len_one_line[j] + len_words[i+1] + 1 <= W) and (len_words[i+1]>1)):
		len_one_line[j] += 1 + len_words[i+1]
		i+=1
	else:
		if (len_words[i+1]>1) or (i+2 == len(words)):
			penalties[j] = (W - len_one_line[j])**3
			j += 1
			i += 1
			len_one_line[j] = len_words[i]
			penalties[j] = (W - len_one_line[j])**3
			j+=1
			i+=1
		else:
			penalties[j] = (W - len_one_line[j]) ** 3
			j += 1
			len_one_line[j] += 1 + len_words[i + 1] + len_words[i + 2]
			penalties[j] = (W - len_one_line[j]) ** 3
			i += 2
			j += 1
'''
panalty = 0
for i in range(len(penalties)):
	if penalties[i] == 0:
		break
	panalty += penalties[i]

# 2) 한 줄에 표시할 단어의 조합이 (앞+) (+뒤) 중 패널티 값이 작은 것으로 택할 경우
len_one_line = [0] * len(words)
len_one_line[0] = len(words[0])
penalties = [0] * len(words)

i = 0
j = 0
while(True):
	if i+1 == len(words):
		break
	# (+뒤)의 패널티 값이 작은 경우
	if (j == 0) or (len_one_line[j] + 1 + len_words[i+1] > len_one_line[j+1] + ):
		len_one_line[j] += 1 + len_words[i+1]
	# (앞+)의 패널티 값이 작은 경우

'''

panalty = 0
for i in range(len(penalties)):
	if penalties[i] == 0 and i != 0:
		break
	panalty += penalties[i]

# 결과 : 최소 penalty값
print(panalty)