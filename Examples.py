import random
# for number in range(5,10,2):
#     print(number)
#
# surnames = ["Rivest", "Shamir", "Adleman"]
# for pos, surname in enumerate(surnames):
#     print(pos, surname)
#
# n = 39
# remainders = []
# while n > 0:
#     n, remainder = divmod(n,2)
#     remainders.append(remainder)
# remainders.reverse()
# print(remainders)
#
# print('Enter your name:')
# x = input()
# print('Hello, ' + x)

# def outer():
#     test = 1
#     def inner():
#         global test
#         test = 2
#         print("inner:", test)
#     inner()
#     print("outer:", test)
#
#
# test = 0
# outer()
# print("global:",test)

# def inner():
#     nonlocal test
#     test = 2
#     print("inner:", test)
#
#
# def outer():
#     test = 1
#     inner()
#     print("outer:", test)
#
#
# test = 0
# outer()
# print("global:",test)

#
# x = [1,2,3]
# def func(x):
#     x[1] = 42
#     x = "something else"
#     print(x, id(x))
#
#
# func(x)
# print(x, id(x))


# iterable unpacking
# def func(a,b,c):
#     print(a,b,c)
#
#
# values = (1,3,-7)
# func(*values)
#
# # dictionary unpacking
#
# valuesFromDict = {"b":1, "c":2, "a":42}
# func(**valuesFromDict)
#


# def kwo(*a, c):
#     print(a, c)
#
#
# kwo(1, 2, 3, c=5)


# def my_testing_func(p1, p2, /, p_or_kw, *, kw):
#     print(p1, p2, p_or_kw, kw)
#
#
# my_testing_func(1, 2, 3, kw=5)


# def my_testing_func(p1, p2=None, /, p_or_kw=None, *, kw):
#     print(p1, p2, p_or_kw, kw)
#
#
# my_testing_func(1, 2, 3, kw=5)
#


# def factorial(n):
#     if n in (0,1):
#         return 1
#     result = n
#     for k in range(2,n):
#         result *= k
#     return result
#
#
# f5 = factorial(4)
# print(f5)

# from functools import reduce
# from operator import mul
#
#
# def factorial(n):
#     return reduce(mul, range(1, n+1), 1)
#
#
# f5 = factorial(5)
# print(f5)


# # iterative solution
# def fibonacci_numbers(upto):
#     if upto == 0:
#         print(0)
#     elif upto > 1:
#         n = 1
#         prev = 1
#         pprev = 0
#         print(0)
#         print(1)
#         while n < upto:
#             currnum = prev + pprev
#             pprev = prev
#             prev = currnum
#             print(currnum)
#             n += 1
#     else:
#         print(0)
#         print(1)
#
#
# # fibonacci_numbers(7)
#
#
# # recursive solution
# def fibonacci_number_recursive(num):
#     if num >= 2:
#         return fibonacci_number_recursive(num-1) + fibonacci_number_recursive(num-2)
#     elif num == 1:
#         return 1
#     elif num == 0:
#         return 0
#
#
# def print_fibonacci_numbers_recursive(upto):
#     n = 0
#     while n <= upto:
#         print(fibonacci_number_recursive(n))
#         n += 1
#
#
# print_fibonacci_numbers_recursive(7)


# # length of a string
# def length_of_string(input_string):
#     n = 0
#     for character in input_string:
#         n += 1
#     return n
#
#
# print(length_of_string(""))
#
# print("")
#
#
# def length_of_string_recursive(input_string):
#     if input_string == "":
#         return 0
#     elif input_string[:-1] == "":
#         return 1
#     else:
#         return length_of_string_recursive(input_string[:-1]) + 1
#
#
# print(length_of_string_recursive("Das ist ein ganz toller Satz!"))
#


# def multiplication(a, b=1):
#     """Return a multiplied by b."""
#     return a * b
#
# dir(__builtins__)
#
#
#
# print(multiplication(2,3))

# # list comprehension test
#
# my_list = [n**2 for n in range(10)]
#
# print(my_list)
#
# # same with the map function
#
# my_list_mapped = list(map(lambda n: n**2, range(10)))
#
# print(my_list_mapped)
#
# ## same with for loop
#
# my_list_looped = []
#
# for n in range(10):
#     my_list_looped.append(n**2)
#
# print(my_list_looped)
#
#
# # smart example with list comprehension
#
# items = "ABCD"
# pairs = [(items[a], items[b]) for a in range(len(items)) for b in range(a, len(items))]
#
# print(pairs)


