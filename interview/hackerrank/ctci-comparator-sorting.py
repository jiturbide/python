from functools import cmp_to_key

class Player:
    def __init__(self, name, score):
        self.name = name
        self.score = score
        
#    def __repr__(self):
#        return 0

    def comparator(a, b):
        if a.score < b.score:
            return 1
        else:
            if a.score == b.score:
                if a.name > b.name:
                    return 1
            return -1

if __name__ == "__main__":
    data = []
    data.append(Player("amy", 100))
    data.append(Player("david", 100))
    data.append(Player("heraldo", 50))
    data.append(Player("aakansha", 75))
    data.append(Player("aleksa", 150))
        
    data = sorted(data, key=cmp_to_key(Player.comparator))
    for i in data:
        print(i.score, i.name)
        
    print(1/2)
    print(1/2.0)
    print(1//2)
    array = [1,2,3]
    print(array[1:2])
    