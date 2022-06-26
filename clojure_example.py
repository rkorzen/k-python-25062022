
def incr_by_factory(by: int):
    def func(a: int):
        return a + by

    return func


incr_by_2 = incr_by_factory(2)

print(incr_by_2(5))

# def func(a):
#     return a + 7
incr_by_7 = incr_by_factory(7)
print(incr_by_7(5))