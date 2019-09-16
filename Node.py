class Node():
    def __init__(self):
        self.index = None
        self.x = None
        self.y = None
        self.value = None

    def to_string(self):
        print("Index: " + str(self.index) + ", x: " + str(self.x) + ", y: " + str(self.y) + ", value: " + str(self.value))
