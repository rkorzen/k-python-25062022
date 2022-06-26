# przestrzen globalna - przestrzen modulu
a = 1

print(locals())
print(globals())


def foo():

    b = 2  # b jest w przestrzeni lokalnej funkcji foo
    print(a, b)
    print(locals())
    print(globals())


# print(b)
foo()

#
# def foo2():
#     b = 2  # b jest w przestrzeni lokalnej funkcji foo
#     a = 10
#     print(a, b)
#     return a
#
#
# print(a)
#
#
# def foo3():
#     b = 2  # b jest w przestrzeni lokalnej funkcji foo
#     global a
#     a = 10
#     print(a, b)
#
#
# foo3()
# print(a)
#
# # A) 10
# # B) 1
#
# def foo4():
#     b = 2  # b jest w przestrzeni lokalnej funkcji foo
#
#     def bazz():
#         c = 1 # c jest w przestrzeni lokalnej funkcji bazz
#         # nonlocal b  # dla bazz b jest w przestrzeni "nielokalnej" ale tez nie w globalnej
#                   # w przestrzeni domykajacej
#                   # clojure - domkniecie
#         # b = 15
#
#
#         def bar():
#             nonlocal b
#             b = 25
#         bar()
#
#         print(a, b, c)
#     bazz()
#     print(a, b)
#
#
# foo4()
# # print(a)
#
