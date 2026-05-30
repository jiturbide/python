def remove_duplicates_fromlist(the_list):
    list2 = []
    
    for e in the_list:
        if e not in list2:
            list2.append(e)
            
    return list2
    
    
if __name__ == "__main__":

    obtained = remove_duplicates_fromlist(["a", "b", "c", "a", "d", "c"])
    expected = ["a", "b", "c", "d"]
    print("Got:", obtained, ", expected:", expected, ", Correct:", obtained == expected)
