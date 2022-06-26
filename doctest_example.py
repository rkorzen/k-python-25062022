def suma(a: int, b: int) -> int:
    """Suma dwóch argumentów:
    >>> suma(1, 2)
    3

    >>> suma(-1, -2)
    -3

    >>> suma(0, 0)
    0

    """
    return a + b

if __name__ == "__main__":
    import doctest
    doctest.testmod()