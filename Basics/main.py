import helper


def lesson_001() -> None:
    # Strings are immutable
    immutable: str = "you can't change me!"
    immutable.replace("can't", "can")
    immutable + "!!"  # NOQA
    print(immutable)


def lesson__002() -> None:
    from helper import lesson_002_helper
    # If not immutable, variables are call by reference
    mutable_list = ["I am mutable & I go by reference."]
    mutable_dict = {"mutable": True}
    lesson_002_helper(_list=mutable_list, _dict=mutable_dict)
    print(f"{mutable_list=}", f"{mutable_dict=}")


def lesson_003() -> None:
    _txt = "AaShish gahlAwat"
    print("1. Text: %s" % _txt)
    print(f"2. Text: {_txt}")
    print("3. {0} {1}".format("Text:", _txt))
    print("4. Text: {_var}".format(_var=_txt))
    print("5. Text: ", f"{_txt} " * 2)
    print(r"C:\user")
    print(fr"C:\user\{_txt}")
    print(f"{_txt:#<20}")
    print(f"{_txt: >20}")
    print(f"{_txt:$^20}")
    print(f"{12345.98765:.9f}")
    print(_txt.upper())
    print(_txt.title())
    print(_txt.lower())


def lesson_004() -> None:
    _ = 500
    a = 1000
    b = 500 + _
    print("==: ", a == b)
    print("is: ", a is b)


def lesson_005() -> None:
    a = 0.3
    b = 0.1 + 0.2
    print(f"{a=}")
    print(f"{b=}")
    print(a == b)


def lesson_006() -> None:
    import math
    _combinations = 3
    _list = [
        "first",
        "second",
        "third",
        "fourth",
        "fifth",
        "sixty",
        "seventh",
        "eighth",
        "ninth",
        "tenth"
    ]
    print(math.comb(len(_list), _combinations))


def lesson_007() -> None:
    a = False
    b = False
    c = True
    d = False
    e = False

    _args = [a, b, c, d, e]

    print("Least one is True") if any(_args) else print("All are False")
    print("All are True") if all(_args) else print("All are not True")


def lesson_008() -> None:
    _str = "radar"
    print("Palindrome: ", _str == _str[::-1])


def lesson_009() -> None:
    _txt = "Split me down!"
    print(_txt := _txt.split(" "))
    print(*_txt)
    print([*_txt])


def lesson_010() -> None:
    from helper import (
        lesson_010_generator,
        lesson_010_generator_return,
        lesson_010_for_loop
    )
    import timeit
    _gen = lesson_010_generator()
    _list: list[int, int, int] = [next(_gen), next(_gen), next(_gen)]
    print(_list)

    for_time = timeit.timeit(stmt=lesson_010_for_loop, number=10_000)
    generator_time = timeit.timeit(stmt=lesson_010_generator_return, number=10_000)
    print(f"{for_time=}")
    print(f"{generator_time=}")
    print(round((for_time / generator_time) * 100, 2), "% faster")


def lesson_011() -> None:
    _txt: str = "Text"
    for _attr in dir(_txt):
        print(_attr)


def lesson_012() -> None:
    a, b = 1, 2
    print(f"{a=} {b=}")
    b, a = a, b
    print(f"{a=} {b=}")


def lesson_013() -> None:
    from getpass import getpass
    import secrets
    print(input("Enter username: "))
    print(f"Suggested password: {secrets.token_hex(12)}")
    print(getpass("Enter password: "))


def lesson_014() -> None:
    _tuple = (1, 2)
    print(f"{_tuple=}")
    _tuple += (3, 4)
    print(f"{_tuple=}")
    try:
        _tuple[0] = 0  # NOQA
    except TypeError:
        print("Tuples are immutable")


def lesson_015() -> None:
    _var1 = (1)  # NOQA
    print(f"{_var1=}", type(_var1))
    _var2 = (1,)
    print(f"{_var2=}", type(_var2))
    _var3 = 1, 2
    print(f"{_var3=}", type(_var3))
    _var4 = [1, 2]
    print(f"{_var4=}", type(_var4))


