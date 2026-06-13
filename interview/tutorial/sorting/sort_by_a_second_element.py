from operator import itemgetter

if __name__ == "__main__":

    data = [('apple', 3), ('banana', 1), ('cherry', 2)]

    data_sorted = sorted(data, key=itemgetter(1))
    print("Sorted 1: ", data_sorted)

    data_sorted2 = sorted(data, key=lambda x:x[1])
    print("Sorted 2: ", data_sorted2)

