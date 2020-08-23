"""
ROT13 is a simple letter substitution cipher that replaces a letter with the letter 13 letters after it in the alphabet. ROT13 is an example of the Caesar cipher.

Create a function that takes a string and returns the string ciphered with Rot13. If there are numbers or special characters included in the string, they should be returned as they are. Only letters from the latin/english alphabet should be shifted, like in the original Rot13 "implementation".

Please note that using encode is considered cheating.
"""


def rot13(message):
    abc = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    out = ""
    for i in message:
        if i in abc.lower():
            out += abc[(abc.lower().index(i)+13) % 26].lower()
        elif i in abc:
            out += abc[(abc.index(i)+13) % 26]
        else:
            out += i
    print(out)


rot13("Test")
