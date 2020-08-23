def decompose(n):
    goal = 0
    result = [n]
    while result:
        current = result.pop()
        print(current, "  приймаємо в курент і видаляємо з резалт")
        goal += current ** 2
        print(goal, "  квадрат введеного числа")
        for i in range(current - 1, 0, -1):
            print(i, "Число з циклу")
            if goal - (i ** 2) >= 0:
                goal -= i ** 2
                print(goal, "Потрібне число гол -= і ** 2")
                result.append(i)
                if goal == 0:
                    result.sort()
                    print(result, " Остаточний результат")
                    return result
    return None


print(decompose(11))
"""
My little sister came back home from school with the following task: given a squared sheet of paper she has to cut it in pieces which, when assembled, give squares the sides of which form an increasing sequence of numbers. At the beginning it was lot of fun but little by little we were tired of seeing the pile of torn paper. So we decided to write a program that could help us and protects trees.

Task
Given a positive integral number n, return a strictly increasing sequence (list/array/string depending on the language) of numbers, so that the sum of the squares is equal to n².

If there are multiple solutions (and there will be), return as far as possible the result with the largest possible values:

Examples
decompose(11) must return [1,2,4,10]. Note that there are actually two ways to decompose 11², 11² = 121 = 1 + 4 + 16 + 100 = 1² + 2² + 4² + 10² but don't return [2,6,9], since 9 is smaller than 10.

For decompose(50) don't return [1, 1, 4, 9, 49] but [1, 3, 5, 8, 49] since [1, 1, 4, 9, 49] doesn't form a strictly increasing sequence.
"""
