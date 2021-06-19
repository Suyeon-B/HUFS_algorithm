# 허프만 트리 노드
class node:
    def __init__(self, freq, symbol, left=None, right=None):
        # frequency of symbol
        self.freq = freq

        # symbol name (charecter)
        self.symbol = symbol

        # node left of current node
        self.left = left

        # node right of current node
        self.right = right

        # tree direction (0/1)
        self.huff = ''


def printNodes(node, val=''):
    # 현재 노드에 대한 허프만 코드
    newVal = val + str(node.huff)

    # 노드가 에지 노드가 아닌 경우
    # 그 안을 순회한다.
    if (node.left):
        printNodes(node.left, newVal)
    if (node.right):
        printNodes(node.right, newVal)

    # 노드가 에지 노드인 경우
    if (not node.left and not node.right):
        result.append(freq[int(node.symbol)] * len(newVal))


# charecters for huffman tree
chars = []
result = []
# frequency of charecters
freq = list(map(int, input().split()))
for i in range(len(freq)):
    chars.append(i)

# list containing unused nodes
nodes = []

for x in range(len(chars)):
    nodes.append(node(freq[x], chars[x]))

while len(nodes) > 1:
    # 빈도수에 따라 정렬
    nodes = sorted(nodes, key=lambda x: x.freq)

    # 가장 작은 노드 2개를 고른다
    left = nodes[0]
    right = nodes[1]

    # 방향을 잡아준다
    left.huff = 0
    right.huff = 1

    # 작은 두 노드를 합하고
    # 그들의 부모노드로 설정한다
    newNode = node(left.freq + right.freq, left.symbol + right.symbol, left, right)

    # 노드 2개를 제거하고
    # 부모노드를 새로운 노드로 추가
    nodes.remove(left)
    nodes.remove(right)
    nodes.append(newNode)

# 출력
printNodes(nodes[0])
Result = 0
for x in result:
    Result += x

print(Result)