# pythagorean triple (a, b, c) must be intergers
#
# from math import sqrt
#
# search_until = 10
#
# triples = [(a, b, sqrt(a**2 + b**2)) for a in range(1, search_until) for b in range(a, search_until)]
#
# print(triples)
#
# # now we filter them
#
# triples_filtered = [(a, b, int(c)) for a,b,c in triples if c.is_integer()]
#
# print(triples_filtered)
#
#
# # combine into one list comprehension
#
# triples_faster = [
#     (a, b, int(c)) for a in range(1, search_until) for b in range(a, search_until)
#     if (c := sqrt(a**2 + b**2)).is_integer()
# ]
#
# print(triples_faster)
#
#
# # # also works for dictionaries and sets
#
# from string import ascii_lowercase
#
# lettermap = {c: k for k,c in enumerate(ascii_lowercase, 1)}
#
# print(lettermap)
#
# # same with using generator expression
#
# lettermap2 = dict((c,k) for k,c in enumerate(ascii_lowercase, 1))
#
# print(lettermap2)
#
# # set examplel
#
# # random numbers // with increasing range // written as generator
# random_numbers = (random.randrange(a) for a in range(1, 10))
# print(random_numbers)
#
# numbers = [a for a in range(10)]
# letters1 = set(num for num in random_numbers)
# print(letters1)
#
#
# print(random.randrange(10))


# # examples for generator functions
#
# def get_squares_gen(n):
#     for x in range(n):
#         yield x**2
#
#
# print(list(get_squares_gen(10)))
#
# # we can create generoator object with this
#
# squares = get_squares_gen(4)
#
# print(squares)
# print(next(squares))
# print(next(squares))
# print(next(squares))
# print(next(squares))
# # print(next(squares)) # exhausted

# smarter to read with yield from expression
#
#
# def print_squares(start, end):
#     yield from (n**2 for n in range(start, end))
#
#
# print(list(print_squares(1,20)))
#
# # generators
#
# s1 = sum([n**2 for n in range(10**6)])
# s2 = sum((n**2 for n in range(10**6)))
# s3 = sum(n**2 for n in range(10**6)) # short form of generator
#
# print(s1, s2, s3)

# very smart fibonacci numbers

# def fibonacci(N):
#     """Return all fibonacci numbers up to N."""
#
#     a, b = 0, 1
#     while a <= N:
#         yield a
#         a, b = b, a + b
#
#
# print(list(fibonacci(50)))

# from time import sleep, time
#
#
# def f():
#     sleep(0.3)
#
#
# def g():
#     sleep(0.5)
#
#
# t = time()
# f()
# print("f took:", time()-t)
# t = time()
# g()
# print("g took:", time()-t)

# first decorator example

#
# from time import sleep, time
# from functools import wraps
#
#
# def measure(func):
#     @wraps(func)
#     def wrapper(*args, **kwargs):
#         t = time()
#         func(*args, **kwargs)
#         print(func.__name__, "took:", time()-t)
#     return wrapper
#
#
# @measure
# def f(sleep_time=0.1):
#     """ Just to have some time passing for testing. """
#     sleep(sleep_time)
#
#
# f(sleep_time=10)

# some more examples/ variants


from time import sleep, time
# from functools import wraps
#
#
# def measure(func):
#     @wraps(func)
#     def wrapper(*args, **kwargs):
#         t = time()
#         result = func(*args, **kwargs)
#         print(func.__name__, "took:", time()-t)
#         return result
#     return wrapper
#
#
# def max_result(func):
#     @wraps(func)
#     def wrapper(*args, **kwargs):
#         result = func(*args, **kwargs)
#
#         if result > 10000:
#             print(f"Result is too big ({result}).", "Max allowed is 10000.")
#         return result
#     return wrapper
#
#
# @measure #decorator
# @max_result
# def cube(n):
#     # sleep(0.01)
#     return n**3
#
#
# print(cube(100))


# # decorators with arguments
# from time import sleep, time
# from functools import wraps
#
#
# def max_result(threshold):
#     def decorator(func):
#         @wraps(func)
#         def wrapper(*args, **kwargs):
#             result = func(*args, **kwargs)
#
#             if result > threshold:
#                 print(f"Result is too big ({result}).", f"Max allowed is {threshold}.")
#             return result
#
#         return wrapper
#     return decorator
#
#
# @max_result(75)
# def cube(n):
#     return n**3
#
#
# @max_result(100)
# def square(n):
#     return n**2
#
#
# @max_result(1000)
# def multiply(a, b):
#     return a * b
#
#
# print(cube(5))
# print(square(12))
# print(multiply(120, 10))
#


