class MyList(list):
    bags = []

    def __init__(self, lst):
        self._add(lst)

    def __add(self, data):
        for i in data:
            print("Работает магический метод")

            self.names.append(i)

    def __len__(self):
        print("Работает магический метод")
        return len(self.bags)

    def __str__(self):
        print("Работает магический метод")
        return f'{self.bags}'

lst = MyList(['Jone', 'Snow', 'Java'])
if not lst[2] == 'Python':
    lst[2] == 'Python'

print(lst)
print(len(lst))


