from .Face import Face
import random


class Cube:
    def __init__(self, colors=["white", "red", "green", "blue", "yellow", "orange"]):
        self.cube = self.createCube(colors)

    def __str__(self):
        return self.cube

    def createCube(self, colors):
        cube = []
        for color in colors:
            cube.append(Face(color))

        return cube

    def rotate(self, side, rotations, counter_clockwise):
        self.cube[side].rotate(counter_clockwise, rotations)
        for r in range(rotations):
            if side == 0:
                self.rotate_s0(counter_clockwise)
            if side == 1:
                self.rotate_s1(counter_clockwise)
            if side == 2:
                self.rotate_s2(counter_clockwise)
            if side == 3:
                self.rotate_s3(counter_clockwise)
            if side == 4:
                self.rotate_s4(counter_clockwise)
            if side == 5:
                self.rotate_s5(counter_clockwise)

        return self.cube

    def rotate_s0(self, counter_clockwise):
        # s00 - s50
        # s01 - s10
        # s02 - s40
        # s03 - s30
        s50 = self.cube[5].get_side(0)
        s10 = self.cube[1].get_side(0)
        s40 = self.cube[4].get_side(0)
        s30 = self.cube[3].get_side(0)
        if counter_clockwise:
            self.cube[5].set_side(s10, 0)
            self.cube[1].set_side(s40, 0)
            self.cube[4].set_side(s30, 0)
            self.cube[3].set_side(s50, 0)
        else:
            self.cube[5].set_side(s30, 0)
            self.cube[1].set_side(s50, 0)
            self.cube[4].set_side(s10, 0)
            self.cube[3].set_side(s40, 0)

    def rotate_s1(self, counter_clockwise):
        # s10 - s01
        # s11 - s53
        # s12 - s21
        # s13 - s41
        s01 = self.cube[0].get_side(1)
        s53 = self.cube[5].get_side(3)
        s21 = self.cube[2].get_side(1)
        s41 = self.cube[4].get_side(1)
        if counter_clockwise:
            self.cube[0].set_side(s53, 1)
            self.cube[5].set_side(s21, 3)
            self.cube[2].set_side(s41, 1)
            self.cube[4].set_side(s01, 1)
        else:
            self.cube[0].set_side(s41, 1)
            self.cube[5].set_side(s01, 3)
            self.cube[2].set_side(s53, 1)
            self.cube[4].set_side(s21, 1)

    def rotate_s2(self, counter_clockwise):
        # s20 - s52
        # s21 - s12
        # s22 - s42
        # s23 - s32
        s52 = self.cube[5].get_side(2)
        s12 = self.cube[1].get_side(2)
        s42 = self.cube[4].get_side(2)
        s32 = self.cube[3].get_side(2)
        if counter_clockwise:
            self.cube[5].set_side(s12, 2)
            self.cube[1].set_side(s42, 2)
            self.cube[4].set_side(s32, 2)
            self.cube[3].set_side(s52, 2)
        else:
            self.cube[5].set_side(s32, 2)
            self.cube[1].set_side(s52, 2)
            self.cube[4].set_side(s12, 2)
            self.cube[3].set_side(s42, 2)

    def rotate_s3(self, counter_clockwise):
        # s30 - s03
        # s31 - s43
        # s32 - s23
        # s33 - s51
        s03 = self.cube[0].get_side(3)
        s43 = self.cube[4].get_side(3)
        s23 = self.cube[2].get_side(3)
        s51 = self.cube[5].get_side(1)
        if counter_clockwise:
            self.cube[0].set_side(s43, 3)
            self.cube[4].set_side(s23, 3)
            self.cube[2].set_side(s51, 3)
            self.cube[5].set_side(s03, 1)
        else:
            self.cube[0].set_side(s51, 3)
            self.cube[4].set_side(s03, 3)
            self.cube[2].set_side(s43, 3)
            self.cube[5].set_side(s23, 1)

    def rotate_s4(self, counter_clockwise):
        # s40 - s02
        # s41 - s13
        # s42 - s22
        # s43 - s31
        s02 = self.cube[0].get_side(2)
        s13 = self.cube[1].get_side(3)
        s22 = self.cube[2].get_side(2)
        s31 = self.cube[3].get_side(1)
        if counter_clockwise:
            self.cube[0].set_side(s13, 2)
            self.cube[1].set_side(s22, 3)
            self.cube[2].set_side(s31, 2)
            self.cube[3].set_side(s02, 1)
        else:
            self.cube[0].set_side(s31, 2)
            self.cube[1].set_side(s02, 3)
            self.cube[2].set_side(s13, 2)
            self.cube[3].set_side(s22, 1)

    def rotate_s5(self, counter_clockwise):
        # s50 - s00
        # s51 - s33
        # s52 - s20
        # s53 - s11
        s00 = self.cube[0].get_side(0)
        s33 = self.cube[3].get_side(3)
        s20 = self.cube[2].get_side(0)
        s11 = self.cube[1].get_side(1)
        if counter_clockwise:
            self.cube[0].set_side(s33, 0)
            self.cube[3].set_side(s20, 3)
            self.cube[2].set_side(s11, 0)
            self.cube[1].set_side(s00, 1)
        else:
            self.cube[0].set_side(s11, 0)
            self.cube[3].set_side(s00, 3)
            self.cube[2].set_side(s33, 0)
            self.cube[1].set_side(s20, 1)

    def shuffle(self, iterations):
        for i in range(iterations):
            self.rotate(random.randint(0, 5), random.randint(1, 3), bool(random.getrandbits(1)))

    def get_side(self, side):
        return self.cube[side]
