from datetime import datetime

RED = "\033[31m"
GRAY = "\033[90m"
BLACK = "\033[30m"
NORM = "\033[0m"


def print_colored(color, msg):
    """
    Prints provided message in color. See predefined variables above.
    :param color: Color variable or color code in "\033[30m" format
    :param msg: Message/object to be printed
    """
    print(f"{color + msg + NORM}")


def info(func):
    """
    Prints name of the function, start, end and execution time.
    :param func: callable function
    :return:
    """
    def wrapper(*args, **kwargs):
        start = datetime.now()
        print_colored(BLACK, f"[{start.strftime("%H:%M:%S")}][START] {func.__module__}.{func.__name__}()")
        # print(f"{GRAY}[{start.strftime("%H:%M:%S")}][START] {func.__module__}.{func.__name__}(){NORM}")
        result = func(*args, **kwargs)
        end = datetime.now()
        spent = round((end - start).total_seconds() * 1000)
        print_colored(BLACK, f"[{end.strftime("%H:%M:%S")}][ END ] {func.__module__}.{func.__name__}(), {spent} ms")
        # print(f"{GRAY}[{end.strftime("%H:%M:%S")}][ END ] {func.__module__}.{func.__name__}(), {spent} ms{NORM}")
        return result

    return wrapper
