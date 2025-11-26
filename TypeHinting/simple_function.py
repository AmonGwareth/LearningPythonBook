#
#
# def hypotenuse(a: float, b: float) -> float:
#     return (a**2 + b**2) ** 0.5
#
#
# print(hypotenuse(3, 4))
# print(hypotenuse(3.5, 4.9))
# # print(hypotenuse(complex(1, 2), 10))

from collections.abc import Iterable


def title(names: Iterable[str | bytes]) -> list[str | bytes]:
    return [name.title() for name in names]


print(title(["ALICE", "bob"]))
print(title([b"ALICE", b"bob"]))
