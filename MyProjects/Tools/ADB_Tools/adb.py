import subprocess

import cv2
import numpy as np


class ADB:
    def __init__(self, device_id):
        """
        Initializes an ADB object with the specified device ID.

        Args:
            device_id (str): The ID of the device to connect to.
        """
        self.device_id = device_id

    def screen_capture(self, name):
        """
        Captures the screen of the connected device and saves it as an image file.

        Args:
            name (str): The name of the image file to save.
        """
        subprocess.run(f"adb -s {self.device_id} exec-out screencap -p > {name}.png ", shell=True)

    def click(self, x, y):
        """
        Simulates a tap on the screen of the connected device at the specified coordinates.

        Args:
            x (int): The x-coordinate of the tap.
            y (int): The y-coordinate of the tap.
        """
        subprocess.run(f"adb -s {self.device_id} shell input tap {x} {y}", shell=True)

    def find(self, img=None, template_pic_name=False, threshold=0.99):
        """
        Finds the specified image on the screen of the connected device.

        Args:
            img (str): The path to the image to search for.
            template_pic_name (str): The name of the template image file to save. If not provided, a screenshot will be captured.
            threshold (float): The threshold value for matching similarity. Defaults to 0.99.

        Returns:
            list: A list of tuples representing the coordinates of the found image on the screen.
        """
        if img is None:
            raise ValueError("The 'img' argument must be provided with a valid image path.")
        if not template_pic_name:
            self.screen_capture(self.device_id)
            template_pic_name = self.device_id + '.png'
        else:
            self.screen_capture(template_pic_name)
        img = cv2.imread(img)
        img2 = cv2.imread(template_pic_name)
        result = cv2.matchTemplate(img, img2, cv2.TM_CCOEFF_NORMED)
        loc = np.where(result >= threshold)
        test_data = list(zip(*loc[::-1]))
        return test_data