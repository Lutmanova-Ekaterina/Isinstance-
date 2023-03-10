class TeamIterator:
    def __init__(self, team):
        self.team = team
        self.members = list(self.team._juniorMembers + self.team._seniorMembers)
        self.i = 0

    def __nex__(self):
        if self.i < len(self.members):
            current = self.members[self.i]
            self.i += 1
            return current
        else:
            raise StopIteration

class Team:
    def __init__(self):
        self._juniorMembers = list()
        self._seniorMembers = list()

    def add_junior_members(self, members):
        self._juniorMembers += members

    def add_senior_members(self, members):
        self._seniorMembers += members

    def __iter__(self):
        return TeamIterator(self)

def main():
team = Team()
team.add_junior_members(['Ivan', 'Mary', 'Nikita'])
team.add_senior_members(['Rita', 'Roma', 'Ramil'])
print('*** Итерируемся по команде в цикле for ***')
for member in team:
    print(member)
print('*** Итерируемся по команде в цикле while ***')
iterator = iter(team)
while True:
    try:
        elem = next(iterator)
        print(elem)
    except StopIteration:
        break

if __name__ == '__main__':
    main()
