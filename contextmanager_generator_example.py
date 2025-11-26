
from contextlib import contextmanager
from time import time

@contextmanager
def my_context_manager():
    print("Entering 'with' context")
    val = object()
    print(id(val))
    try:
        yield val
    except Exception as e:
        print(f"{type(e)=}{e=}{e.__traceback__=}")
    finally:
        print("Exiting 'with' context")


@contextmanager
def measure():
    t = time()
    try:
        yield t
    except Exception as e:
        print(f"{type(e)=}{e=}{e.__traceback__=}")
    finally:
        print("Took:", time()-t)


# context manager to exit loop on exception =) nice I like it
@contextmanager
def exit_loop_exception(container):
    print("Entering 'with' context")
    try:
        yield
    except Exception as e:
        print("Exception occurred", e)
        print(e.args)
        container[:] = e.args
    finally:
        print("Exiting 'with' context")


# class based approach - here we can return after exception
class ExitLoopException:
    def __enter__(self):
        print("Entering 'with' context")
        self.result = None
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_val:
            self.result = exc_val.args
            return True

        print("Exiting 'with' context")
        return False


def solve_equation_42a_17b_c(range_num=100, equals=5096):
    for a in range(range_num):
        for b in range(range_num):
            for c in range(range_num):
                if 42 * a + 17 * b + c == equals:
                    raise Exception(a, b, c)

