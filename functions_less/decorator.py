


def decorated(func):
    def wrapped():
        S = func()
        return S + ' Python'
    return wrapped
@decorated
def f():
    return 'Hello world'
print(f())


def tag(tag_name):
def real_decorator(func):
    def wrapped():
        S = func()
        return f'<{tag_name} > {S} </{tag_name}>'
    return real_decorator
# x = decorator(tag(f())
@decorator
@tag('html')
def f():
    return ('Hello world')

print(f())