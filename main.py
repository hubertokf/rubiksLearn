from Cube import Cube


def main():
    cube = Cube(colors=["white", "red", "green", "blue", "yellow", "orange"])

    print(cube.get_side(0))
    cube.shuffle(20)
    print(cube.get_side(0))


if __name__ == "__main__":
    main()
