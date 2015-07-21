def addarg(uarg):
    "Returns a decorator that adds a given argument to a function"
    def decorator(f):
        "Decorates the function"
        def wrapper(*args, **kw):
            "return the function with additional argument"
            return f(uarg, *args, **kw)
        return wrapper
    return decorator

