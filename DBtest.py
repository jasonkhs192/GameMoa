class Myclass:
    def __init__(self):
        self.value1 = 1
        self.value2 = 2

    def get_list(self):
        return [self.value1, self.value2]

x = Myclass().get_list()
for y in x:
    print(y)