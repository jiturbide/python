def add_two_reversed_numbers(num_lst1:list, num_lst2:list):
    # Edge case
    num1 = 0
    num2 = 0

    for i in range(len(num_lst1)):
        num1 = num1 + num_lst1[len(num_lst1) -i -1] * pow(10,i)

    for i in range(len(num_lst2)):
        num2 = num2 + num_lst2[len(num_lst2) -i -1] * pow(10,i)

    sum = num1 + num2

    lst_result = []
    while sum > 0:
        lst_result.append(sum%10)
        sum = sum // 10

    return lst_result

if __name__ == '__main__':
    print("Start of the program")

    testCases = [
        ([2,4,3], [5,6,4], [7,0,8])
    ]

    for nums1, nums2, expected in testCases:
        result = add_two_reversed_numbers(nums1, nums2)
        if result == expected:
            print("Pass", nums1, nums2, result)
        else:
            print("Fail", nums1, nums2, result, expected)


'''
Challenge 3 — Linked List: Add Two Numbers
Difficulty: Medium | Topic: Linked Lists, Math

Problem Statement
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each node contains a single digit. Add the two numbers and return the sum as a linked list in the same reverse-digit format.
You may assume neither number has leading zeros, except for the number 0 itself.
Input Format

First line: space-separated digits of the first number (in reverse order)
Second line: space-separated digits of the second number (in reverse order)

Constraints

Number of nodes in each list: [1, 100]
0 ≤ Node.val ≤ 9

Sample Input
2 4 3
5 6 4
Sample Output
7 0 8
'''