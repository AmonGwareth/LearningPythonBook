import decimal
import json
import fractions
from datetime import date


class ComplexEncoder(json.JSONEncoder):
    def default(self, obj):
        print(f"ComplexEncoder.default: {obj=}")
        if isinstance(obj, complex):
            return {
                "_meta": "complex",
                "num": [obj.real, obj.imag],
            }


def object_hook(obj):
    print(f"object_hook: {obj=}")
    try:
        if obj["_meta"] == "complex":
            return complex(*obj["num"])
    except KeyError:
        return obj


class FractionEncoder(json.JSONEncoder):
    def default(self, o):
        print(f"ComplexEncoder.default: {o=}")
        if isinstance(o, fractions.Fraction):
            return {
                "_meta": "fraction object",
                "fraction": [o.numerator, o.denominator],
            }


def fraction_hook(o):
    print(f"object_hook: {o=}")
    try:
        if o["_meta"] == "fraction object":
            return fractions.Fraction(*o["fraction"])
    except KeyError:
        return o


class DecimalEncoder(json.JSONEncoder):
    def default(self, o):
        print(f"ComplexEncoder.default: {o=}")
        if isinstance(o, decimal.Decimal):
            return {
                "_meta": "decimal object",
                "decimal": str(o),
            }


def decimal_hook(o):
    print(f"object_hook: {o=}")
    try:
        if o["_meta"] == "decimal object":
            return decimal.Decimal(o["decimal"])
    except KeyError:
        return o


class DatetimeDateEncoder(json.JSONEncoder):
    def default(self, o):
        print(f"ComplexEncoder.default: {o=}")
        if isinstance(o, date):
            return {
                "_meta": "date object from datetime",
                "date": [o.year, o.month, o.day],
            }


def datetime_date_hook(o):
    print(f"object_hook: {o=}")
    try:
        if o["_meta"] == "date object from datetime":
            return date(*o["date"])
    except KeyError:
        return o


