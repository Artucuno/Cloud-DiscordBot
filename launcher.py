import logging
import sys
import os
import config
import random
import datetime
import subprocess
import time

def user_choice():
    return input("> ").lower().strip()

def clear_screen():
    IS_WINDOWS = os.name == "nt"
    IS_MAC = sys.platform == "darwin"
    INTERACTIVE_MODE = not len(sys.argv) > 1  # CLI flags = non-interactive
    if IS_WINDOWS:
        os.system("cls")
    else:
        os.system("clear")
def wait():
    INTERACTIVE_MODE = not len(sys.argv) > 1  # CLI flags = non-interactive
    if INTERACTIVE_MODE:
        input("Push Enter to continue.")
def changelog():
    print("this is W.I.P!")
    wait()
    main()
def main():
    clear_screen()
    print("----------------\n"
          "Cloud-DiscordBot\n"
          "----------------\n")
    print("1. Start Cloud\n"
          "\n"
          "2. Changelog\n"
          "\n"
          "0. Exit\n")
    choice = user_choice()
    if choice == "1":
        clear_screen()
        print("Starting bot..\n")
        time.sleep(2)
        subprocess.call((sys.executable, "cloud.py"))
    if choice == "2":
        changelog()
    if choice == "0":
        clear_screen()
        print("Exited with code '1'")
        sys.exit(1)

start = main()
print(start)