# # classes and objects
#
# class Simplest:
#     pass
#
#
# print(type(Simplest))
#
# simp = Simplest()
# print(type(simp))
#
# print(type(simp) is Simplest)
# #
#
# class Person:
#     species = "Human"
#
#
# print(Person.species)
#
#
# Person.alive = True
#
# print(Person.alive)
#
# man = Person()
#
# print(man.alive)
# print(man.species)
#
#
# Person.happy = True
#
# print(man.happy) # can use happy
#
# man.name = "Darth"
#
# # print(Person.name) - error

# there is attribute shadowing
#
# class Point:
#     x = 10
#     y = 7
#
#
# p = Point()
#
# print((p.x, p.y))
#
# p.x = 12
#
# print((p.x, p.y))  # takes x from instance
# print((Point.x, Point.y))
#
# del p.x
# print((p.x, p.y))  # looks for x in class
#
# p.z = 3
#
# print((p.x, p.y, p.z))

#
# class Square:
#     side = 8
#
#     def area(self):
#         return self.side**2
#
#
# sq = Square()
# print(sq.area())
# print(Square.area(sq))
# sq.side = 10
# print(sq.area())


# add initialization to the class

# class Rectangle:
#     def __init__(self, side_a, side_b):
#         self.side_a = side_a
#         self.side_b = side_b
#
#     def area(self):
#         return self.side_a * self.side_b
#
#
# r1 = Rectangle(10, 4)
#
# print((r1.side_a, r1.side_b))
#
# print(r1.area())
#
# r2 = Rectangle(7, 3)
# print(r2.area())

# from class_inheritance import Car, RaceCar, CityCar, F1Car
#
# car = Car()
# racecar = RaceCar()
# citycar = CityCar()
# f1car = F1Car()
#
# # cars = [car, racecar, citycar, f1car]
# #
# # for car in cars:
# #     car.start()
# # check the relations
# print(isinstance(car, Car))
#
# print(isinstance(f1car, RaceCar))
#
# print(issubclass(RaceCar, Car))
#
#
# # how to make inheritance properly use super()
#
# class Book:
#     def __init__(self, title, publisher, pages):
#         self.title = title
#         self.publisher = publisher
#         self.pages = pages
#
#
# class Ebook(Book):
#     def __init__(self, title, publisher, pages, format_):
#         super().__init__(title, publisher, pages)
#         self.format_ = format_
#
#
# ebook = Ebook("Learn Python Programming", "Packt Publishing", 500, "PDF")
#
# print((ebook.title, ebook.publisher, ebook.pages, ebook.format_))
#
#
# from Multiple_inheritance import RegularHexagon, RegularPolygon, Square, Shape, Plotter, Polygon
#
# hexagon = RegularHexagon(10)
# print(hexagon.area())
#
# print(hexagon.get_geometric_type())
# hexagon.plot(0.8, (75, 77))
# square = Square(12)
# print(square.area())
# print(square.get_geometric_type())
# square.plot(0.93, (74, 75))
#
#
# # show in which class python is looking
# print(square.__class__.__mro__)

# palindrome example
# from static_methods import StringUtil
#
# print(StringUtil.is_palindrome("Radar", case_insensitive=True))
# print(StringUtil.is_palindrome("A nut for a jar of tuna"))
# print(StringUtil.is_palindrome("Never Odd, Or Even!"))
#
# print(StringUtil.get_unique_words("Hallo Hallo Ich mag die Palindrome wirklich wirklich sehr sehr sehr gerne"))
#

# from property_decorator import PersonPythonic
#
# person = PersonPythonic(39)
# print(person.age)
#
# person.age = 42
# print(person.age)
#
# # person.age = 100

# cacheing

# from cached_property import Manager, Client, ManualCacheManager, CachedPropertyManager
#
# client = Client()
#
# manager = Manager()
# manager.perform_query()
#
# manual_manager = ManualCacheManager()
# manual_manager.perform_query()
# manual_manager.perform_query()
#
# cached_property_manager = CachedPropertyManager()
#
# cached_property_manager.perform_query(object_id=42)
# cached_property_manager.perform_query(name_ilike="%Python%")
#
# del cached_property_manager.client
# cached_property_manager.perform_query(age_gte=18)


