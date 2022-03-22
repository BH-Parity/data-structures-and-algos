class array:
    def __init__(self):
        self.array = []

    @property
    def length(self):
        return len(self.array)

    @property
    def plot(self):
        return self.array

    # 增
    def append(self, item):
        self.array.append(item)

    def insert(self, idx, item):
        self.array.insert(idx, item)

    # 删
    def pop(self, idx=-1):
        return self.array.pop(idx)

    # 改
    def modify(self, idx, item):
        self.array[idx] = item

    # 查
    def look(self, idx=0):
        return self.array[idx]


if __name__ == '__main__':
    arr = array()
    arr.append(1)
    arr.append(2)
    arr.append(3)
    print(arr.plot)

    arr.pop(0)
    print(arr.plot)

    arr.modify(0, -1)
    print(arr.plot)

    print(arr.look(0))