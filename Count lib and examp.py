"""
The main idea is to count all the occurring characters in a string.
 If you have a string like aba, then the result should be {'a': 2, 'b': 1}.

What if the string is empty? Then the result should be empty object literal, {}.

"""


from collections import Counter as count


def count_for_leters(string):
    return {i: string.count(i) for i in string}


count_for_leters('aba')
count_for_leters('')
