class Node():
    def __init__(self, index, x, y, value):
        self.index = index
        self.x = x
        self.y = y
        self.value = value

    def to_string(self):
        print("Index: " + str(self.index) + ", x: " + str(self.x) + ", y: " + str(self.y) + ", value: " + str(self.value))