# # operator overloading
#
# from operator_overloading import Weird
#
# # weird = Weird("Hello! I am 9 years old!")
# weird = Weird("Hello! I am 42 years old!")
# weird2 = Weird("Hello! I am 10 years old!")
# print(len(weird))
# print(bool(weird))
#
# weird3 = weird + weird2
#
# print(bool(weird3))
# print(weird3._s)

# # data classes
# from dataclasses_example import Body
#
# body = Body("Ball", 19, 3.1415)
# print(body.kinetic_energy(), body.kinetic_energy_unit)
# print(body)
# print(body.name)
# print(body.mass, body.mass_unit)
# print(body.speed, body.speed_unit)
# print(body.momentum(), body.momentum_unit)

# own iterators
from math import ceil
from iterator_examples import OddEven, FrontBack

# oddeven = OddEven("0123456789")
# print(oddeven.indexes)
# print(oddeven.__next__())
# print(next(oddeven))
# print("".join(c for c in oddeven))
#
# oddeven2 = OddEven("ABC")
# it = iter(oddeven2)
# print(it)
# print(next(it))
# print(next(it))
# print(next(it))
# # print(next(it)) # throws error
#
# frontback = FrontBack("Das könnte sehr verwirrend sein")
# # frontback = FrontBack("aaaaabbbbb")
# print(frontback.indexes)
#
# print("".join(c for c in frontback))
# # print(ceil(len("123456789")/2))
# # print(list(range(0, ceil(len("123456789")), 2)))
# # print(len("123456789"))
# # print(list(range(0,8,0.5)))


# # local context manager
#
# from decimal import Context, Decimal, localcontext
#
# one = Decimal("1")
# three = Decimal("3")
# with localcontext(Context(prec=5)) as ctx:
#     print("Custom decimal context:", one/three)
# print("Original context restored:", one/three)
#

# # can be used in context of files:
#
# from decimal import Context, Decimal, localcontext
#
# one = Decimal("1")
# three = Decimal("3")
# with (localcontext(Context(prec=5)), open("output.txt", "w") as out_file):
#     out_file.write(f"{one}/{three} = {one/three}\n")
# # this handles the file well, it is closed after we leave the localcontext


from own_context_manager_example import MyContextManager

# contextmanager = MyContextManager()
# #
# # contextmanager.__enter__()
# # contextmanager.__exit__("a","b","c")
#
# with contextmanager as ctx:
#     print("inside the new context")
#     print(id(ctx))
#     raise Exception("Exception inside 'with' context")
#     print("this line will never be reached")
#
# print("After 'with context")
#
# # alternatively


# with MyContextManager() as ctx:
#     print("inside the new context")
#     print(ctx)
#     # ctx.__exit__("a","b","c")
#     raise Exception("Exception inside 'with' context")
#     print("this line will never be reached")
#
# print("After 'with context")

# from contextmanager_generator_example import my_context_manager, measure, exit_loop_exception, ExitLoopException, solve_equation_42a_17b_c
# from time import sleep
# # print("about ot enter 'with' context")
# # with my_context_manager() as val:
# #     print("inside 'with' context")
# #     print(id(val))
# #     raise Exception("Excepiton inside 'wioth' context")
# # print("After 'with' context")
# #
# #
# # # val is still available
# #
# # print(val)
#
# with measure() as t:
#     sleep(0.5)
#     raise Exception("Excepiton inside 'wioth' context")
#
# print(f"we are out, Start time was {t}")
#
# sleep(0.6)
#
# # container work around
# print(f"Time passed till here: {time()-t}")
# result = []
# with exit_loop_exception(result) as ele:
#     n = 100
#     for a in range(n):
#         for b in range(n):
#             for c in range(n):
#                 if 42 * a + 17 * b + c == 5096:
#                     raise Exception(a, b, c)
#
#
# print(result)
#
# with ExitLoopException() as ele:
#     solve_equation_42a_17b_c()
#
# print(ele.result)  # now we can use the elements from the class directly
#
# with ExitLoopException() as ele:
#     solve_equation_42a_17b_c(100, 4096)
#
# print(ele.result)  # now we can use the elements from the class directly
#
# # solve_equation_42a_17b_c(100, 4096)
#