def lesson_016() -> None:
    # Iteration on tuple is slightly faster
    from timeit import timeit
    # Avoid dot operator as it need to locate function inside module
    # timeit.timeit

    def loop__on_list():
        for i in [1, 2, 3, 4, 5]:
            pass

    def loop_on_tuple():
        for i in (1, 2, 3, 4, 5):
            pass

    list_time = timeit(stmt=loop__on_list, number=10_000_000)
    tuple_time = timeit(stmt=loop_on_tuple, number=10_000_000)
    print(f"{list_time=}")
    print(f"{tuple_time=}")
    print(round((list_time / tuple_time) * 100, 2), "% faster")


def lesson_017() -> None:
    def first(_name):
        print(f"{_name} function called!")

    def second(_name):
        print(f"{_name} function called!")

    _first = "FIRST"
    _second = "SECOND"
    _fn_mapping = {
        _first: first,
        _second: second
    }
    _fn_mapping[_first](_first)


def lesson_018() -> None:
    _name = "Aashish Gahlawat"

    def only_kwargs(*, _name):
        print(_name)

    def only_positional(_name, /):
        print(_name)

    def positional_and_kwargs(_name):
        print(_name)

    positional_and_kwargs("Called WITHOUT keyword arguments")
    positional_and_kwargs(_name="Called WITH keyword arguments")

    try:
        only_kwargs(_name)  # NOQA
    except TypeError:
        print("Can't call WITHOUT Keyword arguments")
    try:
        only_positional(_name=_name)  # NOQA
    except TypeError:
        print("Can't call WITH keyword arguments")


def lesson_019() -> None:
    help(float)


def lesson_020() -> None:
    import logging
    _red = "\033[91m"
    print(_red + "RED")
    _yellow = "\033[93m"
    print(_yellow + "YELLOW")

    logging.info("Information Log")
    logging.error("Error Log")
    logging.debug("Debug log")
    logging.warning("Warning log")
    logging.critical("Critical log")

    logging.log(level=0, msg="Log of level 1")


def lesson_021() -> None:
    from bisect import bisect
    _sorted_list = [1, 2, 3, 5]
    _four = 4

    _idx = bisect(_sorted_list, _four)

    print(f"{_sorted_list=}")
    print(f"{_idx=}")
    _sorted_list.insert(_idx, _four)
    print(f"{_sorted_list=}")


def lesson_022() -> None:
    for i in range(5):
        pass
    else:
        print("All iterations of first for loop executed")

    for i in range(5):
        if i == 2:
            break
    else:
        print("All iterations of second for loop executed")


def lesson_023() -> None:
    # Avoid using from package_name import *
    import numpy as np

    a = np.array([[1, 2], [3, 4]])
    b = np.array([[5, 6], [7, 8]])

    print("Matrix multiplication: ")
    print(a @ b)


def lesson_024() -> None:
    _names = ["Aashish", "Gahlawat"]
    _names_dict = {name: len(name) for name in _names}
    print("Names Length: ", _names_dict)


def lesson_025() -> None:
    # Common BUG
    _list = [
        "first",
        "second",
        "third",
        "fourth",
        "fifth",
        "sixty",
        "seventh",
        "eighth"
        "ninth",
        "tenth",
    ]
    print("Should be 10 but is: ", len(_list))
    print("BUG element: ", _list[7])


def lesson_026():
    # Avoid Global Variables

    _data = helper.lesson_026_data()
    print(f"{_data}")

    # Monkey Patching
    helper.lesson_026_data = helper.lesson_026_monkey_patched_data

    _data = helper.lesson_026_data()
    print(f"{_data}")


def lesson_027() -> None:
    import numpy as np
    _list1 = [1, 2, 3]
    _list2 = [[1], [2], [3]]
    _list3 = [[[1]], [[2]], [[3]]]
    print(np.array(_list1).flatten())
    print(np.array(_list2).flatten())
    print(np.array(_list2).flatten())


def lesson_028() -> None:
    from package1 import lesson_028_helper
    print(lesson_028.__qualname__)
    lesson_028_helper()


def lesson_029() -> None:
    # Pickle
    return


def lesson_030() -> None:
    # Data Class
    return


def lesson_031() -> None:
    # Context Manager
    return


