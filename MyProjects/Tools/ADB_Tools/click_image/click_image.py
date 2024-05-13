from adb import ADB


def main():
    """
    The main function that demonstrates the usage of the ADB class.
    """
    d = ADB('8ba035070522')
    point = d.find('gg_icon.png')
    if point:
        print(point)
        d.click(point[0][0], point[0][1])
    else:
        print("No match found.")


if __name__ == "__main__":
    main()
