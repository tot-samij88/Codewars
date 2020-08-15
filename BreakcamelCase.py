"""
Complete the solution so that the function will break up camel casing, using a space between words.

Example
solution("camelCasing")  ==  "camel Casing"

"""

import re


def solution(s):
    return re.sub(r'(?<!^)(?=[A-Z])', ' ', s)


def solution1(s):
    return ''.join(' ' + c if c.isupper() else c for c in s)

import re
def solution2(s):
    return re.sub('([A-Z])', r' \1', s)