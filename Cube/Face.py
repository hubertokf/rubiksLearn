from .Square import Square


class Face:
    def __init__(self, color):
        self.squares = self.createFace(color)

    def __str__(self):
        return """
            {0}\t{1}\t{2}\n
            {7}\t \t{3}\n
            {6}\t{5}\t{4}
        """.format(
            *list(map(lambda x: str(x), self.squares))
        )

    def createFace(self, color):
        squares = []
        for i in range(8):
            squares.append(Square(color))

        return squares

    def rotate(self, counter_clockwise, rotations):
        moves = rotations * 3
        if not counter_clockwise:
            moves = moves * -1

        return self.squares[moves:] + self.squares[:moves]

    def rotate_from_outside(self, input, side):
        end = side * 2
        start = end - 2
        output = self.squares[start:end]
        self.squares[start:end] = input
        return output

    def get_side(self, side):
        start = side * 2
        end = start + 2
        return self.squares[start:end]

    def set_side(self, input, side):
        start = side * 2
        end = start + 2
        self.squares[start:end] = input

        return self.squares
