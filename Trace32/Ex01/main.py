from datetime import datetime
import base64
import sys
import os
import re
import time
import configparser
import urllib.parse
import ctypes
import subprocess
import platform
import enum
import array
import struct
import argparse
import glob
import shutil
import logging

logger = logging.getLogger(__name__)
logging.basicConfig(
    level=logging.DEBUG,
    handlers=[logging.StreamHandler()],
    datefmt="%Y-%m-%d %H:%M:%S",
    format="[%(asctime)s %(levelname)s] --> %(module)s: %(message)s"
)

SOURCE_CODE_PATH = os.path.abspath(os.path.dirname(__file__))
TRACE32_INSTALLATION = "C:\\TCC\\Tools\\trace32\\bosch_2019_r2_alpha6fp_WIN64"
T32_EXE = os.path.join(TRACE32_INSTALLATION, "bin", "windows64", "t32marm.exe")


class Trace32:
    def __init__(self):
        pass

    def run(self):
        logging.info(f"SOURCE_CODE_PATH: {SOURCE_CODE_PATH}")
        logging.info(f"TRACE32_INSTALLATION: {TRACE32_INSTALLATION}")
        logging.info(f"T32_EXE: {T32_EXE}")

        cmd = [f"{T32_EXE}", "-c", f"{SOURCE_CODE_PATH}\\Lauterbach\\config.t32", "20000", "Wind", "USB", "CORE=1",
               "-s",
               f"{SOURCE_CODE_PATH}\\Lauterbach\\start_powerview_Debug_ON.cmm"]
        subprocess.Popen(cmd)
        time.sleep(5)


if __name__ == "__main__":
    trace32 = Trace32()
    trace32.run()
