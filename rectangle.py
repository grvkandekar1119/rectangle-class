class Rectangle:
    """A rectangle defined by integer length and width.

    Iterating over an instance yields two dictionaries, in order:
        {'length': <length>}
        {'width': <width>}
    """

    def __init__(self, length: int, width: int):
        if not isinstance(length, int) or not isinstance(width, int):
            raise TypeError("length and width must be integers")
        self.length = length
        self.width = width

    def __iter__(self):
        yield {'length': self.length}
        yield {'width': self.width}


if __name__ == "__main__":
    rect = Rectangle(10, 5)
    for item in rect:
        print(item)
    # Output:
    # {'length': 10}
    # {'width': 5}

    print(list(rect))
    # [{'length': 10}, {'width': 5}]
