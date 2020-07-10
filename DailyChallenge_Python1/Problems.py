from functools import reduce
class Probs():
    """class containing problem methods"""

    # cons(a, b) constructs a pair, and car(pair) and cdr(pair) returns the first and last element of that pair. 
    # For example, car(cons(3, 4)) returns 3, and cdr(cons(3, 4)) returns 4.
    # With the given implementation of cons, implement car and cdr
    def prob_10_07_2020(self, a, b):
        def cons(a, b):
            def pair(f):
                return f(a, b)
            return pair
    
        def car(f):
            def first(a, b):
                return a
            return f(first)

        def cdr(f):
            def last(a, b):
                return b
            return f(last)

        print(car(cons(a, b)))
        print(cdr(cons(a, b)))
    # Completed in 00:05:37

    # Given the root to a binary tree, implement serialize(root), which serializes the tree into a string, 
    # and deserialize(s), which deserializes the string back into the tree.
    def prob_08_07_2020(self):
        node = Node('root', Node('left', Node('left.left')), Node('right'))
        class08_07_2020 = c08_07_2020()
        assert class08_07_2020.deserialize(class08_07_2020.serialize(node)).left.left.val == 'left.left'
        return node
    # Completed in 00:18:46

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

# 08_07_2020
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class c08_07_2020:
    def serialize(self, root):
        self.vals = []
        def encode(node):
            if node:
                self.vals.append(str(node.val))
                encode(node.left)
                encode(node.right)
            else:
                self.vals.append('#')
        encode(root)
        return ' '.join(self.vals)

    def deserialize(self, data):
        
        def decode(vals):
            val = next(vals)
            if val == '#':
                return None
            node = Node(val, decode(vals), decode(vals))
            return node
        vals = iter(data.split())
        return decode(vals)

