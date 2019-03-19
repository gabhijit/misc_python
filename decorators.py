# Trying to understand decorators

def wrapper_with_arguments(**kw):

    def inner(func):
        print ("kwargs:", kw)
        def wrapped(*args, **kwargs):
            print ("Wrapped")
            print ("args:", *args)
            print ("kwargs:", kw)
            first = kw.get('foo')
            second = kw.get('bar')
            result = func(first, second)

        return wrapped

    return inner

print (wrapper_with_arguments(foo=2, bar=3)(print)('hello'))

def add(a, b):
    return a + b

orig_add = add

wrapper_with_arguments(foo=1, bar=2)(add)(2,3)

add = wrapper_with_arguments(foo=3, bar=4)(add)
add(2,3)


def wrapper_sans_arguments(func):

    def wrapped(*arg, **kw):

        print ("args:", *arg)
        print ("kwargs:", **kw)
        return func(*arg, **kw)

    return wrapped

wrapper_sans_arguments(orig_add)(2, 3)

