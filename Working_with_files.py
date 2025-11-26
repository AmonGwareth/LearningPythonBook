import decimal
import fractions
import json

# fh = open("The_Firefly_and_the_Lantern.txt","rt")
# for line in fh.readlines():
#     print(line.strip())
# fh.close()

# # make it save and simplfy --> use defaults
#
# fh = open("The_Firefly_and_the_Lantern.txt")
# try:
#     for line in fh:
#         print(line.strip())
# finally:
#     fh.close()

# # open can be used as context manager
# with open("The_Firefly_and_the_Lantern.txt") as fh:
#     for line in fh:
#         print(line.strip())
#
# # print to the file
# with open("print_example.txt","w") as fw:
#     print("Hey I am printing into a file!!!", file=fw)


# with open("The_Firefly_and_the_Lantern.txt") as f:
#     lines = [line.rstrip() + "___LineEnd___" for line in f]
# with open("My_text_copy.txt", "w") as fw:
#     fw.write("\n".join(lines))

# # test open as binary
# with open("The_Firefly_and_the_Lantern.txt", "rb") as f:
#     print(f.read())
#
# # open with overwrite protection
#
# with open("print_example.txt", "x") as fw:
#     fw.write("test")

# from pathlib import Path
# p = Path("fear.txt")
# path = p.parent.absolute()
# print(p.is_file())
# print(path)
# print(path.is_dir())
# q = Path(r"E:\python\LearningPythonBook")
# print(q.is_dir())


# # manipulation of files and directories
#
# from collections import Counter
# from string import ascii_letters
#
# chars = ascii_letters + ""
#
#
# def sanitize(s, chars):
#     """Filters a String for ascii characters"""
#     return "".join(c for c in s if c in chars)
#
#
# def reverse_string(s):
#     return s[::-1]
#
#
# with open("The_Firefly_and_the_Lantern.txt") as stream:
#     lines = [line.rstrip() for line in stream]
#
# with open("The_Firefly_and_the_Lantern_reversed.txt", "w") as stream:
#     stream.write("\n".join(reverse_string(line) for line in lines))
#
# lines = [sanitize(line, chars) for line in lines]
# whole = "".join(lines)
#
# cnt = Counter(whole.lower().split())
#
# print(cnt.most_common(3))


# # shutil module
#
# import shutil
# from pathlib import Path
#
# base_path = Path("ops_example")
#
# # intitial cleanup
# if base_path.exists() and base_path.is_dir():
#     shutil.rmtree(base_path)
#
# # create directory
# base_path.mkdir()
# path_b = base_path/"A"/"B"
# path_c = base_path/"A"/"C"
# path_d = base_path/"A"/"D"
# path_b.mkdir(parents=True)  # creates path including parents
# path_c.mkdir()  # parent is already there
#
# # add files to the directories
# for filename in ("ex1.txt", "ex2.txt", "ex3.txt"):
#     with open(path_b / filename, "w") as stream:
#         stream.write(f"Some content here in {filename}\n")
#
# shutil.move(path_b, path_d)  # moves the dir
#
# # renaming
# ex1 = path_d / "ex1.txt"
# ex1.rename(ex1.parent / "ex1_renamed.txt")
#

# # manipulate pathnames
#
# from pathlib import Path
# p = Path("ex2.txt")
# print(p.absolute())
# print(p.name)
# print(p.parent.absolute())
# print(p.suffix)
# print(p.parts)
# print(p.absolute().parts)
#
# # readme
# # test_path = p.parent
# # print(p.parent / "..")

# # use temporary files and dirs for testing
#
# from tempfile import NamedTemporaryFile, TemporaryDirectory
#
# with TemporaryDirectory(dir=".") as td:
#     print("TemporaryDirectory:", td)
#     with NamedTemporaryFile(dir=td) as t:
#         name = t.name
#         print(name)

# # visualize content of directory
#
# from pathlib import Path
# p = Path(".")
# for entry in p.glob("*"):
#     print("File:" if entry.is_file() else "Folder:", entry)
#
# iterator_test = p.glob("*")
# print(next(iterator_test))
# print(next(iterator_test))
# print(next(iterator_test))

# alternative with walk

# from pathlib import Path
# p = Path("E:\python\LearningPythonBook")  # gives current dir
#
# for root, dirs, files in p.walk():
#     print(f"{root=}")
#     if dirs:
#         print("Directories:")
#         for dir_ in dirs:
#             print(dir_)
#         print()
#     if files:
#         print("Files:")
#         for filename in files:
#             print(filename)
#         print()##

# # save as zp files
#
# from zipfile import ZipFile
#
# with ZipFile("example.zip","w") as zp:
#     zp.write("My_text_copy.txt")
#     zp.write("My_text_copy_reversed.txt")
#     # zp.write("subfolder/content3.txt")
#     # zp.write("subfolder/content4.txt")
# #
# with ZipFile("example.zip") as zp:
#     zp.extract("My_text_copy.txt", "extract_zip")
#     # zp.extract("subfolder/content3.txt", "extract_zip")


# using JSON files for saving

