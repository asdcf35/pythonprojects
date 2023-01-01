def iterable(func):
    """Resolve $ref schemas."""

    def inner(times, *args, **kwargs):
        """Replace function."""
        # Checking for $ref
        if times == 0:
            return "None"
        else:
            func(*args,**kwargs)
            return inner(times - 1, *args, **kwargs)

    return inner
@iterable
def hi(helps):
    print(helps)

hi("hello")