if __name__ == "__main__":
    str0 = "hola"
    print(str0[0])
    print("hola" + str(1))
    
    
    a = [1,2,3,4,5,6,7,8,9]
    
    for left in range(len(a)):
        for right in range(left+1, len(a)):
            print(a[left], a[right])
    
    s = "hello"
    #del s[2]
    
    print ("s:", s)
    
    num = 1234567
    print(num//10)
    print(num%10)
    
    #1000000 bucket_size [10 - 100000]
    #1000000 = max_buckets * bucket_size
    
    str = "ABC"
    print(chr(ord(str[1])+1))
    print(ord('Z') - ord('A'))
    print(ord('9')-ord('0'))
    print('--------')
    
    arr1 = [1,2,3,4,5]
    effective_rotation = 9 % len(arr1)
    print(effective_rotation, arr1[3:4])
    result = arr1[effective_rotation:len(arr1)] + arr1[0:effective_rotation]
    print(result)

    s1 = 'hola'
    s2 = 'mund'    
    unique = set(s1)
    print(unique)
    for i in range(0, len(s2)):
        if s2[i] in unique :
            print('YES')
    

