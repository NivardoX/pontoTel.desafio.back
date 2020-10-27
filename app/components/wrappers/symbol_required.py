def symbol_required(func):
    def wrapper(*args, **kwargs):
        if args[0].symbol is not None:

            return func(*args, **kwargs)

        else:
            raise Exception("Symbol not defined")

    return wrapper
