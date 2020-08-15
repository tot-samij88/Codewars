"""
In this kata we want to convert a string into an integer. The strings simply represent the numbers in words.

Examples:

"one" => 1
"twenty" => 20
"two hundred forty-six" => 246
"seven hundred eighty-three thousand nine hundred and nineteen" => 783919
Additional Notes:

The minimum number is "zero" (inclusively)
The maximum number, which must be supported is 1 million (inclusively)
The "and" in e.g. "one hundred and twenty-four" is optional, in some cases it's present and in others it's not
All tested numbers are valid, you don't need to validate them

"""


def parse_int(string):
    dict = {'one': 1,
            'two': 2,
            'three': 3,
            'four': 4,
            'five': 5,
            'six': 6,
            'seven': 7,
            'eight': 8,
            'nine': 9,
            'ten': 10,
            'eleven': 11,
            'twelve': 12,
            'thirteen': 13,
            'fourteen': 14,
            'fifteen': 15,
            'sixteen': 16,
            'seventeen': 17,
            'eighteen': 18,
            'nineteen': 19,
            'twenty': 20,
            'thirty': 30,
            'forty': 40,
            'fifty': 50,
            'sixty': 60,
            'seventy': 70,
            'eighty': 80,
            'ninety': 90,
            'hundred': 100,
            'million': 1000000}
    result = 0
    temp = []

    for s in string.split('thousand'):
        sum = 0
        for i in s.strip().split():
            if i.find('-') != -1:
                for j in i.split('-'):
                    if j in dict:
                        sum += dict.get(j)
            else:
                if i in dict:
                    if i == 'hundred':
                        sum *= dict.get(i)
                    elif i == 'million':
                        sum *= dict.get(i)
                    else:
                        sum += dict.get(i)
        temp.append(sum)

    if len(temp) > 1:
        result = temp[0] * 1000 + temp[1]
    elif len(temp) == 1:
        result = temp[0]

    return result


#        BEST EXAMPLE
words = {w: n for n, w in enumerate(
    'zero one two three four five six seven eight nine ten eleven twelve thirteen fourteen fifteen sixteen seventeen eighteen nineteen'.split())}
words.update({w: 10 * n for n, w in enumerate(
    'twenty thirty forty fifty sixty seventy eighty ninety hundred'.split(), 2)})
thousands = {w: 1000 ** n for n, w in enumerate(
    'thousand million billion trillion quadrillion quintillion sextillion septillion octillion nonillion decillion'.split(), 1)}


def parse_int(strng):
    num = group = 0
    for w in strng.replace(' and ', ' ').replace('-', ' ').split():
        if w == 'hundred':
            group *= words[w]
        elif w in words:
            group += words[w]
        else:
            num += group * thousands[w]
            group = 0
    return num + group
