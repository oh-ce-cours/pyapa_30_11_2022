import typing

T = typing.TypeVar("T")


def est_pair(nombre):
    return nombre % 2 == 0


def my_filter(f: typing.Callable[[T], bool], iterable: typing.Iterable[T]) -> list[T]:
    res = []
    for item in iterable:
        if f(item):
            res.append(item)
    return res


print(list(filter(est_pair, range(10))))
print(list(my_filter(est_pair, range(10))))
