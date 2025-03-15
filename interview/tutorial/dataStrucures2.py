from collections import deque

# Data structures

def fun(arr):
    return arr

if __name__ == '__main__':
    # Sets
    basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
    print("basket:", basket)
    print('apple in basket', "apple" in basket)

    a = set('abracadabra') # add each letter as element, doesn't allow duplicates
    b = set('alacazam')
    print(a,b)
    basket.add('strawberry')

    # Dictionaries
    tel = {'jack': 4098, 'sape': 4139, 'luis': 9861, 'miriam': 1234}
    tel['guido'] = 1234
    tel['guido'] = 1235
    print('tel: ', tel)
    print("list(tel):", list(tel))
    print("sorted(tel):", sorted(tel))

    print("'jluis' in tel:",'jluis' in tel)

    anotherDirectory = dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])
    print("anotherDirectory:", anotherDirectory)
    tel2 = dict(jan=1, feb=2, mar=3)
    print('tel2:', tel2)
    tel3 = {x: x + '.' for x in tel}
    print('tel3:', tel3)


    # Looping techniques
    for k,v in tel.items():
        print(k, v)

    names = list(tel)
    for i, k in enumerate(names):
        print("enumerate", i, k)

    questions = ['name', 'quest', 'favorite color']
    answers = ['lancelot', 'the holy grail', 'blue']

    for k, v in zip(questions, answers):
        print(k, v)

    for i in reversed(range(1,10,1)):
        print("element: ", i)

    basket = ["banana", "grapes", "watermelon", "pear", "kiwi", "banana"]
    print(sorted(basket))
    print(set(basket))
    print(sorted(set(basket)))

    array = [1,2,3,4,5]
    i = 3
    del array[:i]
    print(array)

    x = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
    sorted_x = sorted(x.items(), key=lambda kv: kv[1])
    print('sorted:', sorted_x)

