import functools


def duplicar (func):
    @functools.wraps(func)
    def envelope(*args, **kwargs):
        print("Antes")
        func(*args, **kwargs)
        print("Depois")

    return envelope

@duplicar
def hello(nome):
    return print(f"Hello {nome}")

hello("Vinicius")

print(hello.__name__)