# import sys, json
#
# data = {
#     "big_number": 2**3141,
#     "max_float": sys.float_info.max,
#     "a_list": [2, 3, 5, 7],
# }
#
# json_data = json.dumps(data)  # create json data
# data_out = json.loads(json_data)  # from json back to python
# assert data == data_out  # checks with assertionError if data is matching
#
# print(json_data)
#
#
# from custom_encoder_example import ComplexEncoder, object_hook
#
# data = {
#     "an_int": 42,
#     "a_float": 3.14159265,
#     "a_complex": 3 + 4j,
# }
#
# json_data = json.dumps(data, cls=ComplexEncoder)
# data_out = json.loads(json_data, object_hook=object_hook)
#
# print(json_data)
# print(data_out)
#
#
# # # quick test to see what happens w.o custom decoder
# # json_data = json.dumps(data) #throws error
# # data_out = json.loads(json_data)
# #
# # print(json_data)
# # print(data_out)

# # task encoders for fractions and decimal objects
# from custom_encoder_example import FractionEncoder, DecimalEncoder, fraction_hook, decimal_hook
#
# my_fraction = fractions.Fraction(4, 5)
#
# data = {
#     "an_int": 42,
#     "a_float": 3.14159265,
#     "a_fraction": 4/5,
#     "a_fraction_object": my_fraction,
# }
# print(data)
# print(type(my_fraction))
# print(type(4 + 4j))
# print(fractions.Fraction)
# print(complex)
# print(my_fraction.numerator)
# print(my_fraction.denominator)
#
# json_data = json.dumps(data, cls=FractionEncoder)
# data_out = json.loads(json_data, object_hook=fraction_hook)
#
# print(json_data)
# print(data_out)
#
# print(data_out["a_fraction_object"].numerator)
#
#
# my_decimal = decimal.Decimal("1.1") + decimal.Decimal("2.2")  # string representaiton important!!
# my_float = 1.1 + 2.2
#
# data = {
#     "an_int": 42,
#     "a_float": my_float,
#     "a_decimal_object": my_decimal,
# }
#
# print(data)
# print(type(my_decimal))
#
# print(my_decimal)
# print(decimal.Decimal(str(my_decimal)))  # conert to string to keep precision
# print(my_float)
#
#
# json_data = json.dumps(data, cls=DecimalEncoder)
# data_out = json.loads(json_data, object_hook=decimal_hook)
#
# print(json_data)
# print(data_out)

# enconder for date object

# from datetime import date
# from custom_encoder_example import DatetimeDateEncoder, datetime_date_hook
# # get today's date
# my_date = date.today()
#
# print(my_date)
#
# print(date(2024,5,22))
#
#
# print(date(*[2024, 5, 22]))
#
#
# # test the en- and decoding
#
# data = {
#     "an_int": 2.55,
#     "a_date": my_date,
# }
#
# json_data = json.dumps(data, cls=DatetimeDateEncoder)
# data_out = json.loads(json_data, object_hook=datetime_date_hook)
#
# print(json_data)
# print(data_out)
#
# print(data_out["a_date"].year)

# iio streams

# import io
#
# # stream = io.StringIO()
# #
# # stream.write("Leearning Python Programming. \n")
# #
# # print("Become a Python ninja!", file=stream)
# # contents = stream.getvalue()
# # print(contents)
# # stream.close(
# #
# # as expected we can use it in a context =)
#
# with io.StringIO() as stream:
#     stream.write("Learning Python Programming. \n")
#     print("Become a Python ninja!", file=stream)
#     contents = stream.getvalue()
#     print(contents)

# HTTP requests
#
# import requests
#
# urls = {
#     "get": "https://httpbin.org/get?t=learn+python+programming",
#     # "headers": "https://httpbin.org/headers",
#     "ip": "https://httpbin.org/ip",
#     "user-agent": "https://httpbin.org/user-agent",
#     "UUID": "https://httpbin.org/uuid",
#     "JSON": "https://httpbin.org/json",
# }
#
#
# def get_content(title, url):
#     resp = requests.get(url)
#     print(f"Response for {title}")
#     print(resp.json())
#
#
# for title, url in urls.items():
#     get_content(title, url)
#     print("-" * 40)
#
# # send to the server (make a post)
# url = "https://httpbin.org/post"
# data = dict(title="Learn Python Programming")
# resp = requests.post(url, data=data)
# print("Response for POST")
# print(resp.json())


# using sqlalchemy

from sqlalchemy import create_engine, select, func
from sqlalchemy.orm import Session
from sql_alchemy_classes import Person, Email, Base

# setup the database
engine = create_engine("sqlite:///example.db")
Base.metadata.create_all(engine)

# connect to the database
with Session(engine) as session:
    anakin = Person(name="Anakin Skywalker", age=32)
    obione = Person(name="Obi-Wan Kenobi", age=40)

    obione.emails = [Email(email="obi1@example.com"), Email(email="wanwan@example.com")]
    anakin.emails.append(Email(email="ani@example.com"))

    # use session to actually add it
    session.add(anakin)
    session.add(obione)
    session.commit()

    # query the database

    obione = session.scalar(select(Person).where(Person.name.like("Obi%")))

    print(obione, obione.emails)

    anakin = session.scalar(select(Person).where(Person.name.like("Anakin Skywalker")))

    print(anakin, anakin.emails)

    # can delete from global frame but not from the database
    anakin_id = anakin.id
    del anakin




