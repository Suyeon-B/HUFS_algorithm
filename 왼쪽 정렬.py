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
space = 0
i = 0
j = 0
while(True):
	if i+1 == len(words):
		break
	if (len_one_line[j] + len_words[i+1] + 1 <= W):
		len_one_line[j] += 1 + len_words[i+1]
		i+=1
	else:
		penalties[j] = (W - len_one_line[j])**3
		j+=1
		i+=1
		len_one_line[j] = len_words[i]
		penalties[j] = (W - len_one_line[j])**3

panalty = 0
for i in range(len(penalties)):
	panalty += penalties[i]
# 2)

# 결과 : 최소 penalty값
print(panalty)