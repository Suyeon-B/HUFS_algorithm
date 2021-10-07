class HashOpenAddr:
    def __init__(self, size=10):
        self.size = size
        self.keys = [None] * self.size
        self.values = [None] * self.size

    def __str__(self):
        s = ""
        for k in self:
            if k == None:
                t = "{0:5s}|".format("")
            else:
                t = "{0:-5d}|".format(k)
            s = s + t
        return s

    def __iter__(self):
        for i in range(self.size):
            yield self.keys[i]

    def find_slot(self, key):
        i = self.hash_function(key)
        start = i
        while (self.keys[i] != None) and (self.keys[i] != key):
            i = (i + 1) % self.size
            if (i == start): return None
        return i

    def set(self, key, value=None):
        i = self.find_slot(key)
        if i == None:
            return None
        if (self.keys[i] != None):  # 이미 key 값을 갖는 item이 H에 존재함 (수정)
            self.values[i] = value  # value 값 update 후 리턴

        # H[i]가 비어있는 경우, 즉 key 값을 갖는 item이 없다면 새로 저장함 (삽입)
        else:
            self.keys[i] = key
            self.values[i] = value
        return key

    def hash_function(self, key):
        return key % self.size

    def remove(self, key):
        i = self.find_slot(key)
        if self.keys[i] == None:  # 삭제할 아이템이 실제로 존재하지 않는 경우
            return None
        j = i
        while True:
            self.keys[i] = None
            while True:
                j = (j + 1) % self.size
                if self.keys[j] == None:  # 자리 이동 완료!
                    return key
                k = self.hash_function(self.keys[j])
                # |    i..k..j |
                # |....j..i..k..| or |..k..j..i..|
                if not (i < k <= j or j < i < k or k <= j < i):  # H[j] --> H[i]
                    break
            self.keys[i] = self.keys[j]
            i = j

    def search(self, key):
        i = self.find_slot(key)
        try:
            if self.keys[i] != None:  # key is in table
                return self.keys[i]
        except:
            return None  # not found

    def __getitem__(self, key):
        return self.search(key)

    def __setitem__(self, key, value):
        self.set(key, value)


H = HashOpenAddr()
k = int(input())
n = [int(x) for x in input().split()]
size = len(n)
count = 0
zero_count = 0

t = list(n)
for i in range(size):
    H.set(n[i], k-n[i])
    if k == 0 and n[i] == 0:
        zero_count+=1
for i in range(size):
    if H.search(k-n[i]):
        count += 1

zero_count = zero_count//2
count += zero_count

print(count//2)