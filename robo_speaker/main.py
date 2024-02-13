"""simple program to implement text to speech"""

import os
import platform

system_os = platform.system()
COMMAND = "wsay.exe" if "windows" in system_os.lower() else "say"

if __name__ == "__main__":
    print("\nWelcome to RoboSpeaker 1.1. Created by Manish")
    while True:
        x = input("\nEnter what you want me to say: ")
        if x == "q":
            EXIT_SOUND = "See you later my friend!"
            os.system(f'{COMMAND} "{EXIT_SOUND}"')
            break
        os.system(f'{COMMAND} "{x}"')
