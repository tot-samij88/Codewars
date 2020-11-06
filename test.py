# # Калькулятор з Кодварс, все правильно


# def zero(f=None): return 0 if not f else f(0)


# def one(f=None): return 1 if not f else f(1)


# def two(f=None): return 2 if not f else f(2)


# def three(f=None): return 3 if not f else f(3)


# def four(f=None): return 4 if not f else f(4)


# def five(f=None): return 5 if not f else f(5)


# def six(f=None): return 6 if not f else f(6)


# def seven(f=None): return 7 if not f else f(7)


# def eight(f=None): return 8 if not f else f(8)


# def nine(f=None): return 9 if not f else f(9)


# def plus(y): return lambda x: x+y


# def minus(y): return lambda x: x-y


# def times(y): return lambda x: x*y


# def divided_by(y): return lambda x: x/y


# # Це тоже калькулятор звідти
# # НО ТУТ Є  ФІШКА ПЕРЕОБРАЗУВАННЯ + стр в той що буде дійсно додавати


# def zero(arg=""): return eval("0" + arg)


# def one(arg=""): return eval("1" + arg)


# def two(arg=""): return eval("2" + arg)


# def three(arg=""): return eval("3" + arg)


# def four(arg=""): return eval("4" + arg)


# def five(arg=""): return eval("5" + arg)


# def six(arg=""): return eval("6" + arg)


# def seven(arg=""): return eval("7" + arg)


# def eight(arg=""): return eval("8" + arg)


# def nine(arg=""): return eval("9" + arg)


# def plus(n): return "+%s" % n


# def minus(n): return "-%s" % n


# def times(n): return "*%s" % n


# def divided_by(n): return "/%s" % n

# x, y, z = 1, 2, 3
# print(f'{x=} {y=} {z=}')

# import numpy as np
# import matplotlib.pyplot as plt
# x = np.arange(-10, 10.01, 0.01)
# plt.plot(x, x**4)
# plt.show()


# def f():
#    global z
#    print('z is: ', z)
#    z=50
#    print('new value of global z is: ', z)

# f()
# print('Value of z is: ', z)

# x = True
# y = False
# z = False
# if not x or y:
#     print(1)
# elif not x or not y and z:
#     print(2)
# elif (not x or y) or (not y and x):
#     print(3)
# else:
#     print(4)

# name = "snow storm"
# print("%s" % name[0:8:1])

# a = " aaaaa "

# print(a.upper())
word = "abcdefghij"
print(word[:3] + word[3:])