#  ME
import math


def ss(arr):
    new_arr = []
    arr.sort()
    new_arr.append(arr[0]+arr[1])
    new_arr.append(math.floor((arr[0]+arr[1]+arr[2])/2))
    print(min(new_arr), "days")


ss([1, 23, 2])

# PRO


def solve(xs):
    x, y, z = sorted(xs)
    return min(x + y, (x + y + z) // 2)


"""
You are given three piles of casino chips: white, green and black chips:

the first pile contains only white chips
the second pile contains only green chips
the third pile contains only black chips
Each day you take exactly two chips of different colors and head to the casino. You can chose any color, but you are not allowed to take two chips of the same color in a day.

You will be given an array representing the number of chips of each color and your task is to return the maximum number of days you can pick the chips. Each day you need to take exactly two chips.

solve([1,1,1]) = 1, because after you pick on day one, there will be only one chip left
solve([1,2,1] = 2, you can pick twice; you pick two chips on day one then on day two
solve([4,1,1]) = 2
More examples in the test cases. Good luck!

Brute force is not the way to go here. Look for a simplifying mathematical approach.
"""
