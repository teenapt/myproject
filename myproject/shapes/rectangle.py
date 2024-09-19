# shapes/rectangle.py

class Rectangle:
    def __init__(self, length: int, width: int):
        self.length = length
        self.width = width

    def __iter__(self):
        yield {'length': self.length}
        yield {'width': self.width}

    def __repr__(self):
        return f"Rectangle(length={self.length}, width={self.width})"
