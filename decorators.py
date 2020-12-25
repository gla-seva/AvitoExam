from random import randint


def log(template: str):
    def decorator(func):
        def wrapper(*args, **kwargs):
            ret = func(*args, **kwargs)
            print(template.format(randint(1, 10)))
            return ret

        return wrapper

    return decorator
