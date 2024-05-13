import subprocess
import sys
import cv2
import numpy as np
from adb import ADB

sys.setrecursionlimit(10000)


def bypass_slide(image):
    image = cv2.imread(image)
    img = image[955:1519, 154:926]
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img3 = cv2.Canny(gray, 200, 200, L2gradient=True)
    kernel = np.ones([23, 23])
    kernel[2:, 2:] = -0.1
    im = cv2.filter2D(img3 / 255, -1, kernel)
    im1 = im[:, :125]
    y1, x1 = np.argmax(im1) // im1.shape[1], np.argmax(im1) % im1.shape[1]
    im2 = im[:, 125:]
    y2, x2 = np.argmax(im2) // im2.shape[1], np.argmax(im2) % im2.shape[1] + 125
    return x2 - x1


def slide_captcha(device, adb):
    adb.dumpXml(device)
    checktext = adb.findElementByName("Slider captcha verification")
    print(checktext)
    if checktext:
        # adb.excuteAdb(sr, "adb shell screencap -p /sdcard/cap.png")
        # adb.excuteAdb(sr, f"adb pull /sdcard/cap.png {sr}/captcha.png")
        check = adb.checkImage(device, "keo.png", device)
        if check and check['status'] == "success":
            captcha = bypass_slide(f"{device}/screen.png")
            adb.inputSwipe(device, round(check['x']), round(check['y']), int(check['x']) + int(captcha), round(check['y']),
                           1000)
        return True
    else:
        return False


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
