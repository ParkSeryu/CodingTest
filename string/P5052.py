class NODE:
    def __init__(self):
        self.value = False
        self.childs = {}


class Trie:
    def __init__(self):
        self.root = NODE()

    def insert(self, phone_num):
        curNode = self.root
        for num in phone_num:
            if num not in curNode.childs:
                curNode.childs[num] = NODE()
            curNode = curNode.childs[num]
            if curNode.value is True:
                return False
        curNode.value = True
        return True


t = int(input())

for _ in range(t):
    n = int(input())
    lst = list()
    for _ in range(n):
        lst.append(input())
    lst.sort()
    rtn = True
    trie = Trie()
    for i in range(len(lst)):
        rtn = trie.insert(lst[i])
        if not rtn:
            break

    if rtn:
        print("YES")
    else:
        print("NO")