def lesson_032() -> None:
    _list1 = [1, 2, 3, 3]
    _list2 = [1, 2, 3, 2, 2]
    _set1 = set(_list1)
    _set2 = set(_list2)
    print(f"{_set1}")
    print(f"{_set2}")
    print(_set1 == _set2)


def lesson_033() -> None:
    _list: list[str, ...] = ["first", "second", "third"]

    _new_list: list[str, ...] = []
    for _txt in _list:
        _new_list.append(_txt.upper())

    print(_new_list)
    # Faster than for loop
    print([_txt.upper() for _txt in _list])
    # Faster than list comprehension
    print(list(map(str.upper, _list)))


def lesson_034() -> None:
    # Regex
    return


def lesson_035() -> None:
    # Lists XOR
    return


def lesson_036() -> None:
    # Decorators
    return


def lesson_037() -> None:
    from sys import getsizeof
    print(getsizeof(range(1000)))
    print(getsizeof(list(range(1000))))


def lesson_038() -> None:
    import os
    print(os.getcwd())


def lesson_039() -> None:
    # @formatter:off
    a = 1; b = 2
    print(f"{a=}", f"{b=}")
    print(_txt := "Aashish"); print(_txt := "Gahlawat")  # NOQA
    # @formatter:on


def lesson_040() -> None:
    _none = "I am not None instance!"

    if _none is not None:
        print("Right Way to check for None")

    if None is not _none:
        print("Alternative way to check for None")

    if not _none is None:  # NOQA
        print("Alternate way to check for None")


def lesson_041() -> None:
    _list = [1, 2, 3]
    print(_list * 3)


def lesson_042() -> None:
    print(1_00)  # Numeric
    print(0b_0101)  # Binary
    print(0x_52_fa)  # Hex
    print(1_00 * 1_00_00)


def lesson_043() -> None:
    _name, _, _age = ("Ashish", "Throw Away", 28)
    print(f"{_name=}", f"{_age=}")
    _first, *_, _last = [1, 2, 3, 4, 5]
    print(f"{_first=}", f"{_last=}")


def lesson_044() -> None:
    item = ["SWORD", "SHIELD", "PEN", "NEEDLE"]
    rarity = [4, 3, 2, 1]
    weight = [400, 300, 20, 1]
    _inventory = zip(item, rarity, weight)
    i, r, w = zip(*_inventory)
    print(list(_inventory))  # Empty
    print("Items: {0}\nRarity{1}\nWeight: {2}".format(i, r, w))


def lesson_045() -> None:
    _val = 0.7 + 0.6
    # float calculations are not precise
    print(True) if _val >= 1.3 else print(False)


def lesson_046() -> None:
    def is_divisible_by_2(_num):
        # similar to apply in pandas
        return True if _num % 2 == 0 else False

    _list = [1, 2, 3, 4, 5, 6]
    print(list(filter(is_divisible_by_2, _list)))


def lesson_047() -> None:
    def _add(*numbers):
        return sum(numbers)

    print(_add(1, 2, 3, 4, 5))


