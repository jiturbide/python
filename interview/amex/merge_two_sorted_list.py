def mergeSortedLists(lst1, lst2):
    lstmerged = []
    len_lst1 = len(lst1)
    len_lst2 = len(lst2)

    while len(lstmerged) < (len_lst1+len_lst2):
        if len(lst1) > 0 and len(lst2) > 0:
            if lst1[0] <= lst2[0]:
                lstmerged.append(lst1[0])
                del lst1[0]
            else:
                lstmerged.append(lst2[0])
                del lst2[0]
        elif len(lst2) == 0:
            lstmerged.append(lst1[0])
            del lst1[0]
        else:
            lstmerged.append(lst1[0])
            del lst1[0]
    
    return lstmerged

if __name__ == "__main__":
    
    obtained = mergeSortedLists([1, 4, 6], [2, 3, 5])
    expected = [1, 2, 3, 4, 5, 6]
    print("Got:", obtained, ", expected:", expected, ", Correct:", obtained == expected)

