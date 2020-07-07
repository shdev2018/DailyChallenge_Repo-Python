from functools import reduce
class Probs():
    """class containing problem methods"""

    # Given an array of integers, return a new array such that each element at index i of the new 
    # array is the product of all the numbers in the original array except the one at i.
    def prob_07_07_2020(self, array):
        newArray = []
        for x in array:
            # Remove element from list
            temp = [w for w in array if w != x]
            # Get product of new list and append
            newArray.append(reduce(lambda y, z: y * z, temp, 1))
        return newArray
    # Completed in 00:04:22

    # Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
    def prob_06_07_2020(self, lst, k):
        i = 0
        j = 0
        for x in lst:
            for y in lst:
                if i is not j and x + y == k:
                    return True
                j += 1
            i += 1
        return False
    # Completed in 00:04:37