def lesson_048() -> None:
    x = int("1234567"[6])  # 7
    y = -round(2.1)  # -2
    print(x // y)  # Quotient


def lesson_049() -> None:
    pass
    # shutil.rmtree("folder_path_to_delete")


def lesson_050() -> None:
    print(round(123, -2))
    print(str(round(123, -2))[-3])


def lesson_051() -> None:
    print("Make cursor move randomly infinitely")
    # import pyautogui as pag
    # import random
    # import time
    # while True:
    #     x = random.randint(600, 700)
    #     y = random.randint(200, 600)
    #     pag.moveTo(x, y, 0.5)
    #     time.sleep(2)


def lesson_052() -> None:
    _banana = "BANANA"
    _orange = "ORANGE"
    _apple = "APPLE"
    _mango = "MANGO"

    _list = [_banana, _orange, _apple, _mango]
    _rarity = {
        _orange: 1,
        _banana: 2,
        _mango: 3,
        _apple: 4,
    }

    print(sorted(_list, key=_rarity.__getitem__, reverse=True))
    print("Banana Rarity: ", _rarity.__getitem__(_banana))


def lesson_053() -> None:
    eval("print('WARNING: Never use `eval` unless you really have to')")


def lesson_054() -> None:
    _list1 = [1, 2]
    _list2 = [3, 4]

    print(_list1)
    _list1.extend(_list2)
    print(_list1)
    print(_list1 + _list2)


def lesson_055() -> None:
    def _divide(_denominator):
        try:
            1 / _denominator
        except ZeroDivisionError:
            print("Can not divide by Zero")
        else:
            print("Divided without any exception")
        finally:
            print("Exception Exited")

    print("Dividing by 1")
    _divide(1)
    print("Dividing by 0")
    _divide(0)


def lesson_056() -> None:
    from time import time
    _range = 1_00_000_000

    _list1 = []
    _start = time()
    for i in range(_range):
        # Each time an element is added, memory is allocated
        _list1.append(i)
    print(_start - time())

    _list2 = [0] * _range
    _start = time()
    for i in range(_range):
        _list2[i] = i
    print(_start - time())


def lesson_057() -> None:
    x = 3
    y = (x - 1) ^ 2  # XOR
    print(y)


def lesson_058() -> None:
    _name = "aashish"

    if _name == "first" or "second":
        print(True)


def lesson_059() -> None:
    _list = ["first", "second"]

    for idx, _txt in enumerate(_list):
        print(f"{idx}: {_txt}")


def lesson_060() -> None:
    from enum import Enum
    # enums
    class Status(Enum):
        FIRST = "one"
        SECOND = "two"

    print(Status.FIRST.name)
    print(Status.FIRST.value)


def lesson_061() -> None:
    class CallableClass:
        def __call__(self, *args, **kwargs):
            print("Class called")

    _callable_class_var = CallableClass()

    class NonCallableClass:
        pass

    _non_callable_class_var = NonCallableClass()

    def callable_function():
        print("Function called")

    _variable: str = "Non callable variable"

    print(callable(callable_function))
    print(callable(_callable_class_var))

    print(callable(_variable))
    print(callable(_non_callable_class_var))


def lesson_062() -> None:
    _txt = "Aashish Gahlawat"
    print(isinstance(_txt, str))
    print(isinstance(_txt, (int, str)))
    print(isinstance(_txt, (int, float)))


def lesson_063() -> None:
    _dict = {"key": "value"}
    print(_dict.get("key", None))
    print(_dict.get("invalid_key", None))


def lesson_064() -> None:
    class Person:

        def __init__(self, _name):  # Constructor
            print("Initializing object")
            self.name = _name

    p1 = Person("Aashish Gahlawat")
    print(getattr(p1, "name", None))
    print(getattr(p1, "age", None))


def lesson_065() -> None:
    class Person:

        def __new__(cls, *args, **kwargs):
            print("Creating object")
            return super().__new__(cls, *args, *kwargs)

    Person()


def lesson_066() -> None:
    # property (setter & getter)
    class Person:
        def __init__(self, _a):
            self._age = _a

        @property  # Getter
        def age(self):
            return self._age

        @age.setter
        def age(self, _a):
            self._age = _a

    p1 = Person(28)
    print(p1.age)
    p1.age = 29
    print(p1.age)


def lesson_067() -> None:
    # super
    return


def lesson_068() -> None:
    # pass vs continue
    for num in range(0, 2):
        pass  # null operator (when statement is required)
        print("This statement is after 'pass'")
        continue
        print("This statement is after 'continue'")  # NOQA

    for num in range(50, 100, 10):
        pass  # null operator (when statement is required)
    return


def lesson_069() -> None:
    # super(Class, self).function(*args, **kwargs)
    # super().function(*args, **kwargs)
    class Person1:

        def __new__(cls, *args, **kwargs):
            print("Creating object")
            return super().__new__(cls, *args, *kwargs)

    class Person2:

        def __new__(cls, *args, **kwargs):
            print("Creating object")
            return super(Person2, cls).__new__(cls, *args, *kwargs)

    Person1()
    Person2()
    return


def lesson_070() -> None:
    # Multiple inheritance MRO:
    return


def lesson_071() -> None:
    def return_fn():
        return

    def return_none_fn():
        return None

    print(return_fn())
    print(return_none_fn())


def lesson_072() -> None:
    # Name Mangling
    return


def lesson_073() -> None:
    _var1 = "Aashish Gahlawat"
    _var2: str = "Aashish Gahlawat"

    def _test_fn1(_list: str):
        for _ in _list:
            ...

    def _test_fn2() -> str:
        return 1  # NOQA

    _test_fn1([1, 2, 3])  # NOQA
    print(_test_fn2())
    print(_var1 is _var2, _var1 == _var2)


def lesson_074() -> None:
    class Parent:
        ...

    class Child(Parent):
        ...

    print(isinstance(Child(), Child))
    print(type(Child()) == Child)

    print(isinstance(Child(), Parent))
    print(type(Child()) == Parent)


def lesson_075() -> None:
    _list = [1, 2, 3, 4, 5, 6]

    print(_list[::2])
    print(_list[::-1])
    print(_list[::-2])


def lesson_076() -> None:
    _people = [("Aashish", 5000), ("Gahlawat", 1000)]

    def tax_fn(_person: tuple):
        _tax_rate = 0.05
        _name = _person[0]
        _salary = _person[1] - (_person[1] * _tax_rate)
        return _name, _salary  # (_name, _age) tuple

    _post_tax = list(map(tax_fn, _people))
    print(_post_tax)


def lesson_077() -> None:
    _var1 = 1
    _var2 = 2

    if 1 == _var1 < 2:  # (1 == _var1) and (_var1 < 2)
        print(True)


def lesson_078() -> None:
    from copy import copy, deepcopy
    _list1 = [1, [2], 4]
    _list2 = copy(_list1)
    _list3 = deepcopy(_list1)

    _list1.append(5)
    _list1[1].append(3)

    print()
    print(_list1)
    print(_list2)
    print(_list3)


def lesson_079() -> None:
    from copy import copy
    _var1 = 1
    _var2 = 1
    _var3 = copy(_var1)
    _var4 = 3

    print(_var1 is _var2, _var2 is _var3)
    print(_var1 == _var2, _var2 == _var3)

    print()
    print(id(_var1))
    print(id(_var2))
    print(id(_var3))
    print()
    print(id(_var4))


def lesson080() -> None:
    _var1 = True
    _var2 = True
    _var3 = True

    def without_guard_clause():
        if _var1:
            if _var2:
                if _var3:
                    print("Victory")
                else:
                    print("_var3 is False")
            else:
                print("_var2 is False")
        else:
            print("_var1 is False")

    def with_guard_clause():
        if not _var1:
            print("_var1 is False")
            return
        if not _var2:
            print("_var3 is False")
            return
        if not _var3:
            print("_var3 is False")
            return
        print("Victory")


def lesson_081() -> None:
    _list1 = [1, 2, 3, 4]
    _list2 = [1, 2, 3, 4]

    print(id(_list1), id(_list2))  # Mutable
    print(_list1 is not _list2)
    print(_list1 != _list2)
    ...


def lesson_082() -> None:
    from math import ceil
    print(7 / 3)
    print(7 // 3)
    print(ceil(7 / 3))


def lesson_083() -> None:
    _list1 = [1, 3, 2, 9, 4]
    _list2 = [1, 3, 2, 9, 7, 3]
    print(sorted(_list1))
    print(_list2.sort())  # Inplace
    print(_list2)

def lesson_084() -> None:
    print(list(range(0, 5)))


def lesson_085() -> None:
    # async
    ...

def lesson_086() -> None:
    # PyTest strategy-fixture
    ...


def lesson_087() -> None:
    # TDD & BDD
    ...

def lesson_088() -> None:
    # __slots__
    ...

def lesson_089() -> None:
    # TODO: Upgrade python

    number = 51

    match number:
        case 10: print("number is 10")
        case _: print("Number not found")

    match number:
        case _ if number < 50:
            print('Number is less than 50')
        case _ if number == 50:
            print('Number is 50')
        case _: print("Number not found")

    match [number < 50, number == 50]:
        case [True, False]:
            print("Number less than 50")
        case [_, True]:
            print('Number is 50')
        case [False, False]:
            print("Number is greater than 50")

# ----------------------------------------------------------------------------------------------------------------------


if __name__ == "__main__":
    _lesson_number = "089"
    eval(f"lesson_{_lesson_number}()")
    print("\nLessons by Aashish Gahlawat")
