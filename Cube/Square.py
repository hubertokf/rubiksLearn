class Square:
    def __init__(self, color="red", center=False):
        self.color = color
        self.isCenter = center
        self.colorRef = self.getColorRef(color)
        self.colorHex = self.getColorHex(color)

    def __str__(self):
        return self.color

    def getColorRef(self, color):
        if color == "white":
            return 1
        if color == "red":
            return 2
        if color == "blue":
            return 3
        if color == "green":
            return 4
        if color == "yellow":
            return 4
        if color == "orange":
            return 4

    def getColorHex(self, color):
        if color == "white":
            return "#FFFFFF"
        if color == "red":
            return "#FF0000"
        if color == "blue":
            return "#0000FF"
        if color == "green":
            return "#00FF00"
        if color == "yellow":
            return "#ffff00"
        if color == "orange":
            return "#ffa500"
