# -*- coding: utf-8 -*-
__author__ = 'xy'
'''
 You are given an array with positive numbers and a number N. You should find the N-th power of the element in the array with the index N. If N is outside of the array, then return -1. Don't forget that the first element has the index 0.

Let's look at a few examples:
- array = [1, 2, 3, 4] and N = 2, then the result is 32 == 9;
- array = [1, 2, 3] and N = 3, but N is outside of the array, so the result is -1.

Input: Two arguments. An array as a list of integers and a number as a integer.

Output: The result as an integer.

Example:

index_power([1, 2, 3, 4], 2) == 9

index_power([1, 3, 10, 100], 3) == 1000000

index_power([0, 1], 0) == 1

index_power([1, 2], 3) == -1


'''
#
# def index_power(array, n):
#     if n >= len(array):
#         return -1
#     else:
#         return array[n] ** n
#
# print index_power([1,2,3], 2)

# c1

#try-except
def index_power(array, n):

    try:
        return array[n] ** n

    except IndexError:
        return -1
