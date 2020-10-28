from typing import Callable

from app.components.exceptions.SymbolNotDefinedException import (
    SymbolNotDefinedException,
)


def symbol_required(func: Callable) -> Callable:
    def wrapper(*args, **kwargs):
        if args[0].symbol is not None:

            return func(*args, **kwargs)

        else:
            raise SymbolNotDefinedException("Symbol not defined")

    return wrapper
